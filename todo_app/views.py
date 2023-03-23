from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from .models import Todo


# Create your views here.
def home(request):
    todo = Todo()
    all = todo.all() 
    return render(request, 'index.html', {'todos':all})

def modify(request, id):
     todo = Todo()
     todo = todo.get(id)
     return render(request, 'modify.html', {'todo':todo})

def add(request):
    if request.method == 'POST':
            todo = Todo()
            data = {'title': request.POST['title'], 'content':request.POST['content']}
            todo = todo.create(data)
            return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'response':'méthod not allowed'})

def update(request, id):
     if request.method == 'POST':
          todo = Todo()
          data = {'title': request.POST['title'], 'content':request.POST['content']}
          todo.update(data, id)
          return JsonResponse({'response':'success'})
def delete(request, id):
     todo = Todo()
     todo.delete(id)
     return JsonResponse({'response':'success'})