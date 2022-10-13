from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .service import regular_streings


def index(request):
    if request.method == "POST":
        regul = request.POST.get("regul")
        text = request.POST.get("text")
        if regular_streings(regul, text):
            return HttpResponse("Совпадения найдены")
        if not regular_streings(regul,text):
            return HttpResponse("Регулярное выражение не верно")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})