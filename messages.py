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
                    title="Отмена",
                    value="/cencel",
                )
            ],
        )
    )
DID_THAT_HELP_b = CardFactory.thumbnail_card(ThumbnailCard(title="Did that help?/Вам помог наш ответ?",
            subtitle="",
            text="If you want continue and write question for operator, click no. Click cansel to close question"
                 "/Отправьте да, если вопрос решён. Если вы хотите задать вопрос оператору, напишите нет. Если вы хотите закрыть вопрос, нажмите отмена",
            images=[
                CardImage(
                    url="https://www.mtzion.lib.il.us/kids-teens/question-mark.jpg/@@images/image.jpeg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Yes/Да",
                    value="Yes",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="No/Нет",
                    value="No",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Cancel/Отмена",
                    value="/cencel",
                )
            ],
        )
    )
async def function_TYPE_QUESTION(language:str)->Attachment:
    if language=="English":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Let's prepare question to send operator:",
                subtitle="Please write your question in first line and then add detales, or write"
                         "/skip to ask question that was writen before, or close question",
                text="Push bottun or write question",
                images=[
                    CardImage(
                        url="https://static.thenounproject.com/png/993506-200.png"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Skip",
                        value="/skip",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Close question",
                        value="/close",
                    ),
                ],
            )
        )
    elif language=="Русский":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Давайте подготовим вопрос для оператора",
            subtitle="Напишите ваш вопрос ниже и добавьте коментарии в следующей строке."
                     " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос",
            text="Нажмите кнопку или введите вопрос",
            images=[
                CardImage(
                    url="https://static.thenounproject.com/png/993506-200.png"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Пропустить",
                    value="/skip",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Закрыть вопрос",
                    value="/cencel",
                ),
            ],
            )
        )
    else:
        return CardFactory.thumbnail_card(ThumbnailCard(title="Let's prepare question to send operator:/ Давайте продготовим вопрос для оператора",
        subtitle="Please write your question in first line and then add detales, or write"
                 "/skip to ask question that was writen before, or close question/ ""Напишите ваш вопрос ниже и добавьте коментарии в следующей строке."
                     " Если вы хотите отправить тот вопрос который был задан боту нажмите пропустить. Если вы хотите отменить вопрос, нажмите отменить вопрос",
        text="Push bottun or write question / Нажмите кнопку или введите вопрос",
        images=[
            CardImage(
                url="https://static.thenounproject.com/png/993506-200.png"
            )
        ],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Skip/Пропустить",
                value="/skip",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="Close question/Отменить вопрос",
                value="/cencel",
            ),
        ],
        )
)
async def function_SETTING(language:str,email:str)->Attachment:
    if language=="English":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Setting",
                subtitle="Your current paramenters:",
                text="<ul><li><strong>Language:</strong>        English</li><li><strong>Email</strong>       "+email+"</li></ul>",
                images=[
                    CardImage(
                        url="https://i.pinimg.com/originals/b8/cd/6d/b8cd6d45a84bd74c9d480a3b25309261.png"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="English",
                        value="English",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Русский",
                        value="Русский",
                    ),
                ],
            )
        )
    elif language=="Русский":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Настройки",
            subtitle="Ваши текущие настройки:",
            text="<ul><li><strong>Язык:</strong>        Русский</li><li>Эл. адрес       " + email + "</li></ul>",
            images=[
                CardImage(
                    url="https://i.pinimg.com/originals/b8/cd/6d/b8cd6d45a84bd74c9d480a3b25309261.png"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="English",
                    value="English",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Русский",
                    value="Русский",
                ),
            ],
            )
        )
    else:
        return CardFactory.thumbnail_card(ThumbnailCard(title="Setting/Настройки",
            subtitle="Your current paramenters:/ Ваши текущие настройки",
            text="<ul><li><strong>Language/Язык:</strong>        Bilingual/Двуязычный</li><li>Email/Эл.почта       " + email + "</li></ul>",
            images=[
                CardImage(
                    url="https://i.pinimg.com/originals/b8/cd/6d/b8cd6d45a84bd74c9d480a3b25309261.png"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="English",
                    value="English",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="Русский",
                    value="Русский",
                ),
            ],
            )
        )
async def function_ASK_QUESTION(language:str)->Attachment:
    if language=="English":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Ask your question!",
                subtitle=" All right. All settings are finished."
                                "Now, you can ask your first question or return to setting",
                images=[
                    CardImage(
                        url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Return to setting",
                        value="/setting",
                    ),
                ],
            )
        )
    elif language=="Русский":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Задайте свой вопрос!",
            subtitle=" Все настройки завершены,"
                                " сейчас вы можете задать свой вопрос или вернуться к настрйкам",
            text="",
            images=[
                CardImage(
                    url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Вернуться к настройкам",
                    value="/setting",
                ),
            ],
            )
        )
    else:
        return CardFactory.thumbnail_card(ThumbnailCard(title="Ask your question!/Задайте свой вопрос!",
            subtitle=" All right. All settings are finished."
                                "Now, you can ask your first question or return to setting/ Все настройки завершены,"
                     " сейчас вы можете задать свой вопрос или вернуться к настрйкам",
            text="You should return to setting to set language/Советуем вам вернуться к настройкам и установить язык",
            images=[
                CardImage(
                    url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Return to setting/Вернуться к настройкам",
                    value="/setting",
                ),
            ],
            )
        )
