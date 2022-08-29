from enum import Enum


class QuestionType(Enum):
    MULTIPLE_CHOICE = 1
    OPEN_ENDED = 2


class Question:
    id: int = 0
    type: QuestionType
    message: str

    def __init__(self, _id: int, _type: QuestionType, _message: str):
        self.id = _id
        self.type = _type
        self.message = _message
