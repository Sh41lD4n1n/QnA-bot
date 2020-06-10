from botbuilder.core import CardFactory
from botbuilder.schema import CardImage, CardAction, ActionTypes, ThumbnailCard, Attachment, ReceiptItem, Fact, \
    ReceiptCard

#await turn_context.send_activity(MessageFactory.attachment(await messages.function_SETTING(userProfile.language,userProfile.email)))
DID_THAT_HELP = CardFactory.thumbnail_card(ThumbnailCard(title="Did that help?",
            subtitle="",
            text="Click yes, if your question are solved."
                 " If you want continue and write question for operator, click no. Click cansel to close question",
            images=[
                CardImage(
                    url="https://www.mtzion.lib.il.us/kids-teens/question-mark.jpg/@@images/image.jpeg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Yes",
                    value="Yes",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="No",
                    value="No",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Cancel",
                    value="/cancel",
                ),
            ],
        )
    )
DID_THAT_HELP_rus = CardFactory.thumbnail_card(ThumbnailCard(title="Вам помог наш ответ?",
            subtitle="",
            text="Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена",
            images=[
                CardImage(
                    url="https://www.mtzion.lib.il.us/kids-teens/question-mark.jpg/@@images/image.jpeg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Да",
                    value="Yes",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Нет",
                    value="No",
                ),
                CardAction(
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
async def function_DID_THAT_HELP(language:str)->Attachment:
    if language=="English":
        title = "Did that help?"
        subtitle = ""
        text = "Click yes, if your question are solved."
        " If you want continue and write question for operator, click no. Click cansel to close question"
        button = [Button("Yes","Yes") ,Button("No","No"),Button("Cancel","/cancel")]
    elif language == "Русский":
        title = "Вам помог наш ответ?"
        subtitle = ""
        text = "Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена"
        button = [Button("Да","Yes") ,Button("Нет","No"),Button("Отмена","/cancel")]
    else:
        title = "Did that help?/Вам помог наш ответ?"
        subtitle = ""
        text = "If you want continue and write question for operator, click no. Click cansel to close question"
        "/Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена"
        button = [Button("Yes/Да","Yes") ,Button("No/Нет","No"),Button("Cancel/Отмена","/cancel")]
    return create_thumbnail_card(title,subtitle,text,
                                 "https://www.mtzion.lib.il.us/kids-teens/question-mark.jpg/@@images/image.jpeg",button)
async def function_TYPE_QUESTION(language:str)->Attachment:
    if language=="English":
        title = "Let's prepare question to send operator:"
        subtitle = "Please write your question in first line and then add detales, or write /skip to ask question that was writen before, or close question"
        text = "Push button or write question"
        button =[ Button ("Skip","/skip"),Button("Close question","/cancel")]
    elif language=="Русский":
        title = "Давайте подготовим вопрос для оператора"
        subtitle = "Напишите ваш вопрос ниже и добавьте коментарии в следующей строке."
        " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос"
        text = "Нажмите кнопку или введите вопрос"
        button =[Button("Пропустить","/skip"),Button("Отменить вопрос","/cancel")]
    else:
        title="Let's prepare question to send operator:/ Давайте продготовим вопрос для оператора"
        subtitle = "Please write your question in first line and then add detales, or write"
        "/skip to ask question that was writen before, or close question/ ""Напишите ваш вопрос ниже и добавьте коментарии в следующей строке."
        " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос"
        text="Push bottun or write question / Нажмите кнопку или введите вопрос"
        button =[Button("Skip/Пропустить","/skip"),Button("Close question/Отменить вопрос","/cancel")]
    return create_thumbnail_card(title,subtitle,text,"https://static.thenounproject.com/png/993506-200.png",button)
async def function_SETTING(language:str,email:str)->Attachment:
    button = [Button("English", "English"), Button("Русский", "Русский")]
    if language=="English":
        title = "Setting"
        subtitle = "Your current paramenters:"
        text = "<ul><li><strong>Language:</strong>        English</li><li><strong>Email</strong>       " + email + "</li></ul>"
    elif language=="Русский":
        title = "Настройки"
        subtitle = "Ваши текущие настройки:"
        text = "<ul><li><strong>Язык:</strong>        Русский</li><li>Эл. адрес       " + email + "</li></ul>"
    else:
        title = "Setting/Настройки"
        subtitle = "Your current paramenters:/ Ваши текущие настройки"
        text = "<ul><li><strong>Language/Язык:</strong>        Bilingual/Двуязычный</li><li>Email/Эл.почта       " + email + "</li></ul>"
    return create_thumbnail_card(title,subtitle,text,url="https://static.thenounproject.com/png/993506-200.png",elements_of_button=button)

async def function_ASK_QUESTION(language:str)->Attachment:
    if language=="English":
        title = "Ask your question!"
        subtitle = " All right. All settings are finished. Now, you can ask your first question or return to setting"
        text=""
        button=[Button("Return to setting","/setting")]
    elif language=="Русский":
        title = "Задайте свой вопрос!",
        subtitle = " Все настройки завершены, сейчас вы можете задать свой вопрос или вернуться к настрйкам"
        text = ""
        button=[Button("Вернуться к настройкам","/setting")]
    else:
        title = "Ask your question!/Задайте свой вопрос!"
        subtitle = " All right. All settings are finished. Now, you can ask your first question or return to setting/ Все настройки завершены, сейчас вы можете задать свой вопрос или вернуться к настрйкам"
        text = "You should return to setting to set language/Советуем вам вернуться к настройкам и установить язык"
        button=[Button("Return to setting/Вернуться к настройкам","/setting")]
    return create_thumbnail_card(title,subtitle,text,
           url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg",elements_of_button=button)
async def function_ASK_NEW_QUESTION(language:str)->Attachment:
    if language=="English":
        title = "Do you have any other question?"
        subtitle = "You can ask your next question or change setting"
        text=""
        button=[Button("Setting","/setting")]
    elif language=="Русский":
        title = "Есть еще вопросы?"
        subtitle = "Вы можете задать свой вопрос или изменить настрйки"
        text = ""
        button=[Button("Настройки","/setting")]
    else:
        title = "Do you have any other question? / Есть еще вопросы?"
        subtitle = "You can ask your next question or change setting / Вы можете задать свой вопрос или изменить настрйки"
        text=""
        button=[Button("Setting/Настройки","/setting")]
    return create_thumbnail_card(title,subtitle,text,
         url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg",elements_of_button=button)
async def function_FEEDBACK(language:str)->Attachment:
    buttons = [Button(title="😁",value="5"),Button(title="🙂",value="4"),Button(title="😐",value="3"),Button(title="😕",value="2"),Button(title="😡",value="1")]
    if language=="English":
        title = "Feedback"
        subtitle = "Thank you for using QnAbot, we belive you have found your answer."
        " To help us improve, we'd like to know your opinion."
        text = "Please give a mark to bot."
    elif language=="Русский":
        title = "Обратная связь"
        subtitle = "Спасибо вам за то, что пльзуетесь нашим ботом."
        " Мы надеемся вы смогли получить ответ за свой вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота."
        text = "Поставьте оценку работе бота"
    else:
        title = "Feedback/Обратная связь"
        subtitle = "Thank you for using QnAbot, we belive you have found your answer."
        " To help us improve, we'd like to know your opinion./  Спасибо вам за то, что пльзуетесь нашим ботом."
        " Мы надеемся вы смогли получить ответ за свой вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота."
        text = "Please give a mark to bot. / Поставьте оценку работе бота"
    return create_thumbnail_card(title,subtitle,text
         ,url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU",elements_of_button=buttons)
async def function_FEEDBACK1(language: str) -> Attachment:
        if language == "English":
            title = "Feedback"
            subtitle = "Thank you for your mark. It is important for us."
            "Could you please write your opinion in next message."
            text = "If you want to skip this step push skip button"
            button = [Button("Skip","/skip")]
        elif language == "Русский":
            title = "Обратная связь"
            subtitle = "Спасибо вам за вашу оценку."
            text = " Для нас очень важно знать ваше мнение и интересно читать ваши коментарии. Напишите отзыв в следующем сообщении или нажмите кнопку пропустить"
            button = [Button("Пропустить","/skip")]
        else:
            title = "Feedback /Обратная связь"
            subtitle = "Thank you for your mark. It is important for us."
            "Could you please write your opinion in next message. / Спасибо вам за вашу оценку. Для нас очень важно знать ваше мнение и интересно читать ваши коментарии"
            text = "If you want to skip this step push skip button/ Напишите отзыв в следующем сообщении или нажмите кнопку пропустить"
            button = [Button("Skip/Пропустить","/skip")]
        return create_thumbnail_card(title,subtitle,text
             ,url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU",elements_of_button=button)

async def function_BUILD_QUESTION(question:str,detales:str,language:str,email:str)->Attachment:
    if language=="English":
        title = "Question for operator"
        last_sentence="best regards \n mail  "+email
    elif language=="Русский":
        title = "Вопрос для отправки оператору"
        last_sentence = "С наилучшими пожеланиями, \n mail  " + email
    else:
        title = "Question for operator/Вопрос для отправки оператору"
        last_sentence = "best regards/С наилучшими пожеланиями, \n mail  " + email
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
            {"type": "TextBlock", "text": detales, "spacing": "none"},
            {
                "type": "TextBlock",
                "text": last_sentence,
                "weight": "bolder",
                "spacing": "medium",
            },
            {
                "type": "TextBlock",
                "text": "Fri, October 10 8:30 AM",
                "weight": "bolder",
                "spacing": "none",
            },
        ],
    }
    )
async def function_HELP (language:str="b",state:str=None)->Attachment:
        if language=="English":
            text = "Help message"
            about_bot = "Hello and welcome to our bot. This bot can give answer for your question. Bot able to give answer for some problems in automatic mode and send other questions to Operators."
            author = "Bot was created by ---/---"
            description_for_command=[
                "Start conversation with user",      #/start
                "Show list of all setting. You can change langauge here. This command available after initialisation and when you finish to write question", #setting
                "Write this comand to see all ticktes opend and closed",     #ticket
                "",#skip
                "Type this command to close question" #skip
            ]
        elif language=="Русский":
            text = "Помощь"
            about_bot = "Привет и добро пожаловать в наше приложение. Это бот умеет отвечать на вопросы. Бот может ответить на некоторые вопросы быстро и спмостоятелно. Сложные вопросы бот отправляет оператору."
            author = "Бот был создан ---/---"
            description_for_command = [
                "Чтобы начать первый диалог с ботом нужно написать эту команду",  # /start
                "Эта команда показывает полный список настроек. Она доступна если бот не формирует вопрос или не ригистрирует пользователя",
                # setting
                "Отображает полный список всех запросов отправленных оператору",  # ticket
                "Пропустить некоторые шаги при создании вопроса или составлении отзыва, можно с помщью команды /skip",  # skip
                "Отменить вопрос"  # cencel
            ]
        else:
            text = "Help message /"+"Помощь"
            about_bot = "Hello and welcome to our bot. This bot can give answer for your question. Bot able to give answer for some problems in automatic mode and send other questions to Operators. /"+"Привет и добро пожаловать в наше приложение. Это бот умеет отвечать на вопросы. Бот может ответить на некоторые вопросы быстро и спмостоятелно. Сложные вопросы бот отправляет оператору."
            author = "Bot was created by /"+ "Бот был создан ---/---"
            description_for_command = [
                "Start conversation with user /"+"Чтобы начать первый диалог с ботом нужно написать эту команду",  # /start
                "Show list of all setting. You can change langauge here. This command available after initialisation and when you finish to write question/"+"Эта команда показывает полный список настроек. Она доступна если бот не формирует вопрос или не ригистрирует пользователя",
                # setting
                "Write this comand to see all ticktes opend and closed / "+"Отображает полный список всех запросов отправленных оператору",  # ticket
                ""+"Пропустить некоторые шаги при создании вопроса или составлении отзыва, можно с помщью команды /skip",  # skip
                "Type this command to close question/"+"Отменить вопрос"  # skip
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
                     {"type": "Column", "width": "100px",
                      "items": [{"type": "TextBlock", "text": "List of command"}]},
                     {"type": "Column", "width": "stretch",
                      "items": [{"type": "TextBlock", "text": "Description"}]}
                 ], "separator": True},
                {
                    "type": "ColumnSet",
                    "columns": [
                        {"type": "Column", "width": "100px",
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
                            "type": "Column", "width": "100px",
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
                            "type": "Column", "width": "100px",
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
                        "type": "Column", "width": "100px",
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
                        "type": "Column", "width": "100px",
                        "items": [{"type": "TextBlock", "text": "/cancel"}]
                    },
                    {
                        "type": "Column", "width": "stretch",
                        "items": [{"type": "TextBlock", "text": description_for_command[4], "wrap": True}]
                    }]
                },
            ]
        })