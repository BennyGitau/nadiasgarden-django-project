from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multipleform = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST) #request.FILES
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thank you for ordering! Your order is: %s, %s, %s pizza. \n The order will be ready in 25 minutes' % (filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'], 
            filled_form.cleaned_data['size'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again'
        return render(request, 'pizza/order.html', {'created_pizza_pk': created_pizza_pk,'Pizzaform': filled_form, 'note': note, 'multiple_form': multipleform})

    else:       
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'Pizzaform': form, 'multiple_form': multipleform})
    
def pizzas(request):
    number_pizzzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_pizzzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_pizzzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            #filled_formset.save()
            for form in filled_formset:
                filled_formset.save()
                print(form.cleaned_data['topping1'])
            note ='Pizzas have been ordered'
        else:
            note = 'Please correct the errors'
        return render(request, 'pizza/pizzas.html', {'formset': formset, 'note': note})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Order has been updated.'
            form = filled_form
            return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza, 'note':note})
    return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza})
