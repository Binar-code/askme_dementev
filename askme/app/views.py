from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse


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
    return TemplateResponse(req, 'tag.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic, 'username': username,
                                                      'cards': paginated_cards})


def hot(req):
    return TemplateResponse(req, 'hot.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic,
                                                      'username': username,
                                                      'cards': paginated_cards})


def question(req):
    return TemplateResponse(req, 'question.html', context={'members': members, 'tags': tags,
                                                           'userpic': userpic, 'username': username,
                                                           'cards': paginated_answers, 'question': main_question})


def ask(req):
    return TemplateResponse(req, 'ask.html', context={'members': members, 'tags': tags,
                                                      'userpic': userpic,
                                                      'username': username})
