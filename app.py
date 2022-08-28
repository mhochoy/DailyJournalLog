from datetime import date
from datetime import datetime
from typing import TextIO
import pytz

from models.question import Question, QuestionType
import configuration


def main():
    try:
        run_application()

    except KeyboardInterrupt:
        print("Quitting...")
        pass


def run_application():
    current_day = date.today()
    timezone = pytz.timezone('America/New_York')
    now = datetime.now(timezone)
    current_time = now.strftime("%I:%M:%S")

    with open(f"{configuration.path}My Daily Journal {current_day}.txt", "w") as f:
        date_string = f"{current_day}\n{current_time}\n\n\n"
        f.write(date_string)
        print(date_string)
        for question in configuration.questions:
            process_question_to_answer(question, file=f)

        f.close()
        input("Daily Journal Log Finished. Press Enter to exit")



def process_question_to_answer(question: Question, file: TextIO):
    file.write(f"{question.message}\n")
    print(f"{question.message}\n\n")
    if question.type == QuestionType.OPEN_ENDED:
        answer = input()
        if not check_for_exit_phrase(answer):
            file.write(f"{answer}\n\n\n")
        else:
            return
    elif question.type == QuestionType.MULTIPLE_CHOICE:
        answers = get_multiple_choice_answers()
        for answer in answers:
            file.write(f"{answer}")
        file.write("\n\n\n")


def get_multiple_choice_answers():
    done = False
    answers = []
    while not done:
        answer = input()
        if check_for_exit_phrase(answer):
            done = True
        else:
            answer = f"- {answer}\n"
            answers.append(answer)

    return answers


def check_for_exit_phrase(answer: str):
    if answer in configuration.exit_phrases:
        return True
    return False


main()
