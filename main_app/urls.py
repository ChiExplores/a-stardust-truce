from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/',views.home, name='home'), #not sure if we need this one?
# 	path('structures/', views.structure_view, name='index'),
# 	path('structures/create/', views.structure_create, name ='create'),
# 	path('structures/<int:data_structures_id>/', views.structure_detail, name='detail'),
# 	path('structures/<int:data_structures_id>/edit/', views.structure_edit, name='edit'),
# 	path('structures/<int:data_structures_id>/assoc_element/<int:element_id>', views.assoc_element, name ='assoc_element'),
# 	path('structures/<int:data_structures_id>/assoc_element/<int:element_id>/delete', views.delete_assoc_element, name ='delete_assoc_element'), 
# 	path('structures/<int:data_structures_id>/assoc_prop/<int:prop_id>', views.assoc_prop, name ='assoc_prop'),
# 	path('structures/<int:data_structures_id>/assoc_prop/<int:prop_id>/delete', views.delete_assoc_prop, name ='delete_assoc_prop'),
# 	path('structures/<int:data_structures_id>/assoc_method/<int:method_id>', views.assoc_method, name ='assoc_method'),
# 	path('structures/<int:data_structures_id>/assoc_method/<int:method_id>/delete', views.delete_assoc_method, name ='delete_assoc_method'),


	# Account Functionality
	path('accounts/signup', views.signup, name='signup'),
	
]
