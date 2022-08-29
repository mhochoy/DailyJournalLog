class QuitException(Exception):
    pass


class MenuException(Exception):
    answer: str
