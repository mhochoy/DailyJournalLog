from datetime import date
from datetime import datetime
from typing import TextIO
import pytz

from models.question import Question, QuestionType
import configuration
import exceptions


def main():
    try:
        run_application()

    except KeyboardInterrupt:
        print("Quitting...")
        pass

    except exceptions.QuitException:
        print("Quitting...")
        quit()

    except exceptions.MenuException as menu_exception:
        if menu_exception.answer == "m_path":
            path = input("Enter new path: ")
            configuration.set_path(path)

        main()


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
    print(f"{question.id}. {question.message}\n\n")
    if question.type == QuestionType.OPEN_ENDED:
        answer = input()
        try:
            if check_for_key_phrase(answer):
                return
            elif not check_for_key_phrase(answer):
                file.write(f"{answer}\n\n\n")
        except exceptions.QuitException:
            raise exceptions.QuitException

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
        try:
            if check_for_key_phrase(answer):
                done = True
            elif not check_for_key_phrase(answer):
                answer = f"- {answer}\n"
                answers.append(answer)
        except exceptions.QuitException:
            raise exceptions.QuitException

    return answers


def check_for_key_phrase(answer: str):
    if answer == "":
        return True
    elif answer in configuration.exit_phrases:
        raise exceptions.QuitException
    elif answer in configuration.options.keys():
        menu_exception = exceptions.MenuException()
        menu_exception.answer = answer
        raise menu_exception

    else:
        return False


main()
