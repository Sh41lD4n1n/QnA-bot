class UserProfile:
    def __init__(self,email:str=None,l:str="b",question:str=None,feedback:str=None,mark:str=None):
        self.email = email
        self.language = l
        self.question= question
        self.mark=mark
