const interestButtons = document.querySelectorAll('.interest-button');

interestButtons.forEach(function(button) {
    button.onclick = function() {
        button.classList.toggle('active');
    };
});