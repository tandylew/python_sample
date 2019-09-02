from .forms import DateForm, SqlForm, AuthenticationForm
from json import JSONEncoder
import urllib.request
import datetime
import re


def index(request):
        if request.method == 'GET':
            form = DateForm(request.POST)
            sql = SqlForm(request.POST)
            return render(request, 'create_task.html', {'form': form, 'sql': sql})
            #return HttpResponse("Hello Word. You're Andy")
        elif request.method == 'POST':
            return HttpResponseRedirect('/display_task/')

def display_task(request):
    if request.method == 'GET':
        result = mycursor.fetchall()
        return render(request, 'display_task.html', {'task_list': result})
    elif request.method == 'POST':
        return HttpResponse("Hello Word. You're Andy")

def graph(request):
    if request.method == 'GET':
        plt.plot(range(20))
        plt.savefig("todo/graph.png")
        image_data = open("todo/graph.png", "rb").read()
        return HttpResponse(image_data, content_type="image/png")

def park(request):
    if request.method == 'GET':
        image_data = open("todo/park.jpg", "rb").read()
        return HttpResponse(image_data, content_type="image/jpg")

def login_info(request):
    if request.method == 'GET':
        login_info = AuthenticationForm(request.POST) 
        return render(request, 'login.html', {'login': login_info})
    if request.method == 'POST':
        response = request.read().decode().split('&')
        username = response[1][response[1].find('=')+1:]
        password = response[2][response[2].find('=')+1:]
        #request.session = get_user_model()._meta.pk.to_python(request.session[SESSION_KEY])
        #username = request.POST['username']
        #password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            print("User: " + username + "Password: " + password)
            login(request, user)
            return HttpResponse("Hello Word. You're " + username)
        else:
            try:              
                 user = User.objects.create_user(username, password=password)
                 login(request, user)
            except:
                 username = 'Andy'
        return HttpResponse("Hello Word. You're " + username)
