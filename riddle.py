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
        return answer.lower().strip() == self.__correct_answer
    def get_type(self):
        raise NotImplementedError
    def get_question(self):
        return self.__question
    def get_id(self):
        return self.__riddle_id
    def get_category(self):
        return self.__category
    def get_correct_answer(self):
        return self.__correct_answer
     
    def to_dict(self):
        return {"id":self.__riddle_id,
                "question":self.__question,
                "correct_answer":self.__correct_answer,
                "type":self.get_type(),
                "possible_answers":[],
                "difficulty":self.__difficulty,
                "category":self.__category}
class MultipleChoiceRiddle(Riddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category,possible_answers: list[str]):
        super().__init__(riddle_id, question, correct_answer, difficulty, category)
        self.__possible_answers=possible_answers
    def display(self):
        print(f"\n{self.get_question()}")
        print(f"possible answers:")
        answers=self.get_possible_answers()
        for i in range(len(answers)):
            print(f"{i+1}.{answers[i]}")
    def check_answer(self, answer):
        if answer.isdigit() and 0<int(answer)<=len(self.__possible_answers):
            i=int(answer)-1
            answer=self.__possible_answers[i]
        elif answer != self.get_correct_answer() and answer>len(self.__possible_answers):
            print(f"enter num from 1 to {len(self.__possible_answers)} or the answer itself.")
        return super().check_answer(answer)
    def get_possible_answers(self):
        answers=self.__possible_answers.copy()
        return answers
    def to_dict(self):
        data=super().to_dict()
        data["possible_answers"]=self.get_possible_answers()
        return data
class FourAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        if len(possible_answers)!=4:
            raise ValueError("FourAnswerRiddle must contain exactly four possible answers")
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)
    def get_type(self):
        return "multiple_4"
class TwoAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        if len(possible_answers)!=2:
            raise ValueError("TwoAnswerRiddle must contain exactly two possible answers")
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)  
    def get_type(self):
        return "multiple_2"   
class OpenRiddle(Riddle):
    def display(self):
        print (f"\n{self.get_question()}")
    def get_type(self):
        return "open"
    
    
