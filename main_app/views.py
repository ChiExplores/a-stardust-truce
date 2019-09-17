from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from main_app.dependencies import checkMethod, checkProperty
from .models import *
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


# def structures_index(request):
#   # This reads ALL structures, not just the logged in user's structures
#   structures = Data_Structure.objects.all()
#   public_structures = Data_Structure.objects.filter(user=request.user)
#   return render(request, 'structures/index.html', { 'structures': structures })


class StructureCreate(LoginRequiredMixin,CreateView):
  model = Data_Structure
  fields = '__all__'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class StructureUpdate(UpdateView):
  model = Data_Structure
  fields = '__all__'

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

    return render(request, './main_app/info.html', {
        'ds': ds,
        'js': js,
        'py': py,
    })

def structure_download(request, data_structures_id):
    ds = Data_Structure.objects.get(id = data_structures_id)
    js = ds.__get_js__()
    py = ds.__get_py__()

    js_data = open(f'{ds.name}.js', 'w+')
    file_data = js
    js_data.write(file_data)
    # response = HttpResponse(js_data, content_type='application/javascript') 
    # response['Content-Disposition'] = "attachment; filename='somejs.js'"
    response = FileResponse(open(f'{ds.name}.js', 'rb'), as_attachment=False, filename='somejs.js')
    return response

#  with open('output.txt', 'w') as f:
#      f.write('Hi there!')

def send_file(response):

    img = open('images/bojnice.jpg', 'rb')

    response = FileResponse(img)

    return response

def send_file(response):

    img = open('images/bojnice.jpg', 'rb')

    response = FileResponse(img)

    return response

class Ds_Update(UpdateView):
    model = Data_Structure
