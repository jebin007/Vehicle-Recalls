from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Recalls
from django.db.models import Q
# Create your views here.
def index(request):
    template = loader.get_template('vrecalls/index.html')
    query = request.GET.get("q")
    if query:
        listquery = query.split()
        if len(listquery) == 1:
            all_recalls = Recalls.objects.filter(
                Q(maketxt__contains=listquery[0]) |
                Q(modeltxt__contains=listquery[0]) |
                Q(yeartxt__contains=listquery[0])
            ).distinct()
        if len(listquery) == 2:
            all_recalls = Recalls.objects.filter(
                (Q(maketxt__contains=listquery[0]) | Q(maketxt__contains=listquery[1])) &
                (Q(modeltxt__contains=listquery[0]) | Q(modeltxt__contains=listquery[1])) |
                (Q(yeartxt__contains=listquery[0]) | Q(yeartxt__contains=listquery[1]))
            ).distinct()
        if len(listquery) == 3:
            all_recalls = Recalls.objects.filter(
                (Q(maketxt__contains=listquery[0]) | Q(maketxt__contains=listquery[1]) | Q(maketxt__contains=listquery[2])) &
                (Q(modeltxt__contains=listquery[0]) | Q(modeltxt__contains=listquery[1]) | Q(modeltxt__contains=listquery[2])) &
                (Q(yeartxt__contains=listquery[0]) | Q(yeartxt__contains=listquery[1])| Q(yeartxt__contains=listquery[2]))
            ).distinct()
        context = {
            'all_recalls': all_recalls,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render())
