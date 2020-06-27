from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def todolist(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {
        'todo_items': todo_items
    })

@csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST["content"]
    create_obj = Todo.objects.create(added_date=current_date, text_input=content)
    print(create_obj)
    print(create_obj.id)
    length_of_todos = Todo.objects.all().count()
    print(f'Total = {length_of_todos}')
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')


# Create your views here.
