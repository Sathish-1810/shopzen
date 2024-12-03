from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import logout

from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required
from .models import Product, TeamMember, Contact, CartItem
import random
from .models import Categories
from django.http import HttpResponse
# OTP Generation
def generate_otp():
    return str(random.randint(100000, 999999))

# Home page view
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Password validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            # Create the user but keep them inactive until OTP verification
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.is_active = False
            user.save()

            otp = generate_otp()  # Generate OTP
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            request.session['otp_timestamp'] = timezone.now().isoformat()  # Save timestamp for OTP expiry

            # Prepare email content
            subject = 'Your OTP Code'
            message = f'Your OTP code is {otp}. It will expire in 5 minutes.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            # Send OTP via email and handle potential errors
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'OTP has been sent to your email.')
            except Exception as e:
                messages.error(request, 'Failed to send OTP. Please try again later.')
                print(e)  # Log the error for debugging
                return redirect('register')

            return redirect('verify_otp')

    return render(request, 'registeration.html')
# OTP Verification view
def verify_otp(request):
    if request.method == 'POST':
        otp_timestamp_str = request.session.get('otp_timestamp')

        if otp_timestamp_str:
            # Convert the string to a naive datetime
            otp_timestamp = datetime.fromisoformat(otp_timestamp_str)
            
            # Check if the datetime is naive (lacking timezone)
            if otp_timestamp.tzinfo is None:
                otp_timestamp = timezone.make_aware(otp_timestamp)  # Make it aware if it's naive
            
            # Get the current time as an aware datetime
            current_time = timezone.now()

            # Define the OTP validity duration
            otp_validity_duration = timedelta(minutes=5)
            otp_valid_until = otp_timestamp + otp_validity_duration

            # Check if the OTP is still valid
            if current_time <= otp_valid_until:
                otp = request.POST.get('otp')
                if otp == request.session.get('otp'):
                    user = User.objects.get(id=request.session['user_id'])
                    user.is_active = True
                    user.save()
                    messages.success(request, 'OTP Verified successfully. Your account is now active.')
                    return redirect('login')  # Redirect to login after successful verification
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
            else:
                messages.error(request, 'OTP has expired. Please request a new OTP.')
                return redirect('resend_otp')
        else:
            messages.error(request, 'OTP verification failed. Please try again.')
            
            
            

    return render(request, 'verify_otp.html')
# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


#logoutpage 
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page
#profileview
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


# Product List view



def product_list(request):
    # Get filtering parameters from the request
    category = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    # Start with all products
def product_list(request):
    category = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    products = Product.objects.all()

    # Apply filters
    if category:
        products = products.filter(category__iexact=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Get the category choices from the model
    categories = Product.CATEGORY_CHOICES

    # Pass the products and categories to the template
    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
    })


# About Us view
def aboutus(request):
    team_members = TeamMember.objects.all()
    return render(request, 'aboutus.html', {'team_members': team_members})

# Contact Us view
def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contactUS = Contact(name=name, email=email, message=message)
        contactUS.save()

        return HttpResponse(f'<h1>Thanks for contacting us, {name}!</h1>')

    return render(request, 'contactus.html')

# Add to Cart view
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

# Cart Detail view
@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

# Remove from Cart view
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

# Update Cart view
@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart_detail')

# Payment Page view
@login_required
def payment_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        if payment_method:
            # Assuming payment is processed successfully (you can integrate actual payment gateway)
            try:
                # Send the success email
                subject = 'Your Payment is Successful'
                message = f"Hello {request.user.username},\n\n" \
                          f"Your order has been placed successfully!\n\n" \
                          f"Your order details are as follows:\n\n"
                for item in cart_items:
                    message += f'Product: {item.product.name}\n Quantity: {item.quantity}\n Price: {item.get_total_price()}\n\n'
                message += f'\nTotal Price: {total_price}\n\nThank you for shopping with us!'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [request.user.email]

                # Send the email
                send_mail(subject, message, from_email, recipient_list)

                # Redirect to payment success page
                return redirect('payment_success')

            except Exception as e:
                messages.error(request, 'Payment failed or email could not be sent. Please try again later.')
                print(e)
                return redirect('payment_page')

    return render(request, 'paymentpage.html', {'cart_items': cart_items, 'total_price': total_price})

# Payment Success page view
@login_required
def payment_success(request):
    return render(request, 'payment_success.html')

def home(request):
    try:
        categories = Categories.objects.all()  # Fetch all categories from the database
    except Exception as e:
        categories = []  # Return an empty list in case of error
        print(f"Error fetching categories: {e}")

    # Render the template with categories
    return render(request, 'index.html', {'categories': categories})