async def function_ASK_NEW_QUESTION(language:str)->Attachment:
    if language=="English":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Do you have any other question?",
                subtitle="You can ask your next question or change setting",
                images=[
                    CardImage(
                        url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Setting",
                        value="/setting",
                    ),
                ],
            )
        )
    elif language=="Русский":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Есть еще вопросы?",
            subtitle="Вы можете задать свой вопрос или изменить настрйки",
            text="",
            images=[
                CardImage(
                    url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Настройки",
                    value="/setting",
                ),
            ],
            )
        )
    else:
        return CardFactory.thumbnail_card(ThumbnailCard(title="Do you have any other question? / Есть еще вопросы?",
            subtitle="You can ask your next question or change setting / Вы можете задать свой вопрос или изменить настрйки",
            images=[
                CardImage(
                    url="https://healthinsuremarketplace.com/wp-content/uploads/2014/02/Fotolia_53938997_XS.jpg"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="Setting/Настройки",
                    value="/setting",
                ),
            ],
            )
)
async def function_BUILD_QUESTION(question:str,detales:str,language:str,email:str)->Attachment:
    if language=="English":
        return CardFactory.adaptive_card({
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0",
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Question for operator",
                    "weight": "bolder",
                    "isSubtle": False,
                },
                {"type": "TextBlock", "text": question, "weight": "bolder", "separator": True},
                {"type": "TextBlock", "text": detales, "spacing": "none"},
                {
                    "type": "TextBlock",
                    "text": "best regards \n mail  "+email,
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
    elif language=="Русский":
        return CardFactory.adaptive_card({
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0",
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Вопрос для отправки оператору",
                    "weight": "bolder",
                    "isSubtle": False,
                },
                {"type": "TextBlock", "text": question, "weight": "bolder", "separator": True},
                {"type": "TextBlock", "text": detales, "spacing": "none"},
                {
                    "type": "TextBlock",
                    "text": "С наилучшими пожеланиями, \n mail  " + email,
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
    else:
        return CardFactory.adaptive_card({
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0",
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Question for operator/Вопрос для отправки оператору",
                    "weight": "bolder",
                    "isSubtle": False,
                },
                {"type": "TextBlock", "text": question, "weight": "bolder", "separator": True},
                {"type": "TextBlock", "text": detales, "spacing": "none"},
                {
                    "type": "TextBlock",
                    "text": "best regards/С наилучшими пожеланиями, \n mail  " + email,
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
async def function_FEEDBACK(language:str)->Attachment:
    if language=="English":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Feedback",
                subtitle="Thank you for using QnAbot, we belive you have found your answer."
                         " To help us improve, we'd like to know your opinion.",
                text="Please give a mark to bot.",
                images=[
                    CardImage(
                        url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😁",
                        value="5",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="🙂",
                        value="4",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😐",
                        value="3",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😕",
                        value="2",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😡",
                        value="1",
                    ),
                ],
            )
        )
    elif language=="Русский":
        return CardFactory.thumbnail_card(ThumbnailCard(title="Обратная связь",
            subtitle="Спасибо вам за то, что пльзуетесь нашим ботом."
                     " Мы надеемся вы смогли получить ответ за свой вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота.",
            text="Поставьте оценку работе бота",
            images=[
                CardImage(
                    url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title="😁",
                    value="5",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="🙂",
                    value="4",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="😐",
                    value="3",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="😕",
                    value="2",
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title="😡",
                    value="1",
                ),
            ],
            )
        )
    else:
        return CardFactory.thumbnail_card(ThumbnailCard(title="Feedback/Обратная связь",
                subtitle="Thank you for using QnAbot, we belive you have found your answer."
                         " To help us improve, we'd like to know your opinion./  Спасибо вам за то, что пльзуетесь нашим ботом."
                     " Мы надеемся вы смогли получить ответ за свой вопрос. Пожалуйста помогите нам стать лучше и оцените работу бота.",
                text="Please give a mark to bot. / Поставьте оценку работе бота",
                images=[
                    CardImage(
                        url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                    )
                ],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😁",
                        value="5",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="🙂",
                        value="4",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😐",
                        value="3",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😕",
                        value="2",
                    ),
                    CardAction(
                        type=ActionTypes.im_back,
                        title="😡",
                        value="1",
                    ),
                ],
          )
        )

async def function_FEEDBACK1(language: str) -> Attachment:
        if language == "English":
            return CardFactory.thumbnail_card(ThumbnailCard(title="Feedback",
                        subtitle="Thank you for your mark. It is important for us."
                                 "Could you please write your opinion in next message.",
                        text="If you want to skip this step push skip button",
                        images=[
                            CardImage(
                                url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                            )
                        ],
                        buttons=[
                            CardAction(
                                type=ActionTypes.im_back,
                                title="Skip",
                                value="/skip",
                            ),
                        ],
                        )
          )
        elif language == "Русский":
            return CardFactory.thumbnail_card(ThumbnailCard(title="Обратная связь",
                    subtitle="Спасибо вам за вашу оценку. Для нас очень важно знать ваше мнение и интересно читать ваши коментарии",
                    text="Напишите отзыв в следующем сообщении или нажмите кнопку пропустить",
                    images=[
                        CardImage(
                            url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                        )
                    ],
                    buttons=[
                        CardAction(
                            type=ActionTypes.im_back,
                            title="Пропустить",
                            value="/skip",
                        ),

                    ],
                    )
      )
        else:
            return CardFactory.thumbnail_card(ThumbnailCard(title="Feedback /Обратная связь",
                    subtitle="Thank you for your mark. It is important for us."
                             "Could you please write your opinion in next message. / Спасибо вам за вашу оценку. Для нас очень важно знать ваше мнение и интересно читать ваши коментарии",
                    text="If you want to skip this step push skip button/ Напишите отзыв в следующем сообщении или нажмите кнопку пропустить",
                    images=[
                        CardImage(
                            url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnwpGT0WK4U9VTQLnGRJ8GSR2i7LhUVOYmgdpRkfQ3Q-N8os9X&usqp=CAU"
                        )
                    ],
                    buttons=[
                        CardAction(
                            type=ActionTypes.im_back,
                            title="Skip/Пропустить",
                            value="/skip",
                        ),
                    ],
                    )
      )
async def function_HELP (language:str,state:str=None)->Attachment:
        if language=="English":
            return CardFactory.adaptive_card({
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0",
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "extraLarge",
            "text": "Help message",
            "weight": "bolder",
            "isSubtle": False,
        },
        {"type": "TextBlock", "text": "Hello and welcome to our bot. This bot can give answer for your question."
                                      "Bot able to give answer for some problems in automatic mode and send other questions to Operators.", "separator": True},
        {"type": "TextBlock", "text": "Bot was created by ---/---", "spacing": "none"},
        {
            "type": "ColumnSet",
            "separator": True,
            "columns": [
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "TextBlock",
                            "weight":"bolder",
                            "text": "List of Comamnd",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "/start",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/setting",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/setting",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/tickets",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/skip",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/cancel",
                            "spacing": "none",
                        },
                    ],
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "TextBlock",
                            "weight": "bolder",
                            "text": "List of Comamnd",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "Start conversation with user",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "Show list of all setting. You can change langauge here. This command available"
                                    " after initialisation and when you finish to write question",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/setting",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "Write this comand to see all ticktes opend and closed",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "When you create question for operator or feedback, you can skip some steps",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "Type this command to close question",
                            "spacing": "none",
                        },
                    ],
                },
            ],
        },
    ],
})
        elif language=="Русский":
            return CardFactory.adaptive_card()
        else:
            return CardFactory.adaptive_card({
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0",
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "extraLarge",
            "text": "Help message",
            "weight": "bolder",
            "isSubtle": False,
        },
        {"type": "TextBlock","wrap": True, "text": "Hello and welcome to our bot. This bot can give answer for your question."
                                      "Bot able to give answer for some problems in automatic mode and send other questions to Operators.", "separator": True},
        {"type": "TextBlock", "text": "Bot was created by ---/---", "spacing": "none"},
        {
            "type": "ColumnSet",
            "separator": True,
            "minHeight":5,
            "columns": [
                {
                    "type": "Column",
                    "width": 5,
                    "minHeight": 5,
                    "items": [
                        {
                            "type": "TextBlock",
                            "weight":"bolder",
                            "text": "List of Comamnd",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "/start",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/setting",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/tickets",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/skip",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "/cancel",
                            "spacing": "none",
                        },
                    ],
                },
                {
                    "type": "Column",
                    "width": 12,
                    "minHeight":10,
                    "items": [
                        {
                            "type": "TextBlock",
                            "weight": "bolder",
                            "text": "Description",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "Start conversation with user",
                            "wrap":True,
                            "spacing": "none",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "Show list of all setting. You can change langauge here. This command available"
                                    " after initialisation and when you finish to write question",
                            "spacing": "none",
                            "isSubtle": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "Write this comand to see all ticktes opend and closed",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "When you create question for operator or feedback, you can skip some steps",
                            "spacing": "none",
                        },
                        {
                            "type": "TextBlock",
                            "text": "Type this command to close question",
                            "spacing": "none",
                        },
                    ],
                },
            ],
        },
    ],
})