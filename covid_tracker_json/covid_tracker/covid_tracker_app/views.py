from django.shortcuts import render
from django.http import HttpResponse

from covid_tracker_app.lib.degrees import trace
from covid_tracker_app.facts import random_facts
from covid_tracker_app.scraper import get_stats

# Create your views here.
def index(request):
    stats = get_stats()
    context = {
    'facts': random_facts(),
    'stats': stats,
    }
    
    if request.method == 'POST':
        source = request.POST['source']
        target = request.POST['target']
        if not target:
            target = 'Tom Hanks'

        path = trace(source, target)

        if type(path) == list:
            context['multiple'] = path
        else: 
            context['path'] = path


        return render(request, 'covid_tracker_app/index.html', context)
    return render(request, 'covid_tracker_app/index.html', context)


