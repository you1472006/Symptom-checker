from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 20, 'rows': 1,'class':'for'})
        
    )
    