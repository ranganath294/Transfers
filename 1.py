# urlsfrom django.urls import path
from . import views

urlpatterns = [
    path('minerbot/', views.minerbot_view, name='minerbot'),
    path('rvr_graph/', views.rvr_graph_view, name='rvr_graph'),
    # Add more paths as needed
]


# views

from django.shortcuts import render

def minerbot_view(request):
    return render(request, 'minerbot.html', {'active_tab': 'minerbot'})

def rvr_graph_view(request):
    return render(request, 'rvr_graph.html', {'active_tab': 'rvr_graph'})

# Add more views as needed




