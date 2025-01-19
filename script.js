function changeButtonColor()
{
    
}
document.querySelector('interest-button').addEventListener('click', function() {
    this.classList.toggle("clicked");
  });

async function submitSignup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const hometown = document.getElementById("hometown").value;
    const messageEmpty = document.getElementById("emptyField");
    const messageEmail = document.getElementById("invalidEmail");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!name || !email || !hometown) {
        messageEmpty.style.display = "block";
    }
    else if(!emailRegex.test(email)){
        messageEmail.style.display = "block";
    }
    else{
        window.location.href="interests.html";
    }
}