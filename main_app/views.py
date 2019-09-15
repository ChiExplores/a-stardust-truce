from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from main_app.dependencies import checkMethod, checkProperty
from .models import Data_Structure, Element

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


  # This inherited method is called when a
  # valid structure form is being submitted
#   def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#     form.instance.user = self.request.user
#     # Let the CreateView do its job as usual
#     return super().form_valid(form)


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
        'props': ds.properties,
        'js': js,
        'py': py,
    })