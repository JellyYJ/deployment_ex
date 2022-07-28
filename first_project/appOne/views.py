from django.shortcuts import render
from django.http import HttpResponse

## URL mapping lesson
# def index(request):
#     return HttpResponse("Aw yeah!")

# Template lesson
def index(request):
    # the content my_dict
    # the key: insert_me
    my_dict = {'insert_me':"I am from views.py"}
    return render(request,'index.html',context = my_dict)
