function loginpage(){
    window.location.href = "login/";
}
function homepage(){
    window.location.href = "home/";
}
function registerpage(){
    window.location.href= "/register/";
}
function loginpage1(){
    window.location.href = '/';
}

function productspage(){
    window.location.href = '/products/'
}
function aboutuspage(){
    window.location.href = '/aboutus/'
}
function contactuspage(){
    window.location.href = '/contactus/'
}

// document.getElementById('payNowButton').addEventListener('click', function() {
//     document.getElementById('paymentOptions').style.display = 'block';
// });
document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menuIcon');
    const navbarMenu = document.querySelector('.navbar ul');

    menuIcon.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent immediate bubbling issues
        navbarMenu.classList.toggle('active'); // Toggle the menu visibility
    });

    document.addEventListener('click', function(event) {
        if (!navbarMenu.contains(event.target) && !menuIcon.contains(event.target)) {
            navbarMenu.classList.remove('active'); // Close the menu if clicked outside
        }
    });
});



// AJAX call to update the cart item count
function updateCartCount() {
    fetch('/cart/count/')
        .then(response => response.json())
        .then(data => {
            // Update the cart button with the new cart item count
            const cartButton = document.querySelector('.btn-secondary');
            cartButton.textContent = `View Cart (${data.cart_item_count})`;
        })
        .catch(error => console.error('Error fetching cart count:', error));
}

// Call this function on page load to update the cart count
document.addEventListener('DOMContentLoaded', function () {
    updateCartCount(); // Update the cart count on page load (in case there are already items in the cart)
});

// AJAX call to update the cart item count
function updateCartCount() {
    fetch('/cart/count/') // Fetch updated cart count from your server
        .then(response => response.json())
        .then(data => {
            const cartButton = document.querySelector('.btn-secondary');
            cartButton.textContent = `View Cart (${data.cart_item_count})`;
        })
        .catch(error => console.error('Error fetching cart count:', error));
}

// Handle the form submission for adding an item to the cart
document.querySelectorAll('.add-to-cart-form').forEach(form => {
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(this); // Create FormData from the form
        fetch(this.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value // Include CSRF token
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // After the item is successfully added to the cart, update the cart item count
                updateCartCount();
            } else {
                console.error('Error adding to cart:', data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

// Optionally, update the cart count on page load
document.addEventListener('DOMContentLoaded', function () {
    updateCartCount();
});
