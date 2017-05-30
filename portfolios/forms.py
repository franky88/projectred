from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = [
			"cat",
			"art_name",
			"short_des",
			"image",
		]