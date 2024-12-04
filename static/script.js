function loginpage(){
    window.location.href = "login/";
}
function homepage(){
    window.location.href = "/home/";
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
document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.getElementById('menuIcon');
    const navbarMenu = document.querySelector('.navbar ul');

    menuIcon.addEventListener('click', () => {
        navbarMenu.classList.toggle('active');
    });
});


// Get the menu icon and navbar elements
const menuIcon = document.querySelector('.ri-menu-line');  // Menu icon
const navbarMenu = document.querySelector('.navbar ul');   // Navbar list

// Add a click event listener to the menu icon
menuIcon.addEventListener('click', function() {
    // Toggle the 'active' class to show/hide the menu
    navbarMenu.classList.toggle('active');
});

// Optional: Close the menu if a menu item is clicked (for single-page apps)
const menuItems = document.querySelectorAll('.navbar ul li a');
menuItems.forEach(item => {
    item.addEventListener('click', function() {
        navbarMenu.classList.remove('active');  // Hide the menu after clicking a link
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
