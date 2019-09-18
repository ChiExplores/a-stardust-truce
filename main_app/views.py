from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from main_app.dependencies import checkMethod, checkProperty
from .models import *
from django.http import HttpResponse, FileResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import tempfile

# checkComponent signature
# checkComponent(component, data_structure, on_success, on_failure)

# Account Functionality
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# List of Views
def home(request):
    return render(request, './main_app/edit.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class StructureList(ListView):
    model = Data_Structure
    paginate_by = 8

# def structures_index(request):
#   # This reads ALL structures, not just the logged in user's structures
#   structures = Data_Structure.objects.all()
#   public_structures = Data_Structure.objects.filter(user=request.user)
#   return render(request, 'structures/index.html', { 'structures': structures })


class StructureCreate(LoginRequiredMixin,CreateView):
  model = Data_Structure
  fields = '__all__'
	

class StructureUpdate(UpdateView):
  model = Data_Structure
  fields = ['name', 'description', 'element']
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args)
    context['properties'] = self.object.__get_valid_properties__()
    context['methods'] = self.object.__get_valid_methods__()
    return context

    
class StructureDelete(DeleteView):
    model = Data_Structure
    success_url = '/structures/'

# stubbed detailed
def structure_detail(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    py = ds.__get_py__()
    js = ds.__get_js__()
    methods = ds.methods.all()
    props = ds.properties.all()
    return render(request, 'detail_test.html', {
        'ds':ds,
        'py': py,
        'js': js,
        'methods': methods,
        'props' : props
    })


def structure_info(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()
    

    return render(request, './main_app/info.html', {
        'ds': ds,
        'js': js,
        'py': py,
        'request.user': request.user,
    })

# def structure_download(request, data_structures_id):
#     ds = Data_Structure.objects.get(id = data_structures_id)
#     js = ds.__get_js__()
#     py = ds.__get_py__()


#     js_data = open(f'{ds.name}.js', 'w+')
#     file_data = js
#     js_data.write(file_data)
#     response = HttpResponse(js_data, content_type='application/javascript') 
#     response['Content-Disposition'] = "attachment; filename='somejs.js'"
#     return FileResponse(open(f'{ds.name}.js', 'rb'), as_attachment=True, filename='somejs.js')

def structure_download(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()


    with open(f'{ds.user.username}.js', 'w+') as js_data:
        file_data = js
        js_data.write(file_data)

        response = HttpResponse(js_data, content_type='application/javascript') 
        response['Content-Disposition'] = "attachment; filename=f'{ds.name}.js'"
        return FileResponse(open(f'{ds.user.username}.js', 'rb'), as_attachment=True, filename=f'{ds.name}.js')
