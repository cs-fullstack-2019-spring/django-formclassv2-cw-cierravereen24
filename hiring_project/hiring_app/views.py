from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'hiring_app/index.html')


def employeeInfo(request):
    if(request.method == "POST");
        print("Your info has been submitted")
        name = request.Post["name"]
        dateOfBirth = request.Post["dateOfBirth"]
        position = request.Post["position"]
        salary = request.Post["salary"]
    return render(request, 'hiring_app/employeeInfo.html', {'emp_app' : })