from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class UseAuthenticationForm(AuthenticationForm):
   """Extending Django Authentication form to add form-control class"""
   next_url=forms.CharField(widget=forms.HiddenInput(), required=False)
   

   def __init__(self, *args, **kwargs):
      super(UseAuthenticationForm, self).__init__(*args, **kwargs)
      for field_name, field in self.fields.items():
         field.widget.attrs['class']='form-control'

class UserRegistrationForm(UserCreationForm):
    """Extending Django UserCreation Form to add form-control"""
    def __init__(self, *args, **kwargs):
       super(UserRegistrationForm, self).__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
          field.widget.attrs['class']='form-control'
           

class UserForm(forms.ModelForm):     
   """form update User's update Basic information"""
   class Meta:
      model=User
      fields=['first_name', 'last_name']    

   def __init__(self, *args, **kwargs):
       super(UserForm, self).__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
          field.widget.attrs['class']='form-control'
                     

class UserProfileForm(forms.ModelForm):
   """form update to Update User's additional information"""


   class Meta:
      model=UserProfile
      fields=['mobile', 'adress']    

   def __init__(self, *args, **kwargs):
       super(UserProfileForm, self).__init__(*args, **kwargs)
       for field_name, field in self.fields.items():
          field.widget.attrs['class']='form-control'
                                         