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
]
