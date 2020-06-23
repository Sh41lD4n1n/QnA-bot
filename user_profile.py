from datetime import datetime
from tickets import PTicket


class UserProfile:
    def __init__(self, email: str = None, l: str = "b", question: str = None, feedback: str = None, mark: str = None):
        self.user_id = None
        self.email = email
        self.language = l
        self.question = question
        self.mark = mark
        self.opened_ticket = list()
        self.number_of_question = 0

    def add_question(self, details: str = "") -> str:
        # get date of creation
        date = datetime.now().timetuple()
        # format of date is following month/day/year
        date_of_creation = str(date[1]) + "/" + str(date[2]) + "/" + str(date[0])

        # generate ticket id andcreate ticket
        self.number_of_question += 1
        ticket_id = self.user_id + "-" + str(self.number_of_question)
        ticket = PTicket(title=self.question,
                         time_opened=date_of_creation,
                         ticket_id=ticket_id,
                         email=self.email,
                         details=details)
        ticket.send()
        self.opened_ticket.append(ticket)
        print('opened: ', self.opened_ticket)
        return ticket_id

    def create_user_id(self,id:str):
        date = datetime.now()
        self.user_id = id
        print(self.user_id)
