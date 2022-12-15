from django.shortcuts import render,redirect # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Customer,Rental,Vehicle_Type,Vehicle_Size,Vehicle,Rental_Rate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
# takes a request, returns a response

# index function renders homepage.html template
def rental(request):
    rentals = Rental.objects.all().order_by('rental_date')
    context = {
        'rental': rentals,
    }
    return render(request, 'rental.html', context)

def rentalint(request,id):
    rental = Rental.objects.filter(pk=id)
    context = {
        'rental': rental,
    }
    return render(request, 'rentalint.html', context)


"""def addTodo(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = TodoForm(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        # GET, generate blank form
        context['form'] = TodoForm()
    return render(request, 'home.html', context)

from .forms import TodoForm
def done(request):
    todos = Todo.objects.all().order_by('-pk')
    task_id = request.POST.get('task_id')
    todo = Todo.objects.get(pk=task_id)
    context = {
        'todo': todos,
        'task': todo,
        'id': task_id,
        'form': TodoForm,
    }

    if request.method == 'POST':
        if todo.has_been_done !=True:
            todo.has_been_done = True
            todo.save()
        else:
            todo.has_been_done = False
            todo.save()
            return render(request, 'home.html', context)
        return render(request, 'home.html', context)
    else:
       return render(request, 'home.html', context)
       """