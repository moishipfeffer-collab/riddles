import time,datetime
from riddle import *
from results import *
from player import *
class RiddleGame:
    def __init__(self,player: Player,riddles:list[Riddle],results:list[QuestionResult]):
        self.__player=player
        self.__riddles=riddles
        self.__results=results
    def start(self):
        start_time=time.time()
        self.__results=[]
        for riddle in self.__riddles:
            result=self.ask_riddle(riddle)
            self.__results.append(result)
        time_total=time.time()-start_time
        game_result=GameResult(self.__player.get_username(),str(datetime.date.today()),time_total,self.__results)
        return game_result
    def ask_riddle(self,riddle: Riddle):
        start_time=time.time()
        while True:
            riddle.display()
            answer=input("enter your answer: ")
            if riddle.check_answer(answer):
                break
            print("incorrect, please try again")
        took_time=time.time()-start_time
        result=QuestionResult(riddle.get_id(),riddle.get_type(),riddle.get_category(),took_time)
        return result
    def print_summary(self, result: GameResult):
        print(f"\nplayer: {result.get_username()}")
        print(f"total riddles: {result.get_total_riddles()}")
        print(f"total time: {result.get_time():.2f}")
        print(f"\navearage by type:")
        aveerage_type=result.average_time_by_type()
        for type,time in aveerage_type.items():
            print(f"{type}: {time:.2f} seconds")
        print(f"\navearage by category:")
        aveerage_category=result.average_time_by_category()
        for category,time in aveerage_category.items():
            print(f"{category}: {time:.2f} cecons")
    