from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from main_app.dependencies import checkMethod, checkProperty
from .models import *
import tempfile

# Account Functionality
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, './main_app/home.html')

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
    model = DataStructure
    paginate_by = 6

@login_required()
def structure_index(request):
  structures_list = DataStructure.objects.filter(user = request.user.id)
  paginator = Paginator(structures_list, 6)
  page = request.GET.get('page')
  is_paginated = paginator.num_pages > 1
  structures = paginator.get_page(page)
  return render(request, './main_app/index.html', {
      'page_obj' : structures,
      'paginator': paginator,
      'is_paginated': is_paginated 
      })

@login_required
def structure_create(request):
    return render(request, 'main_app/data_structure_form.html', {
        'new_form': True,
        'elements': Element.objects.all(), 
    })

@login_required
def structure_create_submit(request):
    new = request.POST
    try:
        new_ds = DataStructure(
            name=new['name'], 
            description=new['description'], 
            element=Element.objects.get(id=new['element']), 
            user=request.user
        )
        new_ds.save()
        return redirect(f'/structures/{new_ds.id}/update')
    except:
        return redirect('/create')

@login_required	
def structure_update(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    return render(request, 'main_app/data_structure_form.html', {
        'new_form': not bool(ds),
        'methods_update': False,
        'name': ds.name, 
        'description': ds.description,
        'element': ds.element,
        'properties': ds.properties.all(), 
        'valid_properties': ds.__get_valid_properties__(), 
    })

@login_required
def structure_update_submit(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    new = request.POST
    try:
        ds.name = new['name']
        ds.description = new['description']
        ds.properties.set(Property.objects.filter(Q(id__in=new.getlist('properties')) & Q(id__in=ds.__get_valid_properties__())))
        ds.save()
        return redirect(f'/structures/{ds.id}/methods')
    except:
        return redirect(f'/structures/{ds.id}/update')
    pass

@login_required
def structure_methods(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    return render(request, 'main_app/data_structure_form.html', {
        'new_form': not bool(ds),
        'methods_update': True,
        'name': ds.name, 
        'description': ds.description,
        'element': ds.element,
        'properties': ds.properties.all(), 
        'valid_properties': ds.__get_valid_properties__(), 
        'methods': ds.methods.all(),
        'valid_methods': ds.__get_valid_methods__()
    })

@login_required
def structure_updaterrr(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    return render(request, 'main_app/edit.html', {
        'new_form': not bool(ds),
        'name': ds.name, 
        'description': ds.description,
        'element': ds.element,
        'properties': ds.properties.all(), 
        'valid_properties': ds.__get_valid_properties__(), 
        'methods': ds.methods.all(),
        'valid_methods': ds.__get_valid_methods__()
        })
        
@login_required
def structure_methods_submit(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    new = request.POST
    try:
        ds.name = new['name']
        ds.description = new['description']
        ds.methods.set(Method.objects.filter(Q(id__in=new.getlist('methods')) & Q(id__in=ds.__get_valid_methods__())))
        ds.save()
        return redirect(ds.get_absolute_url())
    except:
        return redirect(f'/structures/{ds.id}/methods')

class StructureDelete(LoginRequiredMixin, DeleteView):
    model = DataStructure
    success_url = '/structures/'

def structure_info(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()
    methods = ds.methods.all()
    props = ds.properties.all()
    return render(request, './main_app/info.html', {
        'ds': ds,
        'js': js,
        'py': py,
        'request.user': request.user,
        'methods': methods,
        'props' : props,
    })

def structure_download_js(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    filename = f'serve_code/{ds.user.username}.txt'
    js_data = open(filename, 'w+')
    file_data = js
    js_data.write(file_data)
    return FileResponse(open(filename, 'rb'), as_attachment=True, filename=f'{ds.name}.js')

def structure_download_py(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    py = ds.__get_py__()
    filename = f'serve_code/{ds.user.username}.txt'
    py_data = open(filename, 'w+')
    file_data = py
    py_data.write(file_data)
    return FileResponse(open(filename, 'rb'), as_attachment=True, filename=f'{ds.name}.py')

def structure_info_testing(request, data_structures_id):
    ds = DataStructure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()
    methods = ds.methods.all()
    props = ds.properties.all()

    return render(request, './main_app/info_testing.html', {
        'ds': ds,
        'js': js,
        'py': py,
        'request.user': request.user,
        'methods': methods,
        'props' : props
    })



