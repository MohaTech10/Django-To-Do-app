from django.forms import ModelForm
from .models import *

# to create instances we have to get to their columns and attributes by creating a from base on a model
# we will have the all attribute to crate instance suits the model fields
class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
