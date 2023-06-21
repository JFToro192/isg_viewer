from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("geoids/index.html")
    context = {
        'sample_text': 'ISG WebGIS'
    }
    return HttpResponse(template.render(context, request))