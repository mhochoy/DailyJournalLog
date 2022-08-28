from models.question import Question, QuestionType

path = "C:\\Users\\Michael\\Desktop\\Documents\\Journal\\"

question_one = Question(QuestionType.OPEN_ENDED, "How I'm feeling today, so far:")
question_two = Question(QuestionType.MULTIPLE_CHOICE, "Some things that happened today:")
question_three = Question(QuestionType.MULTIPLE_CHOICE, "What I've completed today:")
question_four = Question(QuestionType.MULTIPLE_CHOICE, "Goals for tomorrow:")
question_five = Question(QuestionType.OPEN_ENDED, "How would I rate today on a scale of 1 - 10:")

questions = [
    question_one,
    question_two,
    question_three,
    question_four,
    question_five
]

exit_phrases = [
    "quit",
    "exit",
    "q",
    "e",
    "x",
    "done",
    ""
]
