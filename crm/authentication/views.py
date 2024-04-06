from django.shortcuts import render
from django.views import View
from django.contrib import messages

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        messages.success(request, 'Sucesso!')
        messages.warning(request, 'AVISO!')
        messages.info(request, 'Informativo')
        messages.error(request, 'Erro')
        return render(request, 'authentication/register.html')



