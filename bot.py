# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import asyncio
from botbuilder.core import ActivityHandler, TurnContext, ConversationState, UserState, MessageFactory
from botbuilder.core.teams import TeamsInfo
from botbuilder.schema import ChannelAccount, Activity

from conversation_data import ConversationData
import messages
from user_profile import UserProfile
from datetime import datetime
import codecs


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self, conversation_state: ConversationState, user_state: UserState, queue: asyncio.Queue):
        if conversation_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. user_state is required but None was given"
            )
        self.conversation_state = conversation_state
        self.user_state = user_state
        self.conversation_data_accessor = self.conversation_state.create_property("ConversationData")
        self.user_profile_accessor = self.user_state.create_property("UserProfile")
        self.queue = queue

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        '''
        This function was called by server. It is a main function of program that call other function to reply on message
        :param turn_context contain message that have been sent by user
        VARIABLES
        userProfile is object of class userProfile, that contain user's information
        conversation_data is object of class ConversationData, that contain current conversation state of program
        message is a text that was printed by user
        STAGES
        '''
        userProfile = await self.user_profile_accessor.get(turn_context, UserProfile)
        conversation_data = await self.conversation_data_accessor.get(turn_context, ConversationData)
        message = turn_context.activity.text

        # commands available in any stage of bot


        if message == "Start":
            # conversation between user and bot start with "Start" comamnd
            # bot ask to choose language first (function create a card with question)
            await turn_context.send_activity(messages.language_setting())
            conversation_data.state = "start"
            return

        if message == "/help":
            # print help message
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_HELP(userProfile.language)))
            return

        if message != "Start" and conversation_data.state == "None":
            # ask user type /start
            # print two messages on different languages
            eng, rus = messages.function_TYPE_START()
            await turn_context.send_activity(MessageFactory.text(eng))
            await turn_context.send_activity(MessageFactory.text(rus))
            return

        # stages: if user have wrote start, then bot reply
        if conversation_data.state != None:
            # first stage for new user: set language
            if conversation_data.state == "start":
                # message contain message with sellected language
                # if language don't changed, then message from bot will be printed in two languages
                if message == "English":
                    userProfile.language = "English"
                if message == "Русский":
                    userProfile.language = "Русский"
                # ask user write email and move to introduction stage
                await turn_context.send_activity(messages.function_ASK_EMAIL(language=userProfile.language))
                conversation_data.state = "introduction"
                return
            # introduction stage
            # next step for new user write his/her email
            if conversation_data.state == "introduction":
                # if email correct then function return true and set email
                return await self.set_email(turn_context, userProfile,conversation_data)


            # setting stage
            # in any moment user can change settings
            #there program catch changes
            if conversation_data.state == "setting":
                if message=="English" or message=="Русский":
                    userProfile.language = message
                #move to question state
                conversation_data.state = "menu0"
                await self.manage_menu_state(turn_context, userProfile, conversation_data)
                return

            if conversation_data.state=="menu":
                await self.manage_menu_state(turn_context,userProfile,conversation_data)
            # question stage
            # if user write his/her email, he can ask question
            if conversation_data.state.rfind("question") == 0:
                await self.manage_question_state(conversation_data, turn_context, userProfile)
            # feedback state
            if conversation_data.state.rfind("feedback") == 0:
                await self.manage_feedback_state(userProfile.language, turn_context, conversation_data, userProfile)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        '''This function perform operation at the moment user is added
        '''
        conversation_data = await self.conversation_data_accessor.get(turn_context, ConversationData)
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                if turn_context.activity.text == "Start":
                    # Dialog start, when user write "/start"
                    userProfile = await self.user_profile_accessor.get(turn_context, UserProfile)
                    await turn_context.send_activity(messages.language_setting())
                    conversation_data.state = "start"
                elif turn_context.activity.text == "/help":
                    await turn_context.send_activity(MessageFactory.attachment(await messages.function_HELP("b")))
                else:
                    await turn_context.send_activity(
                        MessageFactory.text("To start conversation with bot please write ```Start```"))
                    await turn_context.send_activity(
                        MessageFactory.text("Чтобы начать диалог с ботом напишите ```Start```"))

    async def set_email(self, turn_context, userProfile,conversation_data):
        message = turn_context.activity.text
        if message.endswith("@innopolis.university") or message.endswith("@innopolis.ru"):
            #get email
            userProfile.email = message
            await turn_context.send_activity(MessageFactory.text(messages.function_EMAIL_COR(userProfile.language,userProfile.email)))
            member = await TeamsInfo.get_member(turn_context, turn_context.activity.from_property.id)
            await turn_context.send_activity(member.user_principal_name)
            userProfile.create_user_id(member.user_principal_name)
            # move to question stage
            conversation_data.state = "menu0"
            # write instruction for question state
            await self.manage_menu_state(turn_context=turn_context,userProfile=userProfile,conversation_data=conversation_data)
        else:
            reply = messages.function_EMAIL_INCOR(userProfile.language)
            for text in reply:
                await turn_context.send_activity(MessageFactory.text(text))

    async def manage_menu_state(self,turn_context:TurnContext,userProfile,conversation_data):
        message=turn_context.activity.text
        #this message will be printed when user will move to menu state
        if conversation_data.state=="menu0":
            await turn_context.send_activity(MessageFactory.attachment(await messages.function_MENU(userProfile.language)))
            conversation_data.state="menu"
            return
        if message == "/tickets":
            #TODO:Manange ticket state
            # print all tickets
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_TICKETS(userProfile.language, userProfile)))
            return
        elif message=="/create_ticket":
            conversation_data.state="question"
            await self.manage_question_state(conversation_data,turn_context,userProfile)
        elif message=="/setting":
            # process setting
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_SETTING(userProfile.language, userProfile.email)))
            conversation_data.state = "setting"
            return



    async def manage_question_state(self, conversation_data, turn_context, userProfile):
        '''
        This function create a question, send it to knowledge base and create ticket for operator
        :param conversation_data contain state ("question"-first state,"question1"-second state, "question2"-third state)
        :param turn_context command turn_context.send_activity.text give text of message and this parameter allow to print message
        :param userProfile provide user's information (language, current question, email) and add ticket
                first state: In this state function wait commands: "/setting", "/tickets","/help"
           (program catch two last command in on_message_activity) and question (text message).
                    If /setting, then write setting menu and move tos setting state
                    If question is received, then save question in userProfile, suggest answer from db
                received "yes" message: If answer from db is satisfied, then move to feedback state (to manage_feedback_function)
                second state: If answer for db is not satisfied, then ask user add details or type /skip command then move to third state
                third state: receive command or details from user and create a ticket, and then move to feedback state

         '''
        message = turn_context.activity.text
        # first state
        if conversation_data.state == "question":
            await turn_context.send_activity("Я внимательно слушаю")
            # get question, suggest answer from db and save question in userProfile
            # save question
            userProfile.question = message
            # send to user answer from knowledge base
            await turn_context.send_activity(
                MessageFactory.text(await self.get_answer_from_knowledge_base(message)))
            # ask question. If answer is yes, then move to feedback. If answer is "/cansel", then move to first state
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_DID_THAT_HELP(userProfile.language)))
            # move to second state
            conversation_data.state = "question1"
            return

        # recived "yes" message: if attempt is success, then move to feedback state (to manage_feedback_function)
        if message == "Yes" and conversation_data.state == "question1":
            conversation_data.state = "feedback"
            return
        if message == "/cancel":
            conversation_data.state = "menu0"
            await self.manage_menu_state(turn_context,userProfile,conversation_data)
            return

        # second state
        if conversation_data.state == "question1" and message == "No":
            # suggest to user add details or type /skip
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_TYPE_QUESTION(userProfile.language)))
            # move to third state
            conversation_data.state = "question2"
            return

        # third state
        if conversation_data.state == "question2":
            details = ""
            # if user type /skip command, then tickets will contain only question
            if message == "/skip":
                details = ""
            # if user type text, then tickets will contain question and details
            else:
                details = message
            # create ticket
            ticket_id = userProfile.add_question(details=details)
            # print ticket (print: title, details,date,email,ticket_id)
            await turn_context.send_activity(MessageFactory.attachment(
                await messages.function_BUILD_QUESTION(userProfile.question, details, userProfile.language,
                                                       userProfile.email, ticket_id)))
            # notify user, that ticket wascreated
            await turn_context.send_activity(
                MessageFactory.text(messages.function_TICKET_WAS_CREATED(userProfile.language)))
            #wait task in paralel
            asyncio.get_running_loop().create_task(self.get_answer_from_operator(ticket_id))
            # move to feedack state
            conversation_data.state = "feedback"
            return

    async def manage_feedback_state(self, language, turn_context: TurnContext, conversation_data, userProfile):
        '''
            This function get feedback from user and store it in file feedback
            :param conversation_data contain state ("question"-first state,"question1"-second state, "question2"-third state)
            :param turn_context command turn_context.send_activity.text give text of message and this parameter allow to print message
            :param userProfile provide user's information (language) and save mark
            first state: ask user give mark (is number from1 to 5) and move to second state
            second state: save user's mark and ask user to give a coments
            third state: save user's coment and move to question state

        '''
        # first state
        if conversation_data.state == "feedback":
            # ask user give mark (is number from1 to 5)
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_FEEDBACK(language)))
            # move to second state
            conversation_data.state = "feedback1"
        # second state
        elif conversation_data.state == "feedback1":
            # save user's mark
            userProfile.mark = turn_context.activity.text
            # ask user to give a coments
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_FEEDBACK1(language)))
            # move to third state
            conversation_data.state = "feedback2"
        # third state
        elif conversation_data.state == "feedback2":
            # write "Thank you for your feedback"
            await turn_context.send_activity(MessageFactory.text(messages.function_THANK_YOU(language)))
            # save coments(it can be "/skip" or text)
            details=turn_context.activity.text
            asyncio.get_running_loop().create_task(self.send_feedback(
                    userProfile.mark, self.queue,details))
            # print message and move to quetion state
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_ASK_NEW_QUESTION(language)))
            conversation_data.state = "menu0"
            await self.manage_menu_state(turn_context,userProfile,conversation_data)

    async def send_feedback(self, mark: str, queue: asyncio.Queue, feedback: str = ""):
        # Function send_feedback write feedback to file feedback.txt
        time_sleep = await queue.get()
        await asyncio.sleep(time_sleep)
        time_sleep = time_sleep + 4 * 0.25
        await queue.put(time_sleep % 5)
        f = codecs.open("feedback.txt", "r", "utf-8")
        line = f.readlines()[0]
        f.close()

        i = 0
        while line[i] != " ":
            i = i + 1
        i = i + 1
        sum = ""
        while line[i] != ",":
            sum = sum + line[i]
            i = i + 1
        try:
            sum = int(sum) + int(mark)
        except ValueError:
            sum = int(sum)
        number_of_questions = ""

        while line[i] != " ":
            i = i + 1
        while line[i] != ",":
            number_of_questions = number_of_questions + line[i]
            i = i + 1
        number_of_questions = int(number_of_questions) + 1
        output=f"Avarage_mark={round(sum/number_of_questions,2)},Sum {sum},Number_of_questions {number_of_questions},\n"
        if len(output)<len(line):
            output=output+", ,"*(len(line)-len(output))
        f = codecs.open("feedback.txt", "r+", "utf-8")
        f.write(output)
        f.close()

        f = codecs.open("feedback.txt", "a", "utf-8")
        f.write(f"Mark: {mark} Feedback {feedback} \n")
        f.close()

        queue.task_done()

    async def get_answer_from_knowledge_base(self, question: str) -> str:
        # TODO: Add data base here
        await asyncio.sleep(3)
        return ("Your answer is " + question)

    async def get_answer_from_operator(self, ticket_id:str) -> str:
        # TODO: Add answer here
        await asyncio.sleep(3)
        return "get_answer_from_operator-"+f"Dear user. I am operator your ticket id is: {ticket_id}"

