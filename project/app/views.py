from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, UserForm2
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'Name: {name}<br>'
                            f'Age: {age}')
    else:
        form = UserForm()
        form2 = UserForm2()
        return render(request, 'app/index.html', context={'form': form, 'form2': form2})
