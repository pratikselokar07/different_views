from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect, render
# from django.views import View
from myapp.forms import StudentForm

from myapp.models import Student

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name='student_list.html'

class IndexTemplateView(TemplateView):
    template_name = "index.html"

def get_context_data(self, **kwargs):
    context = get_context_data(**kwargs)
    # context["name"] = 'Pratik'
    # context["email"] = 'pratik@gmail.com'
    # context["phone"] = 7896541235
    context ={'name': 'Pratik','phone':7758962514}
    return context

class StudentDetailView(DetailView):
    model = Student
    template_name='detail_view.html'
    context_object_name = 'students'
    pk_url_kwarg='id'

class StudentFormView(FormView):
    template_name='form_view.html'
    form_class=StudentForm
    success_url='/show/'
    
    def get_queryset(self):
        return Student.objects.all()
    
    def form_valid(self,form):
        return super().form_valid(form)


class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','phone']
    template_name='create_view.html'
    success_url='/thanks/'
    # template_name='form_view.html'
    # form_class=StudentForm
    # success_url='/show/'
class Thanks(TemplateView):
    template_name='thanks.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','phone']
    template_name='update_view.html'
    success_url='/show/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name='delete_view.html'
    success_url='/show/'
