from django.shortcuts import render, redirect
from .forms import calculationForm
from .models import Calculation

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = calculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.result = instance.principal * (instance.rate/100) * instance.time
            instance.save()
            return  redirect('index')
    else:
        form = calculationForm()
    
    calculations = Calculation.objects.all().order_by('timestamp')
    return render(request, 'index.html', {'form': form, 'calculations': calculations})
    
