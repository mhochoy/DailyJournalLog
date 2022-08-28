from enum import Enum


class QuestionType(Enum):
    MULTIPLE_CHOICE = 1
    OPEN_ENDED = 2


class Question:
    type: QuestionType
    message: str

    def __init__(self, _type: QuestionType, _message: str):
        self.type = _type
        self.message = _message
