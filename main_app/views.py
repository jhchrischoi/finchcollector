from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Finch
from .forms import FeedingForm
from django.views.generic import ListView, DetailView

class FinchList(ListView):
  model = Finch

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.filter()
    return render(request, 'finches/index.html', 
    { 
        'finches': finches 
    }
)

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form=FeedingForm()
  return render(request, 'main_app/detail.html', { 'finch': finch, 'feeding_form':feeding_form })

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

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)