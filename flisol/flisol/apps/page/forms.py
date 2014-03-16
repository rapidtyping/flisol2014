from django import forms
from flisol.apps.page.models import Inscrito

class addInscritoForm(forms.ModelForm):
	class Meta:
		model 	= Inscrito