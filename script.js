document.querySelector('interest-button').addEventListener('click', function() {
    this.classList.toggle("clicked");
  });

  async function submitSignup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const hometown = document.getElementById("hometown").value;
    const message = document.getElementById("emptyField");

    if (!name || !email || !hometown) {
        message.style.display = "block";
    }
    else{
        window.location.href="interests.html";
    }
}
