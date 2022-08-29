from models.question import Question, QuestionType

path: str = "C:\\Users\\Michael\\Desktop\\Documents\\Journal\\"

question_one = Question(0, QuestionType.OPEN_ENDED, "How I'm feeling today, so far:")
question_two = Question(1, QuestionType.MULTIPLE_CHOICE, "Some things that happened today:")
question_three = Question(2, QuestionType.MULTIPLE_CHOICE, "What I've completed today:")
question_four = Question(3, QuestionType.MULTIPLE_CHOICE, "Goals for tomorrow:")
question_five = Question(4, QuestionType.OPEN_ENDED, "How would I rate today on a scale of 1 - 10:")

questions = [
    question_one,
    question_two,
    question_three,
    question_four,
    question_five
]

exit_phrases = [
    "x_",
    "x_quit",
    "x_exit",
]

options: dict = {
    "m_path": path,
    "m_questions": questions
}


def set_path(_path: str):
    options.setdefault("m_path", _path)


def add_question(_question: str):
    _questions = options.get("m_questions")
    _questions.append(_question)
    options.setdefault("m_questions", questions)