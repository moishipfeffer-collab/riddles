class Player:
    def __init__(self,username:str):
        self.__username=username
    def get_username(self):
        return self.__username
    def rename(self,new_username: str):
        if len(new_username.strip())>=2:
            self.__username=new_username
        else:
            raise NameError("name must be a string with min 2 letters")
