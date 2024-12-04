# accounts/context_processors.py

from .models import CartItem  # Import the CartItem model

def cart_item_count(request):
    """
    This function calculates the total number of items in the cart
    for the currently authenticated user.
    """
    if request.user.is_authenticated:
        # Fetch all cart items for the logged-in user
        cart_items = CartItem.objects.filter(user=request.user)
        
        # Calculate the total quantity of items in the cart
        total_items = sum(item.quantity for item in cart_items)
    else:
        total_items = 0  # For unauthenticated users, set cart count to 0

    # Return the count as a dictionary to be used in templates
    return {'cart_item_count': total_items}
