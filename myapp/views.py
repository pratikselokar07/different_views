from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect, render
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
# from django.views import View
from myapp.forms import StudentForm

from myapp.models import Student

class StudentView(View):
    def get(self, request):
        students=Student.objects.all()
        return render(request,'student_list.html',{'students':students})

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

class StudentApiView(APIView):
    # def get(self, request, format=None):
    #     students = Student.objects.all()
    #     serializer = StudentSerializer(students, many=True)
    #     return Response(serializer.data)

    def get(self, request, pk=None, format=None):
        if pk:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id=pk
        students=Student.objects.get(pk=id)
        serializer=StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id=pk
        students=Student.objects.get(pk=id)
        serializer=StudentSerializer(students,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        students=Student.objects.get(pk=id)
        students.delete()
        return Response({'msg':'Data Deleted'})

class StudentListCreateView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentListCreateView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        students=Student.objects.get(pk=id)
        serializer=StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk,format=None):
        id=pk
        students=Student.objects.get(pk=id)
        serializer=StudentSerializer(students,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self,request,pk):
        id=pk
        students=Student.objects.get(pk=id)
        students.delete()
        return Response({'msg':'Data Deleted'})
    
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer