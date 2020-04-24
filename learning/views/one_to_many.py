'''
(c) learning 2020

Purpose: learn one to many relationship

'''
from django.shortcuts import render
from django.shortcuts import HttpResponse

from ..models import Mother, Son
from ..forms import UploadSonForm

# Create your views here.
def one_to_many(request):
    if request.method == 'POST':
        form = UploadSonForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mother_inst, created = Mother.objects.get_or_create(first_name=request.POST.get('mother'))
            son = Son(first_name=first_name,last_name=last_name,mother_id=mother_inst.id)
            son.save()
            return render(request,"learning/index.html")
    return render(request,"learning/one_to_many.html")
