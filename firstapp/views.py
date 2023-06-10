from django.shortcuts import render

# Create your views here.

from .models import course, teacher, faculty

def index(request):
    num_course = course.objects.all().count()
    num_teacher = teacher.objects.count()

    return render(
        request,
        'index.html',
        context = {'num_course':num_course,'num_teacher':num_teacher},
    )

from django.views import generic

class courseListView(generic.ListView):
    model = course

class courseDetailView(generic.DetailView):
    model = course