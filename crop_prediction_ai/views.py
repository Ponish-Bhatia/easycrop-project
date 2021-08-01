from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CropPredictionForm
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from .models import advertisement
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import CreateAdForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from keras.utils import to_categorical
def home(request):
	return render(request, 'home.html', { None:None })
def predictcrop(request):
	if request.method=='GET':
		return render(request, 'predictcrop.html', {'form':CropPredictionForm})
	elif request.method=='POST':
		try:
			crops = pd.read_csv(staticfiles_storage.path(settings.STATIC_ROOT / 'crops.csv'))
			encode_dic = {'label':{'rice': 1,'maize': 2,'chickpea': 3,'kidneybeans': 4,'pigeonpeas': 5,'mothbeans': 6,'blackgram': 7,'lentil': 8,'banana': 9,'mango': 10,'watermelon': 11,'apple': 12,'orange': 13,'papaya': 14,'coconut': 15,'cotton': 16,'jute': 17,'coffee': 18,'mungbean':19,'pomegranate':20,'grapes':21,'muskmelon':22}}
			crops = crops.replace(encode_dic)
			x_values = crops[['N','P','K','temperature','humidity','ph','rainfall']]
			x_valuesdf = pd.DataFrame(x_values)
			y_values = crops['label']
			ai = DecisionTreeClassifier()
			ai.fit(x_valuesdf, y_values)
			# x_values = crops[['N','P','K','temperature','humidity','ph','rainfall']]
			# x_valuesdf = pd.DataFrame(x_values)
			# y_values = crops['label']
			# y_values
			# y_values = to_categorical(y_values)
			# ai = Sequential()
			# ai.add(Dense(20, input_dim=7, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(23, activation='softmax'))
			# ai.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
			# ai.fit(x_valuesdf, y_values, epochs=20, shuffle=True)
			test = pd.DataFrame()
			test['N']=[int(request.POST.get('Nitrogen_in_soil'))]
			test['P']=[int(request.POST.get('Phosphorus_in_soil'))]
			test['K']=[int(request.POST.get('Pottasium_in_soil'))]
			test['temperature']=[int(request.POST.get('temperature'))]
			test['rainfall']=[int(request.POST.get('rainfall_in_mm'))]
			test['ph']=[int(request.POST.get('Soil_ph_value'))]
			test['humidity']=[int(request.POST.get('humidity'))]
			crop_type = ai.predict(test)
			# crop_type = np.argmax(crop_type)
			crop_type = list(encode_dic.get('label').keys())[list(encode_dic.get('label').values()).index(crop_type)]
			return render(request, 'predictcrop.html', {'form':CropPredictionForm, 'crop':crop_type})
		except ValueError:
			return render(request, 'predictcrop.html', {'form':CropPredictionForm, 'error_value_name_type':"All fields should have a number error type: TypeError"})
def creditsuser(request):
	return render(request, 'creditsuser.html', { None:None })
def advertisements(request):
	return render(request, 'advertisements.html', {'ads':advertisement.objects.order_by('-id')})
def detail_ad(request, pk):
	ad = get_object_or_404(advertisement, pk=pk)
	return render(request, 'detailad.html', {'ad':ad})
class SignUp(generic.CreateView):
	form_class = UserCreationForm
	on_success = reverse_lazy('login')
	template_name = 'registration/signup.html'

	def form_valid(self, form):
		view = super(SignUp, self).form_valid(form)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		u = authenticate(username=username, password=password)
		login(self.request, u, backend='django.contrib.auth.backends.ModelBackend')
		return view

@login_required
def createad(request):
	if request.method=='GET':
		return render(request, 'createad.html', {'form':CreateAdForm()})
	if request.method=='POST':
		# f = advertisement()
		# f['title']=request.POST['title']
		# f['description']=request.POST['description']
		# f['image']=request.FILES['image']
		# f['cost']=request.POST['cost']
		# f['address']=request.POST['address']
		# f['user']=request.user
		form=CreateAdForm(request.POST, request.FILES)
		if form.is_valid():
			new_todo=form.save(commit=False)
			new_todo.user = request.user
			# new_todo.image = request.FILES['image']
			new_todo.save()
		else:
			return render(request, 'createad.html', {'form':CreateAdForm(), 'error':form.errors})
		return redirect('home')

def bmc(request):
	return render(request, 'BMC.html')

def predictionintro(request):
	return render(request, 'predictionintro.html')
