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
