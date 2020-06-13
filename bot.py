# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import asyncio
from botbuilder.core import ActivityHandler, TurnContext, ConversationState, UserState, MessageFactory
from botbuilder.schema import ChannelAccount, Activity

from conversation_data import ConversationData
import messages
from user_profile import UserProfile
from datetime import datetime
import codecs


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    def __init__(self,conversation_state:ConversationState, user_state: UserState,queue:asyncio.Queue):
        if conversation_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[StateManagementBot]: Missing parameter. user_state is required but None was given"
            )
        self.conversation_state=conversation_state
        self.user_state=user_state
        self.conversation_data_accessor = self.conversation_state.create_property("ConversationData")
        self.user_profile_accessor=self.user_state.create_property("UserProfile")
        self.queue=queue

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_message_activity(self, turn_context: TurnContext):
        userProfile = await self.user_profile_accessor.get(turn_context, UserProfile)
        conversation_data = await self.conversation_data_accessor.get(turn_context, ConversationData)
        message = turn_context.activity.text

#first stage
        if message=="/start":
            #conversation between user and bot start with "/start" comamnd
            #bot ask to choose language first(function create a card with question)
            await self.language_setting(turn_context)
            conversation_data.state="start"
            return
        if message=="/help":
            await turn_context.send_activity(MessageFactory.attachment(await messages.function_HELP(userProfile.language)))
            return
        if message!="/start" and conversation_data.state=="None":
            await turn_context.send_activity(MessageFactory.text("To start conversation with bot please write ```/start```"))
            await turn_context.send_activity(MessageFactory.text("Чтобы начать диалог с ботом напишите ```/start```"))
            return
        if message == "/tickets":
            print(message)
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_TICKETS(userProfile.language, userProfile)))
            return
#language setting stage
        #if user have wrote start, then bot reply
        if conversation_data.state!=None:
            #first step for new user set language
            if conversation_data.state=="start":
                if message=="English":
                    userProfile.language="English"
                if message=="Русский":
                    userProfile.language = "Русский"
                await self.new_user(turn_context,userProfile.language)
                conversation_data.state = "introduction"
                return
#introduction stage
            #next step for new user write his/her email
            if conversation_data.state == "introduction":
                #if email correct then function return true
                if await self.set_email(turn_context,userProfile):
                    userProfile.create_id()
                    conversation_data.state = "question"
                    await turn_context.send_activity(MessageFactory.attachment(
                        await messages.function_ASK_QUESTION(userProfile.language)))
                    return
#setting stage
            #in any moment user can change settings
            if conversation_data.state=="setting":
                userProfile.language = message
                await turn_context.send_activity(MessageFactory.attachment(
                    await messages.function_ASK_NEW_QUESTION(userProfile.language)))
                conversation_data.state="question"
                return
#question stage
            #if user write his/her email, he can ask question
            if conversation_data.state.rfind("question")==0:
                await self.solve_question(conversation_data,turn_context,userProfile)
