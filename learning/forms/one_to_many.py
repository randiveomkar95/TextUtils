from django import forms
from ..models import Mother, Son

class UploadSonForm(forms.ModelForm):
	class Meta:
		model = Son
		fields = ('first_name','last_name')
