from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(req):
    members = {'Aboba': 100, 'ChargeZealot': 90, 'ZerG': 50}
    tags = {'tag 1': 'tag', 'tag 2': 'tag', 'tag 3': 'tag', 'tag 4': 'tag', 'tag 5': 'tag', 'tag 6': 'tag',
            'tag 7': 'tag', 'tag 8': 'tag', 'tag 9': 'tag', 'tag 10': 'tag'}
    cards = [
        ['../static/img/placeholder-pic.png', 'SomeName 1', 'Lorem Ipsum', '0', ['tag_1', 'tag_2'], 15],
        ['../static/img/placeholder-pic.png', 'SomeName 2', 'Lorem Ipsum', '1', ['tag_1', 'tag_2'], 9],
        ['../static/img/placeholder-pic.png', 'SomeName 3', 'Lorem Ipsum', '0', ['tag_1', 'tag_2'], 0]
    ]
    return TemplateResponse(req, 'index.html', context={'username': 'Aboba',
                                                        'userpic': '../static/img/profile-pic.png',
                                                        'members': members, 'tags': tags, 'cards': cards})


def login(req):
    return TemplateResponse(req, 'login.html')


def signup(req):
    return TemplateResponse(req, 'signup.html')


def settings(req):
    return TemplateResponse(req, 'settings.html')


def tag(req):
    return TemplateResponse(req, 'tag.html')


def hot(req):
    return HttpResponse("In progress")
