from django.shortcuts import render
# from .tasks import add
from .tasks import add, sub
# Create your views here.

# def index(request):
#     print("Results: ")
#     result = add.delay(20, 10)
#     print("Result: ", result)
#     result1 = sub.delay(30, 10)
#     print("Result: ", result1)
#     return render(request, "myapp/home.html")

def index(request):
    print("Results: ")
    result = add.apply_async(args=[10, 20])
    print("Result: ", result)
    result1 = sub.apply_async(args=[30, 10])
    print("Result: ", result1)
    return render(request, "myapp/home.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")


