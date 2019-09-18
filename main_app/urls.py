from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/',views.home, name='home'), #not sure if we need this one?
# 	path('structures/', views.structure_view, name='index'),
	# path('structures/create/', views.structure_create, name ='create'),
	path('structures/<int:data_structures_id>/', views.structure_detail, name='detail'),
	# path('structures/<int:data_structures_id>/edit/', views.structure_edit, name='edit'),
# 	path('structures/<int:data_structures_id>/assoc_element/<int:element_id>', views.assoc_element, name ='assoc_element'),
# 	path('structures/<int:data_structures_id>/assoc_prop/<int:prop_id>', views.assoc_prop, name ='assoc_prop'),
# 	path('structures/<int:data_structures_id>/assoc_method/<int:method_id>', views.assoc_method, name ='assoc_method'),
	#########CBV paths########
	path('structures/', views.StructureList.as_view(), name = 'index'),
	# path('structures/<int:pk>/', views.StructureDetail.as_view(), name = 'detail'),
	path('structures/<int:data_structures_id>/update/', views.structure_update, name = 'update'),
	path('structures/<int:pk>/delete/', views.StructureDelete.as_view(), name = 'delete'),
	path('structures/create/', views.StructureCreate.as_view(), name = 'create'),

	# Account Functionality
	path('accounts/signup', views.signup, name='signup'),	
	# Testing Routes
	path('structures/<int:data_structures_id>/info', views.structure_info, name='info'),
	path('structures/<int:data_structures_id>/js', views.structure_download_js, name='download_js'),
	path('structures/<int:data_structures_id>/py', views.structure_download_py, name='download_py'),
]
