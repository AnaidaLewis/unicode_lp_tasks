from django import forms
from .models import ToDoList, Item

class List(forms.ModelForm):
	class Meta:
		model = ToDoList
		fields = '__all__'

# class Items(forms.ModelForm):
# 	class Meta:
# 		model = Item
# 		fields = '__all__'

# class List(forms.Form):
# 	name = forms.CharField(label="ToDoList", max_length=200)
# 	check = forms.BooleanField(required =False)

# class Items(forms.Form):
# 	name = forms.CharField(label="Enter Item", max_length=200)
# 	check = forms.BooleanField(required =False)