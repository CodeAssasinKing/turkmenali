from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import FormMessage
# Create your views here.
def index(request):
    return render(request, "core/index.html")



def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "core/contacts.html")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        form = FormMessage.objects.create(name=name, email=email, message=message)

        try:
            form.save()
            return render(request, "core/success.html")
        except Exception as e:
            print(e)
            return render(request, "core/error.html")


def messages(request):
    messages = FormMessage.objects.all()
    context = {
        "messages": messages
    }
    return render(request, "core/messages.html", context)