from django.http import HttpResponse
from django.template.response import TemplateResponse
from dataclasses import dataclass


@dataclass
class Card:
    img: str
    title: str
    text: str
    answers: int
    tags: list
    likes: int

    def __init__(self, img, title, text, answers, tags, likes):
        self.img = img
        self.title = title
        self.text = text
        self.answers = answers
        self.tags = tags
        self.likes = likes


members = {'Aboba': 100, 'ChargeZealot': 90, 'ZerG': 50}
tags = [(f'tag_{i}', 'tag') for i in range(1, 11)]


def paginate(obj, req, per_page = 10):
    pass


def index(req):
    cards = [
        Card('../static/img/placeholder-pic.png', 'SomeName 1',
             'Lorem Ipsum', 1, ['tag_1', 'tag_2'], 15),
        Card('../static/img/placeholder-pic.png', 'SomeName 2',
             'Lorem Ipsum', 0, ['tag_1', 'tag_2'], 10),
        Card('../static/img/placeholder-pic.png', 'SomeName 3',
             'Lorem Ipsum', 1, ['tag_1', 'tag_2'], -6),
        Card('../static/img/placeholder-pic.png', 'SomeName 4',
             'Lorem Ipsum', 0, ['tag_1', 'tag_2'], 3),
    ]
    return TemplateResponse(req, 'index.html', context={'username': 'Aboba',
                                                        'userpic': '../static/img/profile-pic.png',
                                                        'members': members, 'tags': tags, 'cards': cards})


def login(req):
    return TemplateResponse(req, 'login.html', context={'members': members, 'tags': tags})


def signup(req):
    return TemplateResponse(req, 'signup.html', context={'members': members, 'tags': tags})


def settings(req):
    return TemplateResponse(req, 'settings.html', context={'members': members, 'tags': tags})


def tag(req):
    return TemplateResponse(req, 'tag.html', context={'members': members, 'tags': tags})


def hot(req):
    return HttpResponse("In progress")


def question(req):
    return TemplateResponse(req, 'question.html', context={'members': members, 'tags': tags})


def ask(req):
    return TemplateResponse(req, 'ask.html', context={'members': members, 'tags': tags})
