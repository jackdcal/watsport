"""timk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import AllListView,MatchListView, MatchDetailView, GroupDetailView, TeamListView


app_name = 'timk'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', AllListView.as_view(), name='world-cup-groups'),
    path('sports/', views.sports_list, name='sports'),
    path('games/', MatchListView.as_view(), name='world-cup-groups'),
    path('teams/', TeamListView.as_view(), name='teams'),
    path('group-<str>-matches/', GroupDetailView.as_view(), name='group-matches'),
    path('<slug:slug>/', MatchDetailView.as_view(), name='match-details'),
    
]

