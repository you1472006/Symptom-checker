from django.shortcuts import render, get_object_or_404
from .models import Symptom, Disease
from .forms import SymptomForm

def symptom_checker(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            
            entered_symptoms = form.cleaned_data['symptoms'].split('\r\n')
            print(entered_symptoms)
            suggested_diseases = Disease.objects.filter(symptoms__name__in=entered_symptoms).distinct()
            return render(request, 'results.html', {'suggested_diseases': suggested_diseases})
    else:
        form = SymptomForm()
        soso= Symptom.objects.all()
    return render(request, 'input.html', {'form': form,'soso':soso})

def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, pk=disease_id)
    return render(request, 'disease_detail.html', {'disease': disease})
