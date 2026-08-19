class QuestionResult:
    def __init__(self,riddle_id: int,riddle_type: str,category:str,time_taken:float):
        self.__riddle_id=riddle_id
        self.__riddle_type=riddle_type
        self.__category=category
        self.__time_taken=time_taken
    def get_riddle_id(self):
        return self.__riddle_id
    def get_type(self):
        return self.__riddle_type
    def get_time(self):
        return self.__time_taken
    def get_category(self):
        return self.__category
class GameResult:
    def __init__(self,username:str,date:str,total_time:float,question_results:list[QuestionResult]):
        self.__username=username
        self.__date=date
        self.__total_time=total_time
        self.__question_results=question_results
    def get_total_riddles(self):
        return len(self.__question_results)
    def average_time_by_type(self):
        average={}
        for question in self.__question_results:
            question_type=question.get_type()
            if question_type not in average:
                average[question_type]=[]
            average[question_type].append(question.get_time())
        for type,time in average.items():
            average[type]=sum(time)/len(time)
        return average
    def average_time_by_category(self):
        average={}
        for question in self.__question_results:
            question_category=question.get_category()
            if question_category not in average:
                average[question_category]=[]
            average[question_category].append(question.get_time())
        for category,time in average.items():
            average[category]=sum(time)/len(time)
        return average
    def to_csv_row(self):
        total=self.get_total_riddles()
        if total>0:
            return [self.__username,self.__date,self.__total_time,self.get_total_riddles(),self.__total_time/self.get_total_riddles()]
    def get_username(self):
        return self.__username
    def get_time(self):
        return self.__total_time
