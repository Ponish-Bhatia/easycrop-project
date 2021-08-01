from django.db import models
from django import forms
from .models import advertisement

class CropPredictor(models.Model):
	Nitrogen_in_soil = models.IntegerField()
	Phosphorus_in_soil = models.IntegerField()
	Pottasium_in_soil = models.IntegerField()
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	Soil_ph_value = models.IntegerField()
	rainfall_in_mm = models.IntegerField()
class CropPredictionForm(forms.ModelForm):
	class Meta():
		model = CropPredictor
		fields = ['Nitrogen_in_soil', 'Phosphorus_in_soil', 'Pottasium_in_soil', 'temperature', 'humidity', 'Soil_ph_value', 'rainfall_in_mm']
		labels={
			'Nitrogen_in_soil':'Nitrogen in soil (in Parts Per Million)',
			'Phosphorus_in_soil':'Phosphorus in soil (in Parts Per Million)',
			'Pottasium_in_soil':'Potassium in soil (in Parts Per Million)',
			'temperature':'Temperature (in Celsius)',
			'humidity':'Humidity in air (in percentage)',
			'Soil_ph_value':'Soil pH value',
			'rainfall_in_mm':'Rainfall (in millimetre)',
		}
		widgets = {
		'Nitrogen_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Phosphorus_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Pottasium_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'temperature':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'humidity':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'rainfall_in_mm':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Soil_ph_value':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
	}

class CreateAdForm(forms.ModelForm):
	class Meta():
		model = advertisement
		fields = ['title','description','image','cost', 'currency', 'address', 'payment_method', 'payment_link', 'country_call_code', 'contact_Number']
		labels={
					'cost':'cost(for 1 Kg)',
					'currency':'specify your currency',
					'contact_Number':'Contact Number (include area code if any)'
				}