#feedback state
            if conversation_data.state.rfind("feedback")==0:
                await self.get_feedback(userProfile.language,turn_context,conversation_data,userProfile)



    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        conversation_data = await self.conversation_data_accessor.get(turn_context, ConversationData)
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                if turn_context.activity.text=="/start":
                    #Dialog start, when user write "/start"
                    userProfile = await self.user_profile_accessor.get(turn_context, UserProfile)
                    await self.language_setting(turn_context)
                    conversation_data.state="start"
                elif turn_context.activity.text=="/help":
                    await turn_context.send_activity(MessageFactory.attachment(await messages.function_HELP("b")))
                else:
                    await turn_context.send_activity(MessageFactory.text("To start conversation with bot please write ```/start```"))
                    await turn_context.send_activity(MessageFactory.text("Чтобы начать диалог с ботом напишите ```/start```"))




    async def set_email(self,turn_context,userProfile):
        message = turn_context.activity.text
        if message.endswith("@innopolis.university") or message.endswith("@innopolis.ru"):
            userProfile.email = message
            if userProfile.language == "English":
                await turn_context.send_activity(f"All right! Your email address is {userProfile.email}")
            if userProfile.language == "Русский":
                await turn_context.send_activity(f"Хорошо. Твой адрес эл. почты {userProfile.email}")
            if userProfile.language =="b":
                await turn_context.send_activity(f"All right! Your email address is {userProfile.email}")
                await turn_context.send_activity(f"Хорошо. Твой адрес эл. почты {userProfile.email}")
            return True
        else:
            if userProfile.language == "English":
                await turn_context.send_activity("Please write innopolis email")
                await turn_context.send_activity("Example: n.surname@innopolis.ru")
            if userProfile.language == "Русский":
                await turn_context.send_activity("Пожалуйста напишите адрес иннополисовской эл. почты")
                await turn_context.send_activity("Пример: n.surname@innopolis.ru")
            if userProfile.language == "b":
                await turn_context.send_activity("Please write innoplis email")
                await turn_context.send_activity("Example: n.sername@innopolis.ru")
                await turn_context.send_activity("Пожалуйста напишите адрес иннополисовксой эл. почты")
                await turn_context.send_activity("Пример: n.surname@innopolis.ru")
            return False

    async def new_user(self,turn_context,language):
        #Then email will be asked
        if language=="English":
            await turn_context.send_activity(
                MessageFactory.text("Ok"))
            await turn_context.send_activity(MessageFactory.text("It seems, I haven’t met you before. Send me your e-mail address please."))
        if language=="Русский":
            MessageFactory.text("Продолжим на русском")
            await turn_context.send_activity(MessageFactory.text("Мне кажется мы не общались раньше. Пожалуйста напишите ваш адрес электронной почты в следующем сообщении"))
        if language!="Русский" and language!="English":
            await turn_context.send_activity(MessageFactory.text("It seems, I haven’t met before. Send me your e-mail address please."))
            await turn_context.send_activity(MessageFactory.text("Мне кажется мы не общались раньше. Пожалуйста напишите ваш адрес электронной почты в следующем сообщении"))

    async def solve_question(self,conversation_data,turn_context,userProfile):
        message = turn_context.activity.text

        # first step get "/setting" or question
        if conversation_data.state == "question":
            # process setting
            if message == "/setting":
                await turn_context.send_activity(MessageFactory.attachment(await messages.function_SETTING(userProfile.language,userProfile.email)))
                conversation_data.state = "setting"
                return
            # search result in database, first attempt
            conversation_data.state = "question2"
            await turn_context.send_activity(
                MessageFactory.text(await self.get_answer_from_knowledge_base(message)))
            userProfile.question = message
            #reply
            await turn_context.send_activity(MessageFactory.attachment(await messages.function_DID_THAT_HELP(userProfile.language)))
            return

        # if attempt is success, then ask feedback
        if message == "Yes":
            conversation_data.state = "feedback"
            await turn_context.send_activity(
                MessageFactory.text("Feedback:"))
            return
        if message == "/cancel":
            conversation_data.state = "question"
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_ASK_NEW_QUESTION(userProfile.language)))
            return
        # search result in database, second attempt
        if conversation_data.state == "question1" and message == "No":
            await turn_context.send_activity(
            MessageFactory.text(await self.get_answer_from_knowledge_base(message)))
            conversation_data.state = "question2"
            await turn_context.send_activity(MessageFactory.attachment(await messages.function_DID_THAT_HELP(userProfile.language)))
            return

        # ask user create ticket
        if conversation_data.state == "question2" and message == "No":
            conversation_data.state = "question3"
            await turn_context.send_activity(MessageFactory.attachment(await messages.function_TYPE_QUESTION(userProfile.language)))
            return

        # create ticket
        if conversation_data.state == "question3":
            conversation_data.state = "question"
            if message=="/skip":
                await turn_context.send_activity(MessageFactory.attachment(
                    await messages.function_BUILD_QUESTION(userProfile.question, "", userProfile.language,
                                           userProfile.email)))
                date = datetime.now().timetuple()
                userProfile.add_question(question=userProfile.question,date_of_creation=str(date[1])+"/"+str(date[2])+"/"+str(date[0]))
                '''loop=asyncio.get_running_loop()
                loop.create_task(self.get_answer_from_operator(userProfile.question,userProfile.email),name="request")'''

            else:
                index = message.find("\n")
                date = datetime.now().timetuple()
                userProfile.add_question(question=message[0:index],
                                         date_of_creation=str(date[1]) + "/" + str(date[2]) + "/" + str(date[0]),detail=message[index+1:])
                await turn_context.send_activity(MessageFactory.attachment(await messages.function_BUILD_QUESTION(message[0:index],message[index+1:],userProfile.language,userProfile.email)))
                '''loop=asyncio.get_running_loop()
                loop.create_task(self.get_answer_from_operator(message[0:index],userProfile.email,message[index+1:]))'''
            if userProfile.language=="English":
                await turn_context.send_activity(
                    MessageFactory.text("Ticket was created. I will inform you about answer."))
            elif userProfile.language=="Русский":
                await turn_context.send_activity(
                    MessageFactory.text("Запрос создан. Я уведомлю о получении ответа."))
            else:
                await turn_context.send_activity(
                    MessageFactory.text("Ticket was created. I will inform you about answer."))
                await turn_context.send_activity(
                    MessageFactory.text("Запрос создан. Я уведомлю о получении ответа."))
            conversation_data.state="feedback"
            return


    async def get_feedback(self,language,turn_context:TurnContext,conversation_data,userProfile):
        if conversation_data.state=="feedback":
            await turn_context.send_activity(
            MessageFactory.attachment(await messages.function_FEEDBACK(language)))
            conversation_data.state="feedback1"
        elif conversation_data.state=="feedback1":
            userProfile.mark=turn_context.activity.text
            await turn_context.send_activity(
                MessageFactory.attachment(await messages.function_FEEDBACK1(language)))
            conversation_data.state = "feedback2"
        elif conversation_data.state=="feedback2":
            if language=="English":
                await turn_context.send_activity(
                    MessageFactory.text("Thank you for your feedback!"))
            elif language=="Русский":
                await turn_context.send_activity(
                    MessageFactory.text("Спасибо за ваш отзыв!"))
            else:
                await turn_context.send_activity(
                    MessageFactory.text("Thank you for your feedback!/Cпасибо за ваш отзыв!"))

            if turn_context.activity.text!="/skip":
                    asyncio.get_running_loop().create_task(self.send_feedback(
                        userProfile.mark,self.queue,turn_context.activity.text))

            await turn_context.send_activity(
                    MessageFactory.attachment(await messages.function_ASK_NEW_QUESTION(language)))
            conversation_data.state = "question"

    async def card_before_question(self,turn_context,language:str="b",q:str=""):
        if language=="English":
            await turn_context.send_activity(
                MessageFactory.text("<b>Write your "+q+" question</b>. All right. All settings are finished."
                                "Now, you can ask your first question or return to setting (/setting)"))
        if language == "Русский":
            await turn_context.send_activity(
                MessageFactory.text("<b>Напиши свой первый вопрос</b> Все настройки завершены,"
                                " сейчас вы можете задать свой первый вопрос или вернуться к настрйкам /setting"))
        if language=="b":
            await turn_context.send_activity(
                MessageFactory.text("<b>Write your first question</b>. All right. All settings are finished."
                                    "Now, you can ask your first question or return to setting (/setting)"
                                    "Note: You skiped language settings. To set language write/setting"))
            await turn_context.send_activity(
                MessageFactory.text("<b>Напиши свой первый вопрос</b> Все настройки завершены,"
                                    " сейчас вы можете задать свой первый вопрос или вернуться к настрйкам /setting"
                                    "Напоминаю, что вы пропустили настройки языка. Чтобы настроить язык вернитесь к настройкам/setting"))


    async def language_setting(self, turn_context):
        attach = Activity(
            attachments=[
                {
                    "contentType": "application/vnd.microsoft.card.thumbnail",
                    "content": {
                        "title": "Hello! It is IT Department help bot!📣 /Привет! Это бот-помощник от Департамента ИТ 📣",
                        "text": "Now, choose your language! 😊/ Выбери язык 😊",
                        "buttons": [
                            {
                                "type": "imBack",
                                "title": "English",
                                "image": "http://moopz.com/assets_c/2012/06/emoji-thumbs-up-150-thumb-autox125-140616.jpg",
                                "value": "English"
                            },
                            {
                                "type": "imBack",
                                "title": "Русский",
                                "image": "https://linguacontact.com/wp-content/uploads/russia-flag.png",
                                "value": "Русский"
                            },
                        ],
                    }
                }
            ],
        )
        await turn_context.send_activity(attach)

    async def send_feedback (self,mark:str,queue:asyncio.Queue,feedback:str=""):
        time_for_sleep=await queue.get()
        time_for_sleep=(time_for_sleep/0.125+4)*0.125
        await queue.put(time_for_sleep%11)
        await asyncio.sleep(time_for_sleep)
        f=codecs.open("output","a","utf-8")
        f.write(f"Mark: {mark} Feedback {feedback} \n")
        f.close()
        queue.task_done()
    async def get_answer_from_knowledge_base(self,question:str)->str:
        await asyncio.sleep(3)
        return ("Your answer is "+question)
    async def get_answer_from_operator(self, title:str,email:str,text:str="")->str:
        await asyncio.sleep(60)
        question=title+"\n"+ text
        return (f"Dear {email}. I am operator your answer is: {question}")