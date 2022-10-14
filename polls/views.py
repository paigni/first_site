from django.shortcuts import render
from django.http import HttpResponse
from polls.forms import UserForm
from polls.services import regular_strings


def index(request):
    if request.method == "POST":
        regul = request.POST.get("regul")
        text = request.POST.get("text")
        service_answer = regular_strings(regul, text)
        return HttpResponse(f"{service_answer}")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})