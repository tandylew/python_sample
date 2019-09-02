import os
import urllib.request
import datetime
import re
from json import JSONEncoder
from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('create_task.html')
    #return HttpResponse("Hello Word. You're Andy")

@app.route('/park.jpg')
def park():
    image_data = open("park.jpg", "rb").read()
    #return HttpResponse(image_data, content_type="image/jpg")
    return send_file("park.jpg", mimetype="image/jpg")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

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
