from django.shortcuts import render, HttpResponse
from .forms import UserForm

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.save()
                return HttpResponse('Sucesso')
            except:
                return HttpResponse('Erro ao Criar o Usuario. Por favor, reporte para equipe tecnica.')
    else:
        form = UserForm()
    return render(request, 'cadastro.html', {'form': form})



