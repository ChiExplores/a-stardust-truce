from django.urls import path, include
from . import views
#  /submit path suffix allows for recreation of Datastructure form through entire create/update process
urlpatterns = [
	path('', views.home, name='home'),
	path('about/',views.home, name='home'), 
	path('structures/index', views.structure_index, name='user_structures'),
	path('structures/<int:data_structures_id>/', views.structure_info, name='info'),
	path('structures/<int:data_structures_id>/update/', views.structure_update, name = 'update'),
	path('structures/<int:data_structures_id>/updater/', views.structure_updaterrr, name = 'updater'),
	path('structures/<int:data_structures_id>/update/submit', views.structure_update_submit, name = 'submit'),
	path('structures/<int:data_structures_id>/methods/submit', views.structure_methods_submit, name='methods_submit'),
	path('structures/<int:data_structures_id>/methods/', views.structure_methods, name='methods'),
	path('structures/create/submit', views.structure_create_submit, name = 'create_submit'),
	path('structures/create/', views.structure_create, name = 'create'),
	path('structures/', views.StructureList.as_view(), name = 'index'),
	path('structures/<int:pk>/delete/', views.StructureDelete.as_view(), name = 'delete'),

	# Account Functionality
	path('accounts/signup', views.signup, name='signup'),	
	
	# Testing Routes
	path('structures/<int:data_structures_id>/info', views.structure_info, name='info'),
	path('structures/<int:data_structures_id>/info_testing', views.structure_info_testing, name='info_testing'),
	path('structures/<int:data_structures_id>/js', views.structure_download_js, name='download_js'),
	path('structures/<int:data_structures_id>/py', views.structure_download_py, name='download_py'),
]
