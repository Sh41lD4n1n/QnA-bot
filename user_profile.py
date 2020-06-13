from datetime import datetime
class UserProfile:
    def __init__(self,email:str=None,l:str="b",question:str=None,feedback:str=None,mark:str=None):
        self.user_id = None
        self.email = email
        self.language = l
        self.question= question
        self.mark=mark
        self.opened_ticket=list()
        self.number_of_question=0
    def add_question(self,question:str,date_of_creation:str, detail:str=""):
        self.number_of_question+=1
        self.opened_ticket.append(Ticket(question,date_of_creation,self.user_id+"-"+str(self.number_of_question), detail))
    def create_id(self):
        self.user_id=self.email[0]+str(int(datetime.timestamp(datetime(2018,1,1)) % 1009))

class Ticket:
    def __init__(self,question:str,date_of_creation:str,number:str, detail:str=""):
        self.question=question
        self.date_of_creation=date_of_creation
        self.number=number
        self.detail=detail