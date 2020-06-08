from botbuilder.core import CardFactory
from botbuilder.schema import CardImage, CardAction, ActionTypes, ThumbnailCard, Attachment, ReceiptItem, Fact, \
    ReceiptCard

#await turn_context.send_activity(MessageFactory.attachment(await messages.function_SETTING(userProfile.language,userProfile.email)))
DID_THAT_HELP = CardFactory.thumbnail_card(ThumbnailCard(title="Did that help?",
            subtitle="",
            text="Click yes, if your question are solved, and no otherwise",
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
                )
            ],
        )
    )
DID_THAT_HELP_rus = CardFactory.thumbnail_card(ThumbnailCard(title="Вам помог наш ответ?",
            subtitle="",
            text="Отправьте да, если вопрос решён, или нет, если вам нужен другой ответ",
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
                )
            ],
        )
    )
DID_THAT_HELP_b = CardFactory.thumbnail_card(ThumbnailCard(title="Did that help?/Вам помог наш ответ?",
            subtitle="",
            text="Click yes, if your question are solved, and no otherwise/Отправьте да, если вопрос решён, или нет, если вам нужен другой ответ",
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
                )
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
'''    async def function_HELP (language:str,email:str,state:str)->Attachment:
        if language=="English":
            return CardFactory.thumbnail_card(ThumbnailCard(title="Help",
                    subtitle="Hello. This bot can give answer for your question. You can use following comand:",
                    text="<ul><li><strong>Language:</strong>        English</li><li>Email       "+email+"</li></ul>",
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
            )'''