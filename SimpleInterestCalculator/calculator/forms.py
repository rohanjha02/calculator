from django import forms
from .models import Calculation

class calculationForm(forms.ModelForm): #Forms to take data input from users
    class Meta:
        model = Calculation
        fields = ['principal', 'rate', 'time']
