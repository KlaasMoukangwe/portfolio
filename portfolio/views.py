from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 10
    ordering = ['-created_at']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'