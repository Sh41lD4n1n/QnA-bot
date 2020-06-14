# QnA-bot

 	1.Install the necessary packages by running the following commands:
		pip install botbuilder-core
		pip install asyncio
		pip install aiohttp
		pip install cookiecutter
 	2.In repository you can find requirements.txt
		Run pip install -r requirements.txt
 	3.Run python app.py 
 	4.Start the Emulator and click the Open Bot button.
 	5. Enter bot url is http://localhost:3978/api/messages
 	6.Click the Connect button and your bot should start.
 
#Conversation with bot 

  	To start conversation enter "/start" command or "/help" to open help message
  	Now you should choose language(if skip this step, bot will write message in two languages)
  	Write email adress in next message (Bot require email adress ends with "innopolis.ru" or "innopolis.university")
  	Now you can write question, type "/setting"(to change language) or type /tickets(to see all opened tickets)
  	If you write question, bot will send answer from data base and then create ticket for operator
      
