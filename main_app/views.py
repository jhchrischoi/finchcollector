from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Finch 
from django.views.generic import ListView


# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class FinchList(ListView):
  model = Finch

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'main_app/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'population', 'habitat', 'trend']

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a finch by excluding the name field!
  fields = ['population', 'habitat', 'trend']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'