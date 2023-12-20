from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from demo.forms import RegisterUserForm
from demo.models import User


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


def about(request):
    #products = Product.objects.filter(count__gte=1).order_by('-date')[:5]
    return render(request, 'demo/about.html',
    {})

def application(request):
    return render(request, 'demo/application.html',
    {})


