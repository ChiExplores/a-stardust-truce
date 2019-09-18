from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from main_app.dependencies import checkMethod, checkProperty
from .models import *
from django.http import HttpResponse, FileResponse

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


class StructureCreate(CreateView):
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
    print(ds)
    return render(request, 'detail_test.html', {
        'ds':ds,
        'py': py,
        'js': js
    })


def structure_info(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()
    valid_props = ds.__get_valid_properties__()

    return render(request, './main_app/info.html', {
        'ds': ds,
        'js': js,
        'py': py,
        'valid_props': valid_props
    })

def structure_download_js(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    filename = f'{ds.user.username}.txt'
    js_data = open(filename, 'w+')
    file_data = js
    js_data.write(file_data)
    return FileResponse(open(filename, 'rb'), as_attachment=True, filename=f'{ds.name}.js')


class Ds_Update(UpdateView):
    model = Data_Structure
