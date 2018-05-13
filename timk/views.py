from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.template.loader import get_template
from django.utils import timezone
from django.http import HttpResponse, Http404
from .models import  Event, Sport, Team, Channel, Game, Venue
import datetime

# Create your views here.

class AllListView(generic.ListView):
    model = Game

    #queryset = Team.objects.order_by('name')
    #context_object_name = 'team_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()

        result_team = Team.objects.values('group').distinct().order_by('group')
        context['grl'] = result_team

        team_list = Team.objects.order_by('name')
        context['teaml'] = team_list

        result_date = Game.objects.values('date').distinct().order_by('date')
        context['datelist'] = result_date

        return context

class MatchListView(generic.ListView):
    model = Game
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        result_team = Team.objects.values('group').distinct().order_by('group')
        context['grl'] = result_team
        return context


class GroupDetailView(generic.ListView):
    model = Game
    template_name = 'timk/group-view.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        if self.kwargs['str']:
            group_str = self.kwargs['str']
        #teams_group = Team.filter(group=group_str)
        context['test'] = Game.objects.all().filter(team1__group__icontains=group_str).distinct()
        return context


class TeamListView(generic.ListView):
    model = Team
    queryset = Team.objects.order_by('name')
    context_object_name = 'team_list'
    
    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['grouplist'] = Team.objects.all().order_by('group')
    #    return context


class MatchDetailView(generic.DetailView):
    model = Game
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        return context
    

def index(request):
    return render(request, 'timk/index.html', {})

def detail(request, event):
    event = get_object_or_404(Event, name=event)
    return render(request, 'timk/details.html', {'event': event})

'''def detail(request, competition_id):
    display = "You're looking at competition %s."
    return HttpResponse(display % competition_id)'''

def team(request, team_id):
    return HttpResponse("teams list")

def events(request):
    return HttpResponse(render(request, 'base.html'))

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

def sports_list(request):
    #sports = Sport.objects
    #return render(request, 'sports.html', {'sports':sports})
    return render(request, 'sports.html')