from _ast import Tuple

from botbuilder.core import CardFactory
from botbuilder.schema import CardImage, CardAction, ActionTypes, ThumbnailCard, Attachment, ReceiptItem, Fact, \
    ReceiptCard, Activity
from datetime import datetime
from tickets import PTicket


# await turn_context.send_activity(MessageFactory.attachment(await messages.function_SETTING(userProfile.language,userProfile.email)))
class Button:
    def __init__(self, title: str, value: str):
        self.title = title
        self.value = value


LIST_OF_COMMAND = [
    "/start", "/help", "/setting", "/ticket", "/opened", "/closed", "/skip", "/cancel"
]


def get_text_from_file(page: int, dialog: int) -> []:
    f = open('textOfMessages', 'r')
    lines = f.readlines()
    number_of_str = 15
    iterator = page * number_of_str + 1
    if lines[iterator][0] == str(page):
        iterator += 1
        while lines[iterator][1] != str(dialog) and lines[iterator][0] == "-":
            iterator = iterator + int(lines[iterator][3])
        if lines[iterator][0] == "-":
            last_line = int(lines[iterator][3])
            for i in range(last_line, iterator + 1):
                list.append(lines[i])
    f.close()


def language_setting() -> Activity:
    return Activity(
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


def create_thumbnail_card(title: str, subtitle: str,
                          text: str, url: str, elements_of_button: Button = []) -> Attachment:
    if len(elements_of_button) != 0:
        button = []
        for elem in elements_of_button:
            button.append(CardAction(
                type=ActionTypes.im_back,
                title=elem.title,
                value=elem.value,
            ))
        return CardFactory.thumbnail_card(ThumbnailCard(title=title,
                                                        subtitle=subtitle,
                                                        text=text,
                                                        images=[
                                                            CardImage(
                                                                url=url,
                                                            )
                                                        ],
                                                        buttons=button,
                                                        )
                                          )


# dialogs before start
def function_TYPE_START():
    eng = "Чтобы начать диалог с ботом напишите ```Start```"
    rus = "To start conversation with bot please write ```Start```"
    return eng, rus


# dialogs for introduction stage

def function_ASK_EMAIL(language: str):
    if language == "English":
        return "Ok It seems, I haven’t met you before. Send me your e-mail address please."
    if language == "Русский":
        return "Продолжим на русском Мне кажется мы не общались раньше. Пожалуйста напишите ваш адрес электронной почты в следующем сообщении"
    if language != "Русский" and language != "English":
        return "It seems, I haven’t met before. Send me your e-mail address please. Мне кажется мы не общались раньше. Пожалуйста напишите ваш адрес электронной почты в следующем сообщении"

def function_EMAIL_INCOR(language:str):
    if language == "English":
        return "Please write innopolis email \n Example: n.surname@innopolis.ru",""
    elif language == "Русский":
        return "","Пожалуйста напишите адрес иннополисовской эл. почты \n Пример: n.surname@innopolis.ru"
    else:
        return "Please write innoplis email \n Example: n.sername@innopolis.ru", "Пожалуйста напишите адрес иннополисовксой эл. почты \n Пример: n.surname@innopolis.ru"


def function_EMAIL_COR(language:str,email:str):
    if language == "English":
        return f"All right! Your email address is {email}"
    elif language == "Русский":
        return f"Хорошо. Твой адрес эл. почты {email}"
    else:
        return f"All right! Your email address is /Хорошо. Твой адрес эл. почты  {userProfile.email}"

async def function_SETTING(language: str, email: str) -> Attachment:
    button = [Button("English", "English"), Button("Русский", "Русский")]
    if language == "English":
        title = "Setting"
        subtitle = "Your current parameters:"
        text = "<ul><li><strong>Language:</strong>        English</li><li><strong>Email</strong>       " + email + "</li></ul>"
    elif language == "Русский":
        title = "Настройки"
        subtitle = "Ваши текущие настройки:"
        text = "<ul><li><strong>Язык:</strong>        Русский</li><li>Эл. адрес       " + email + "</li></ul>"
    else:
        title = "Setting/Настройки"
        subtitle = "Your current parameters:/ Ваши текущие настройки"
        text = "<ul><li><strong>Language/Язык:</strong>        Bilingual/Двуязычный</li><li>Email/Эл.почта       " + email + "</li></ul>"
    return create_thumbnail_card(title, subtitle, text, url="https://static.thenounproject.com/png/993506-200.png",
                                 elements_of_button=button)


# dialogs for manage_question_state funcion
async def function_ASK_QUESTION(language: str) -> Attachment:
    if language == "English":
        title = "Ask your question!"
        subtitle = " All right. All settings are finished. Now, you can ask your question or return to setting."
        text = "Write a question or push button."
        button = [Button("Return to setting", "/setting")]
    elif language == "Русский":
        title = "Задайте свой вопрос!",
        subtitle = " Все настройки завершены, сейчас вы можете задать свой вопрос или вернуться к настрйкам."
        text = "Напишите вопрос или нажмите на кнопку."
        button = [Button("Вернуться к настройкам", "/setting")]
    else:
        title = "Ask your question!/Задайте свой вопрос!"
        subtitle = " All right. All settings are finished. Now, you can ask your question or return to setting./ Все настройки завершены, сейчас вы можете задать свой вопрос или вернуться к настрйкам."
        text = "You should return to setting to set language. /Советуем вам вернуться к настройкам и установить язык."
        button = [Button("Return to setting/Вернуться к настройкам", "/setting")]
    return create_thumbnail_card(title, subtitle, text,
                                 url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg",
                                 elements_of_button=button)


async def function_DID_THAT_HELP(language: str) -> Attachment:
    if language == "English":
        title = "Did that help?"
        subtitle = ""
        text = "Click yes, if your question are solved." \
               "If you want to continue and write question for operator, click no. Click cancel to close question."
        button = [Button("Yes", "Yes"), Button("No", "No"), Button("Cancel", "/cancel")]
    elif language == "Русский":
        title = "Вам помог наш ответ?"
        subtitle = ""
        text = "Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена."
        button = [Button("Да", "Yes"), Button("Нет", "No"), Button("Отмена", "/cancel")]
    else:
        title = "Did that help?/Вам помог наш ответ?"
        subtitle = ""
        text = "If you want to continue and write question for operator, click no. Click cancel to close question." \
               "/Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена."
        button = [Button("Yes/Да", "Yes"), Button("No/Нет", "No"), Button("Cancel/Отмена", "/cancel")]
    return create_thumbnail_card(title, subtitle, text,
                                 "https://www.mtzion.lib.il.us/kids-teens/question-mark.jpg/@@images/image.jpeg",
                                 button)


async def function_ASK_NEW_QUESTION(language: str) -> Attachment:
    if language == "English":
        title = "Do you have any other question?"
        subtitle = "You can ask your next question or change setting."
        text = "Write a question or push button."
        button = [Button("Setting", "/setting")]
    elif language == "Русский":
        title = "Есть еще вопросы?"
        subtitle = "Вы можете задать свой вопрос или изменить настрйки."
        text = "Напишите вопрос или нажмите кнопку."
        button = [Button("Настройки", "/setting")]
    else:
        title = "Do you have any other question? / Есть еще вопросы?"
        subtitle = "You can ask your next question or change setting. / Вы можете задать свой вопрос или изменить настрйки."
        text = "You should return to setting to set language. /Советуем вам вернуться к настройкам и установить язык."
        button = [Button("Setting/Настройки", "/setting")]
    return create_thumbnail_card(title, subtitle, text,
                                 url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg",
                                 elements_of_button=button)


async def function_TYPE_QUESTION(language: str) -> Attachment:
    if language == "English":
        title = "Let's prepare question to send to operator:"
        subtitle = "Please write your question in first line and then add detales, or write /skip to ask question that was writen before, or close question"
        text = "Push button or write question"
        button = [Button("Skip", "/skip"), Button("Close question", "/cancel")]
    elif language == "Русский":
        title = "Давайте подготовим вопрос для оператора"
        subtitle = "Напишите ваш вопрос ниже и добавьте коментарии в следующей строке."
        " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос"
        text = "Нажмите кнопку или введите вопрос."
        button = [Button("Пропустить", "/skip"), Button("Отменить вопрос", "/cancel")]
    else:
        title = "Let's prepare question to send to operator:/ Давайте продготовим вопрос для оператора"
        subtitle = "Please write your question in first line and then add detales, or write" \
                   "/skip to ask question that was writen before, or close question/ ""Напишите ваш вопрос ниже и добавьте коментарии в следующей строке." \
                   " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос"
        text = "Push bottun or write question / Нажмите кнопку или введите вопрос."
        button = [Button("Skip/Пропустить", "/skip"), Button("Close question/Отменить вопрос", "/cancel")]
    return create_thumbnail_card(title, subtitle, text, "https://static.thenounproject.com/png/993506-200.png", button)


async def function_BUILD_QUESTION(question: str, detales: str, language: str, email: str, ticket_id: str) -> Attachment:
    date = datetime.now().timetuple()
    if language == "English":
        title = "Question for operator"
        last_sentence = "Best regards, \n mail  " + email
        ticket_id = f"Ticket id {ticket_id}"
    elif language == "Русский":
        title = "Вопрос для отправки оператору"
        last_sentence = "С наилучшими пожеланиями, \n mail  " + email
        ticket_id = f"Номер запроса {ticket_id}"
    else:
        title = "Question for operator/Вопрос для отправки оператору"
        last_sentence = "Best regards/С наилучшими пожеланиями, \n mail  " + email
        ticket_id = f"Ticket id/Номер запроса {ticket_id}"
    return CardFactory.adaptive_card({
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0",
        "type": "AdaptiveCard",
        "body": [
            {
                "type": "TextBlock",
                "text": title,
                "weight": "bolder",
                "isSubtle": False,
            },
            {"type": "TextBlock", "text": question, "weight": "bolder", "separator": True},
            {"type": "TextBlock", "text": detales, "spacing": "none", "wrap": True},
            {
                "type": "TextBlock",
                "text": last_sentence,
                "weight": "bolder",
                "spacing": "medium",
            },
            {
                "type": "TextBlock",
                "text": ticket_id,
                "weight": "bolder",
                "spacing": "medium",
            },
            {
                "type": "TextBlock",
                "text": str(date[1]) + "/" + str(date[2]) + "/" + str(date[0]),
                "weight": "bolder",
                "spacing": "none",
            },
        ],
    }
    )


def function_TICKET_WAS_CREATED(language: str) -> str:
    if language == "English":
        return "Ticket was created. I will inform you about answer."
    elif language == "Русский":
        return "Запрос создан. Я уведомлю о получении ответа."
    else:
        return "Ticket was created. I will inform you about answer. / Запрос создан. Я уведомлю о получении ответа."


# dialogs for manage_feedback_state funcion
async def function_FEEDBACK(language: str) -> Attachment:
    buttons = [Button(title="😁", value="5"), Button(title="🙂", value="4"), Button(title="😐", value="3"),
               Button(title="😕", value="2"), Button(title="😡", value="1")]
    if language == "English":
        title = "Feedback"
        subtitle = "Thank you for using QnAbot"
        text = "We believe that you have found answer for your question." \
               " To help us improve, we'd like to know your opinion."
    elif language == "Русский":
        title = "Обратная связь"
        subtitle = "Спасибо вам за то, что пользуетесь нашим ботом."
        text = " Мы надеемся, что вы смогли получить ответ на ваш вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота."
    else:
        title = "Feedback/Обратная связь"
        subtitle = "Thank you for using QnAbot, we believe that you have found your answer." \
                   " To help us improve, we'd like to know your opinion./  Спасибо вам за то, что пользуетесь нашим ботом." \
                   " Мы надеемся, что вы смогли получить ответ на ваш вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота."
        text = "Please give a mark to bot. / Поставьте оценку работе бота"
    return create_thumbnail_card(title, subtitle, text
                                 ,
                                 url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU",
                                 elements_of_button=buttons)


async def function_FEEDBACK1(language: str) -> Attachment:
    if language == "English":
        title = "Feedback"
        subtitle = "Thank you for your mark. It is important for us to know your opinion."
        text = "If you want to skip this step, push skip button. Could you please state your opinion in next message."
        button = [Button("Skip", "/skip")]
    elif language == "Русский":
        title = "Обратная связь"
        subtitle = "Спасибо вам за вашу оценку."
        text = " Для нас очень важно знать ваше мнение и интересно читать ваши коментарии. Пожалуйста оставьте отзыв в следующем сообщении. Если вы хотите пропустить этот шаг, нажмите кнопку пропустить."
        button = [Button("Пропустить", "/skip")]
    else:
        title = "Feedback /Обратная связь"
        subtitle = ""
        text = "Thank you for your mark. It is important for us." \
               "Could you please write your opinion in next message. /" \
               "Спасибо вам за вашу оценку. Для нас очень важно знать ваше мнение и интересно читать ваши коментарии. Пожалуйста оставьте отзыв в следующем сообщении."
        button = [Button("Skip/Пропустить", "/skip")]
    return create_thumbnail_card(title, subtitle, text
                                 ,
                                 url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU",
                                 elements_of_button=button)


def function_THANK_YOU(language: str) -> str:
    if language == "English":
        return "Thank you for your feedback!"
    elif language == "Русский":
        return "Спасибо за ваш отзыв!"
    else:
        "Thank you for your feedback!/Cпасибо за ваш отзыв!"


# dialog for help message
async def function_HELP(language: str = "b", state: str = None) -> Attachment:
    width = "110px"
    if language == "English":
        get_text_from_file(0, 2)
        print(list)
        text = list[0]
        about_bot = list[1]
        author = list[2]
        contacts = list[3]
        description_for_command = list[4:9]
    elif language == "Русский":
        text = "Помощь"
        about_bot = "Привет и добро пожаловать в наше приложение. Это бот умеет отвечать на вопросы. Бот может ответить на некоторые вопросы быстро и самостоятелно, а сложные вопросы бот отправит оператору."
        author = "Бот был создан командой студентов."
        contacts = "Вы можете задать ваши вопросы связанные с взаимодействием с ботом --/--"
        description_for_command = [
            "Эта команда позволяет начать диалог со ботом",  # /start
            "Эта команда показывает полный список настроек. Она доступна если бот не формирует вопрос или не "
            "регистрирует пользователя",
            # setting
            "Эта команда отображает полный список из 10 запросов отправленных оператору(открытых и завершенных)",
            # ticket
            "Пропустить некоторые шаги при создании вопроса или составлении отзыва, можно с помщью этой команды",
            # skip
            "Эта команда позволяет закрыть вопрос"  # cencel
        ]
    else:
        text = "Help message /" + "Помощь"
        about_bot = "Hello and welcome to our bot. This bot is able to give answer for your question. " \
                    "Furthermore, some problems can be solved automatically by bot. Unfortunately some problems " \
                    "require human's(Operator's) intervention. / Привет и добро пожаловать в наше приложение. " \
                    "Это бот умеет отвечать на вопросы. Бот может ответить на некоторые вопросы быстро и самостоятелно," \
                    " а сложные вопросы бот отправит оператору."
        author = "Bot was created by team of bachelor students /Бот был создан командой студентов."
        contacts = "You can ask your questions about interaction with bot to --/--"
        description_for_command = [
            "This command start conversation with bot / Эта команда позволяет начать диалог со ботом",  # /start
            "This command open menu of setting (There you can change language). This command available after "
            "initialisation and after you complete to write question / "
            "Эта команда показывает полный список настроек. Она доступна если бот не формирует вопрос или не регистрирует пользователя",
            # setting
            "This command open 10 tickets opened and closed / Эта команда отображает полный список из 10 запросов "
            "отправленных оператору(открытых и завершенных)",  # ticket
            "This command allow you to skip some steps of question creation and feedback writing "
            "/ Пропустить некоторые шаги при создании вопроса или составлении отзыва, можно с помщью этой команды",
            # skip
            "Type this command allow you to close question / Эта команда позволяет закрыть вопрос"  # cancel
        ]
    return CardFactory.adaptive_card({
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": [
            {
                "type": "TextBlock",
                "text": text,
                "separator": True,
                "size": "Medium",
                "weight": "Bolder"
            },
            {
                "type": "TextBlock",
                "text": about_bot,
                "wrap": True,
                "separator": True
            },
            {
                "type": "TextBlock",
                "text": author,
                "wrap": True,
                "separator": True
            },
            {"type": "ColumnSet",
             "columns": [
                 {"type": "Column", "width": width,
                  "items": [{"type": "TextBlock", "text": "List of command"}]},
                 {"type": "Column", "width": "stretch",
                  "items": [{"type": "TextBlock", "text": "Description"}]}
             ], "separator": True},
            {
                "type": "ColumnSet",
                "columns": [
                    {"type": "Column", "width": width,
                     "items": [{"type": "TextBlock", "text": "/start"}],
                     },
                    {"type": "Column", "width": "stretch",
                     "items": [{"type": "TextBlock", "text": description_for_command[0],
                                "wrap": True, "separator": True}]
                     }
                ], "separator": True
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column", "width": width,
                        "items": [{"type": "TextBlock", "text": "/setting "}]
                    },
                    {
                        "type": "Column", "width": "stretch",
                        "items": [{"type": "TextBlock", "text": description_for_command[1],
                                   "wrap": True}]
                    }
                ]
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column", "width": width,
                        "items": [{"type": "TextBlock", "text": " /tickets"
                                   }
                                  ]
                    },
                    {
                        "type": "Column", "width": "stretch",
                        "items": [{"type": "TextBlock", "text": description_for_command[2], "wrap": True
                                   }
                                  ]
                    }
                ]
            },
            {
                "type": "ColumnSet", "columns": [
                {
                    "type": "Column", "width": width,
                    "items": [{"type": "TextBlock", "text": "/skip"
                               }
                              ]
                },
                {
                    "type": "Column", "width": "stretch",
                    "items": [{"type": "TextBlock", "text": description_for_command[3], "wrap": True
                               }
                              ]
                }
            ]
            },
            {
                "type": "ColumnSet", "columns": [
                {
                    "type": "Column", "width": width,
                    "items": [{"type": "TextBlock", "text": "/cancel"}]
                },
                {
                    "type": "Column", "width": "stretch",
                    "items": [{"type": "TextBlock", "text": description_for_command[4], "wrap": True}]
                }]
            },
        ]
    })


