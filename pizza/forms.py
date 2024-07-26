from django import forms
from .models import Size, Pizza

#use the models to create a form
class PizzaForm(forms.ModelForm):
    #Can also specify widgets here
    #size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    #adding image to forms
   # image=forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}
        #widgets in class form.
        #widgets = {'size': forms.CheckboxSelectMultiple}

# class PizzaForm(forms.Form):
#     #use widgets to modify a form

#     topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.Textarea)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])


#multiple pizzas form

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)