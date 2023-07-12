from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', ProjectListView.as_view(), name='project-list'),
    path('portfolio/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]
