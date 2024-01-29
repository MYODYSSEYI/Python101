import os 
import random

# Data management
data_dict_1 = {
    "difficulty": {
        "new": {},
        "hard": {},
        "mid": {},
        "ez": {},
    },
}


data_dict_2 = data_dict_1


# # Create a dictionary to update the data_dict
# updated_data_dict = {
#     "difficulty": {
#         "new": {}, # "new": {question:[answer, right/wrong_count]}
#         "hard": {},
#         "mid": {},
#         "ez": {},
#     },
# }

quesion_count = {
    # "question": 0 => inititial value | 1 => if right - put it in mid | -1 => if wrong - put it in hard
    "new": 0,
    # "question": 0 => inititial value | += 1 => if right 3 times - put it in mid | -= 1 => if wrong and num != 0 
    "hard": 0,
    # "question": 0 => inititial value | += 1 => if right 3 times - put it in ez | -= 1 => if wrong and num != 0
    "mid": 0,
    # all learned questions come in here. 
    "ez": 0,
}

fill_dictionary("test.txt")


def new_count():
    new_questions = Null
    for key in updated_data_dict["new"]:
        new_questions += 1
    return new_questions


def hard_count():
    hard_questions = Null
    for key in updated_data_dict["hard"]:
        hard_questions += 1
    return hard_questions


def mid_count():
    mid_questions = Null
    for key in updated_data_dict["mid"]:
        mid_questions += 1
    return mid_questions


def ez_count():
    ez_questions = Null
    for key in updated_data_dict["ez"]:
        ez_questions += 1
    return ez_questions


def write_data_dict_to_file(selected_file):
    file_path = os.path.join(os.path.dirname(__file__), "CardPacks", selected_file)
    with open(file_path, "w") as f:
        for difficulty, questions, count in data_dict_1["difficulty"].items():
            for question, answer in questions.items():
                f.write(f"{difficulty}:{question}:{answer}:{count}\n")
                
def fill_dictionary(file):
    file_path = os.path.join(os.path.dirname(__file__), "CardPacks", file)
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            difficulty, question, answer, count = line.strip().split(":")
            data_dict_1["difficulty"][difficulty][question] = [answer, count]

next_question_data_dict()


def random_question(which):
    # Get a random question from the dictionary
    question = random.choice(list(which.keys()))
    return question

    
# def del_from_data_dict(question):
#     del question
    

def next_question_data_dict_1():
    question = Null
    if data_dict_1["difficulty"]["new"] != {}:
        question = random_question(data_dict_1["difficulty"]["new"])
        right_wrong_dict_1(question)
    elif data_dict_1["difficulty"]["hard"] != {}:
        question = random_question(data_dict_1["difficulty"]["hard"])
        return question
    elif data_dict_1["difficulty"]["mid"] != {}:
        question = random_question(data_dict_1["difficulty"]["mid"])
        return question
    else:
        quit()


# def next_question_data_dict_2():
#     question = Null
#     if data_dict_2["difficulty"]["new"] != {}:
#         question = random_question(data_dict_2["difficulty"]["new"])
#         right_wrong_dict_2(question)
#     elif data_dict_2["difficulty"]["hard"] != {}:
#         question = random_question(data_dict_2["difficulty"]["hard"])
#         return question
#     elif data_dict_2["difficulty"]["mid"] != {}:
#         question = random_question(data_dict_2["difficulty"]["mid"])
#         return question
#     else:
#         quit()


def right_wrong_dict_1(question):
    choice = input("right or wrong?")
    if choice == "right" and question in data_dict_1["difficulty"]["new"]:
        del data_dict_2["difficulty"]["new"][question]
        data_dict_2["difficulty"]["mid"][question]=[answer, 0]
        data_dict_1.update(data_dict_2)
    elif choice == "wrong" and question in data_dict_1["difficulty"]["new"]:
        del data_dict_2["difficulty"]["new"][question]
        data_dict_2["difficulty"]["hard"][question]=[answer, 0]
        data_dict_1.update(data_dict_2)
    elif choice == "right" and question in data_dict_1["difficulty"]["hard"]:
        if data_dict_1["difficulty"]["hard"][1] >= 0 and data_dict_1["difficulty"]["hard"][1] < 3:
            data_dict_1["difficulty"]["hard"][1] += 1
        elif data_dict_1["difficulty"]["hard"][1] == 3:
            del data_dict_2["difficulty"]["hard"][question]
            data_dict_2["difficulty"]["mid"][question]=[answer, 0]
            data_dict_1.update(data_dict_2)
        elif data_dict_1["difficulty"]["hard"][1] >= 0 and data_dict_1["difficulty"]["hard"][1] < 3:
            data_dict_1["difficulty"]["hard"][1] -= 1
        else:
            print("ERROR")
