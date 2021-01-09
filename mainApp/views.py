from django.shortcuts import render
from .models import TestModel

def front(request):
    names = TestModel.objects.all()
    context = {'names':names}
    return render(request, template_name='index.html', context=context)