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
const menuIcon = document.getElementById('menuIcon');
const navbarMenu = document.querySelector('.navbar ul');

menuIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('active');
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
document.addEventListener("DOMContentLoaded", function() {
    // This ensures that the DOM is loaded before we try to update the cart count
    fetchCartCount();
  });
  
  function fetchCartCount() {
    fetch('/cart/count')
      .then(response => response.json())
      .then(data => {
        updateCartCount(data.count);
      })
      .catch(error => {
        console.error("Error fetching cart count:", error);
      });
  }
  
  function updateCartCount(count) {
    const cartCountElement = document.getElementById('cart-count');
    
    if (cartCountElement) {
      cartCountElement.textContent = count;
    } else {
      console.error("Cart count element not found");
    }
  }
  