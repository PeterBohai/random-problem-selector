import random
import json


class Style:
    RESET = "\033[0m"
    RED = "\033[31m"
    BLUE_D = "\033[34m"
    BLUE_L = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[33m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"


# formatting
kyu_string = Style.BOLD + "kyu" + Style.RESET

# load question bank
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    question_bank = data["question_bank"]
    seen_bank = data["seen_bank"]

print()
command = input("Hi, would you like to SELECT(s) or ADD(a) a question or RESET(r)?  ")

with open("data_file.json", "w") as write_file:

    if command.strip() == "a" or command.strip() == "ADD":

        adding = True
        while adding:
            question_title = input("What's the question title?  ")
            kyu = input(f"Awesome! Now what's the {kyu_string} of this question?  ")
            question_bank[kyu].append(question_title.strip())
            adding = input("Do you want to add another question (y/n)?  ") == "y"
            if adding:
                print("---------------------------------------")

    elif command.strip() == "s" or command.strip() == "SELECT":

        kyu_options = input(f"Please indicate {kyu_string} level (optional - add a space + how many Qs):  ")
        kyu_split = kyu_options.split()

        kyu = kyu_split[0]
        num_questions = 1 if len(kyu_split) == 1 else kyu_split[1]

        for _ in range(int(num_questions)):
            if question_bank[kyu]:
                selected_question = random.choice(question_bank[kyu])
                seen_bank[kyu].append(selected_question)
                question_bank[kyu].remove(selected_question)
                print(f"Try {Style.GREEN + selected_question + Style.RESET }\033[0m")

            else:   # No more questions left in the questions list. Repopulate with all the seen questions.
                question_bank[kyu] = seen_bank[kyu][:]
                seen_bank[kyu].clear()
                print("Already seen all questions. Please restart to loop through again.")
                break

    elif command.strip() == "r" or command.strip() == "RESET":

        kyu = input(f"Please indicate which {kyu_string} questions to reset:  ")
        question_bank[kyu].extend(seen_bank[kyu])
        seen_bank[kyu].clear()
        print(f"Successfully restarted kyu {kyu} questions.")

    print()
    json.dump(data, write_file)
