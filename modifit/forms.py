from django import forms

class LoginForm(forms.Form):
	username = forms.CharField( label='Username', max_length=50 )
	password = forms.CharField( widget=forms.PasswordInput() )

class RegForm(forms.Form):
	username = forms.CharField( label='Username', max_length=50 )
	email = forms.CharField( label='Email', max_length=50 )
	password = forms.CharField( widget=forms.PasswordInput() )
	first_name = forms.CharField( label='First Name (Optional)', max_length=50, required=False )
	last_name = forms.CharField( label='Last Name (Optional)', max_length=50, required=False )