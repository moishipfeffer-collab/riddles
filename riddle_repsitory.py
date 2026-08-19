import json
from riddle import *
class RiddleRepository:
    def __init__(self, file_path:str):
        self.__file_path=file_path
    def load_riddles(self):
        with open(self.__file_path,"r") as file:
            data=json.load(file)
        riddles=[]
        for item in data:
            if item["type"]=="open":
                riddle=OpenRiddle(item["id"],item["question"],item["correct_answer"],item["difficulty"],item["category"])
            elif item["type"]=="multiple_4":
                riddle=FourAnswerRiddle(item["id"],item["question"],item["correct_answer"],item["difficulty"],item["category"],item["possible_answers"])
            elif item["type"]=="multiple_2":
                riddle=TwoAnswerRiddle(item["id"],item["question"],item["correct_answer"],item["difficulty"],item["category"],item["possible_answers"])
            riddles.append(riddle)
        return riddles
    def save_riddles(self,riddles: list[Riddle]):
        data=[]
        for riddle in riddles:
            data.append(riddle.to_dict())
        with open(self.__file_path,"w") as file:
            json.dump(data,file,indent=4)
    def get_all_riddles(self):
        return self.load_riddles()
    def get_riddle_by_id(self,riddle_id:int):
        riddles=self.load_riddles()
        for riddle in riddles:
            if riddle_id==riddle.get_id():
                return riddle
        return None
    def add_riddle(self,riddle:Riddle):
        riddles=self.load_riddles()
        for existing_riddle in riddles:
            if existing_riddle.get_id()==riddle.get_id():
                raise ValueError("riddle id already exists")
        riddles.append(riddle)
        self.save_riddles(riddles)
    def update_riddle(self,riddle_id: int,new_data: dict):
        riddles=self.load_riddles()
        for i in range(len(riddles)):
            riddle=riddles[i]
            if riddle.get_id()==riddle_id:
                riddle_dict=riddle.to_dict()
                for key in new_data:
                    riddle_dict[key]=new_data[key]
                if riddle_dict["type"]=="open":
                    updated_riddle=OpenRiddle(riddle_dict["id"],riddle_dict["question"],riddle_dict["correct_answer"],riddle_dict["difficulty"],riddle_dict["category"],riddle_dict["possible_answers"])
                elif riddle_dict["type"]=="multiple_4":
                    updated_riddle=FourAnswerRiddle(riddle_dict["id"],riddle_dict["question"],riddle_dict["correct_answer"],riddle_dict["difficulty"],riddle_dict["category"],riddle_dict["possible_answers"])
                elif riddle_dict["type"]=="multiple_2":
                    updated_riddle=TwoAnswerRiddle(riddle_dict["id"],riddle_dict["question"],riddle_dict["correct_answer"],riddle_dict["difficulty"],riddle_dict["category"],riddle_dict["possible_answers"])
                riddles[i]=updated_riddle
                self.save_riddles(riddles)
                return True
        return False
    def delete_riddle(self,riddle_id:int):
        riddles=self.load_riddles()
        for i in range(len(riddles)):
            riddle=riddles[i]
            if riddle.get_id()==riddle_id:
                riddles.pop(i)
                self.save_riddles(riddles)
                return True
        return False
