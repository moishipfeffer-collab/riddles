from riddle_repsitory import RiddleRepository
from riddle import *
from player import Player
from riddle_game import RiddleGame
import questionary 
def run_menu():
    repository=RiddleRepository("riddles.json")
    print("\nwelcome to the riddle game!")
    while True:
        given_choose=questionary.select("choose an option:",choices=["play game","manage riddles","view leadership","exit"]).ask()

        if given_choose == "play game":
            play_game(repository)
        elif given_choose == "manage riddles":
            manage_riddles(repository)
        elif given_choose == "view leadership":
            pass
        elif given_choose == "exit":
            break
        else:
            print("invalid chois")
def manage_riddles(repository):
    while True:
        given_choose=questionary.select("nchoose an option:",["add riddle","show all riddles","update riddle","delete riddle","return"]).ask()
        if given_choose=="add riddle":
            add_riddle_menu(repository)
        elif given_choose == "show all riddles":
            show_riddles(repository)
        elif given_choose == "update riddle":
            update_riddle_menu(repository)
        elif given_choose == "delete riddle":
            delete_riddle_menu(repository)
        elif given_choose == "return":
            break
    
def add_riddle_menu(repository):
    riddle_id = int(input("Enter riddle id: "))
    question = input("Enter question: ")
    correct_answer = input("Enter correct answer: ")
    difficulty = input("Enter difficulty: ")
    category = input("Enter category: ")
    riddle_type = input("Enter type (open / multiple_2 / multiple_4): ")
    if riddle_type == "open":
        riddle = OpenRiddle(riddle_id,question,correct_answer,difficulty,category)
    elif riddle_type == "multiple_2":
        answers = []
        for i in range(2):
            answer = input(f"Enter answer {i + 1}: ")
            answers.append(answer)
        riddle = TwoAnswerRiddle(riddle_id,question,correct_answer,difficulty,category,answers)
    elif riddle_type == "multiple_4":
        answers = []
        for i in range(4):
            answer = input(f"Enter answer {i + 1}: ")
            answers.append(answer)
        riddle = FourAnswerRiddle(riddle_id,question,correct_answer,difficulty,category,answers)
    else:
        print("Invalid riddle type")
        return
    repository.add_riddle(riddle)

def show_riddles(repository):
    riddles = repository.get_all_riddles()
    if len(riddles) == 0:
        print("No riddles found")
        return
    for riddle in riddles:
        print(f"ID: {riddle.get_id()}")
        riddle.display()
        print()

def update_riddle_menu(repository):
    riddle_id = int(input("Enter riddle id to update: "))
    riddle = repository.get_riddle_by_id(riddle_id)
    if riddle is None:
        print("Riddle not found")
        return
    print("Current riddle:")
    print(riddle.to_dict())
    new_data = {}
    new_question = input("Enter new question or press Enter to keep current: ")
    if new_question != "":
        new_data["question"] = new_question
    new_answer = input("Enter new correct answer or press Enter to keep current: ")
    if new_answer != "":
        new_data["correct_answer"] = new_answer
    new_difficulty = input("Enter new difficulty or press Enter to keep current: ")
    if new_difficulty != "":
        new_data["difficulty"] = new_difficulty
    new_category = input("Enter new category or press Enter to keep current: ")
    if new_category != "":
        new_data["category"] = new_category
    success = repository.update_riddle(riddle_id, new_data)
    if success:
        print("Riddle updated successfully")
    else:
        print("Riddle not found")

def delete_riddle_menu(repository):
    riddle_id = int(input("Enter riddle id to delete: "))
    riddle = repository.get_riddle_by_id(riddle_id)
    if riddle is None:
        print("Riddle not found")
        return
    print("Riddle to delete:")
    print(riddle.to_dict())
    confirm = input("Are you sure you want to delete this riddle? yes/no: ")
    if confirm.lower() != "yes":
        print("Delete cancelled")
        return
    success = repository.delete_riddle(riddle_id)
    if success:
        print("Riddle deleted successfully")
    else:
        print("Riddle not found")    

def play_game(repository):
    username = input("\nEnter your username: ")
    print(f"\nhello {username}!\nlet's start the game!")
    player = Player(username)
    riddles = repository.get_all_riddles()
    if len(riddles) == 0:
        print("No riddles available")
        return
    game = RiddleGame(player, riddles, [])
    result = game.start()
    game.print_summary(result)