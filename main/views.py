from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Dish

class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'

    def post(self,request):
        dish_id = request.POST.get('dish_id')
        cart = request.session.get('cart', {})
        if dish_id in cart:
            cart[dish_id] += 1
        else:
            cart[dish_id] = 1

        request.session['cart'] = cart
        return redirect('/?show_cart=true')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        cart_item = []
        total_price = 0
        for dish_id, quantity in cart.items():
            dish = Dish.objects.get(id=dish_id)
            dish.quantity = quantity
            cart_item.append(dish)
            total_price +=dish.price * quantity
        context['cart_items'] = cart_item
        context['total_price'] = total_price
        context['show_cart'] = self.request.GET.get('show_cart','false') == 'true'
        return context

