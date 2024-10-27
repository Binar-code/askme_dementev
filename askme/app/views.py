from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from askme.question import Card, Question, Answer


members = {'Aboba': 100, 'ChargeZealot': 90, 'ZerG': 50}
tags = [(f'tag_{i}', 'tag') for i in range(1, 11)]
username = 'Aboba'
userpic = 'img/profile-pic.png'


def paginate(obj_list, req, per_page=4):
    paginator = Paginator(obj_list, per_page)
    page_number = req.GET.get('page', 1)

    try:
        return paginator.get_page(page_number)
    except PageNotAnInteger:
        return paginator.get_page(1)
    except EmptyPage:
        return paginator.get_page(paginator.num_pages)


def index(req):
    cards = [
        Card('img/placeholder-pic.png', f'SomeTitle {i + 1}',
             'Lorem Ipsum', ['tag_1', 'tag_2'], 15, 1)
        for i in range(11)
    ]

    paginated_cards = paginate(cards, req, 4)

    return TemplateResponse(req, 'index.html', context={'username': username,
                                                        'userpic': userpic, 'members': members, 'tags': tags,
                                                        'cards': paginated_cards})


def login(req):
    return TemplateResponse(req, 'login.html', context={'members': members, 'tags': tags})


def signup(req):
    return TemplateResponse(req, 'signup.html', context={'members': members, 'tags': tags})


def settings(req):
    return TemplateResponse(req, 'settings.html', context={'members': members, 'tags': tags,
                                                           'userpic': userpic,
                                                           'username': username})


def tag(req):
    cards = [
        Card('img/placeholder-pic.png', f'SomeTitle {i + 1}',
             'Lorem Ipsum', ['some_tag', 'tag_2'], 15, 1)
        for i in range(7)
    ]

    paginated_cards = paginate(cards, req, 4)

    return TemplateResponse(req, 'tag.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic, 'username': username,
                                                      'cards': paginated_cards})


def hot(req):
    cards = [
        Card('img/placeholder-pic.png', f'SomeTitle {i + 1}',
             'Lorem Ipsum', ['tag_1', 'tag_2'], 999, 999)
        for i in range(10)
    ]
    paginated_cards = paginate(cards, req, 4)
    return TemplateResponse(req, 'hot.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic,
                                                      'username': username,
                                                      'cards': paginated_cards})


def question(req):
    main_question = Question('img/placeholder-pic.png', f'SomeTitle',
             'Lorem Ipsum',  ['tag_1', 'tag_2'], 10)
    answers = [
        Answer('../static/img/placeholder-pic.png', f'SomeTitle {i + 1}',
             'Lorem Ipsum',  ['tag_1', 'tag_2'], 1, False)
        for i in range(10)
    ]

    answers[0].correct = True

    paginated_answers = paginate(answers, req, 3)

    return TemplateResponse(req, 'question.html', context={'members': members, 'tags': tags,
                                                           'userpic': userpic, 'username': username,
                                                           'answers': paginated_answers, 'question': main_question})


def ask(req):
    return TemplateResponse(req, 'ask.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic,
                                                      'username': username})
