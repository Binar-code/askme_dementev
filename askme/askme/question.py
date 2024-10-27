from dataclasses import dataclass


@dataclass
class Question:
    img: str
    title: str
    text: str
    tags: list
    likes: int

    def __init__(self, img, title, text, tags, likes):
        self.img = img
        self.title = title
        self.text = text
        self.tags = tags
        self.likes = likes


@dataclass
class Card(Question):
    answers: int

    def __init__(self, img, title, text, tags, likes, answers):
        super(Card, self).__init__(img, title, text, tags, likes)
        self.answers = answers


@dataclass
class Answer(Question):
    correct: bool

    def __init__(self, img, title, text, tags, likes, correct):
        super(Answer, self).__init__(img, title, text, tags, likes)
        self.correct = correct
