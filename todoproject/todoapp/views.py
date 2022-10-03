from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView



class Tasklist(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'taskk'


class taskdetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class taskupdate(UpdateView):
    model = Task
    template_name = 'update2.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvedetail',kwargs={'pk':self.object.id})




class taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.

def home(request):
    taskk=Task.objects.all()
    if request.method=='POST':
      name=request.POST.get('task')

      priority=request.POST.get('priority')
      date=request.POST.get('date')
      task=Task(name=name,priority=priority,date=date)
      task.save()


    return render (request,'home.html' ,{"taskk":taskk})


def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
      task.delete()
      return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    taskk = Task.objects.get(id=id)
    tu=TodoForm(request.POST or None,instance=taskk)
    if tu.is_valid():
        tu.save()
        return redirect('/')
    return render(request,'update.html',{'tu':tu,'taskk':taskk})