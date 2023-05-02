from django.http import HttpResponse
from django.template import loader


def index(request, url=None):

    template = loader.get_template('menu/index.html')
    context = {
        'latest_question_list': "",
    }
    return HttpResponse(template.render(context, request))