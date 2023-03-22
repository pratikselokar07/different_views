from django.urls import path
from .import views


urlpatterns = [
    path('show/',views.StudentListView.as_view(),name='show'),
    path('index/',views.IndexTemplateView.as_view(extra_context={'email':'Pratik002@gmail.com'}),name='index'),
    path('detail/<int:id>',views.StudentDetailView.as_view(),name='detail'),
    path('form_view/',views.StudentFormView.as_view(),name='form_view'),
    path('create_view/',views.StudentCreateView.as_view(),name='create_view'),
    path('thanks/',views.Thanks.as_view(),name='thanks'),
    path('update_view/<int:pk>',views.StudentUpdateView.as_view(),name='update_view'),
    path('delete_view/<int:pk>',views.StudentDeleteView.as_view(),name='delete_view'),

    path('api_view/',views.StudentApiView.as_view(),name='api_view'),
    path('api_view/<int:pk>/',views.StudentApiView.as_view(),name='api_view'),
    
    path('list_create_view/',views.StudentListCreateView.as_view(),name='list_create_view'),
    path('retrive_update_view/<int:pk>/',views.StudentRetrieveUpdateView.as_view(),name='retrive_update_view'),
    path('retrive_destroy_view/<int:pk>/',views.StudentRetrieveDestroyView.as_view(),name='retrive_destroy_view'),

]