# menu of tickets
async def function_TICKETS(language, userProfile) -> Attachment:
    list_of_question = list()
    list_of_question.append({"type": "TextBlock", "text": "Opened tickets"})
    list_of_question.append({
        "type": "ColumnSet",
        "columns": [
            {"type": "Column", "width": "stretch",
             "items": [{"type": "TextBlock", "text": "Question", "weight": "Bolder", "color": "Accent"}]},
            {"type": "Column", "width": "80px",
             "items": [{"type": "TextBlock", "text": "ticket number/date of creation", "color": "Accent",
                        "weight": "Bolder", "wrap": True, "separator": True}]}
        ], "separator": True
    })
    for question in userProfile.opened_ticket:
        list_of_question.append({
            "type": "ColumnSet",
            "columns": [
                {"type": "Column", "width": "stretch",
                 "items": [{"type": "Container",
                            "items": [
                                {"type": "TextBlock", "text": question.question, "wrap": True, "weight": "Bolder"},
                                {"type": "TextBlock", "text": question.detail, "wrap": True}]
                            }]
                 },
                {"type": "Column", "width": "80px",
                 "items": [{"type": "TextBlock", "text": question.number},
                           {"type": "TextBlock", "text": question.date_of_creation}
                           ]}
            ], "separator": True
        })
    return CardFactory.adaptive_card({
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": list_of_question
    })
