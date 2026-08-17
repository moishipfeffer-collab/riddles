class Riddle:
    def __init__(self,riddle_id: int,question: str, correct_answer: str,
                 difficulty: str,category:str):
        self.__riddle_id=riddle_id
        self.__question=question
        self.__correct_answer=correct_answer
        self.__difficulty=difficulty
        self.__category=category
    def display(self):
        raise NotImplementedError
    def check_answer(self,answer:str):
        return answer == self.__correct_answer
    def get_type(self):
        raise NotImplementedError
     
    def to_dict(self):
        return {"id":self.__riddle_id,
                "qoestion":self.__question,
                "correct_answer":self.__correct_answer,
                "type":self.get_type(),
                "possible_answers":[],
                "difficulty":self.__difficulty,
                "category":self.__category}
class MulipleChoiceRiddle(Riddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category,possible_answers: list[str]):
        super().__init__(riddle_id, question, correct_answer, difficulty, category)
        self.__possible_answers=possible_answers
    def display(self):
        print(f"question:\n{self.__question}")
        print(f"possible answers:\n{self.__possible_answers}")
    def check_answer(self, answer:str):
        return answer == self.__correct_answer
    def get_possible_answers(self):
        answers=self.__possible_answers.copy()
        return answers
class FourAnswerRiddle(MulipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        if len(possible_answers)!=4:
            raise ValueError("FourAnswerRiddle must contain exactly four possible answers")
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)
    def get_type(self):
        return "multiple_4"
class TwoAnswerRiddle(MulipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        if len(possible_answers)!=2:
            raise ValueError("FourAnswerRiddle must contain exactly four possible answers")
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)  
    def get_type(self):
        return "multiple_2"   
class OpenRiddle(Riddle):
    def display(self):
        print (f"question: {self.__question}")
class Player:
    def __init__(self,username:str):
        self.__username=username
    def get_username(self):
        return self.__username
    def rename(self,new_username: str):
        if new_username.isalpha() and len(new_username.strip())>2:
            self.__username=new_username
        else:
            raise NameError("name must be a string with min 2 lietters")
class QuestionResult:
    def __init__(self,riddle_id: int,riddle_type: str,category:str,time_taken:float):
        self.__riddle_id=riddle_id
        self.__riddle_type=riddle_type
        self.__category=category
        self.__time_taken=time_taken
        