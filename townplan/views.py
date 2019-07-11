from django.shortcuts import render,redirect
from .models import Works,Document,Message
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']
        mes = Message.objects.create(name=name,email=email,msg=msg)
        mes.save()
        return redirect('/')

    else:
        #wors = Works.objects.all()
        wors = Works.objects.all()
        docs = Document.objects.all()
        return render(request, "index.html",{'wors': wors,'docs':docs})