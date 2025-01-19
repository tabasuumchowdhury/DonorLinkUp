function changeButtonColor()
{
    
}
document.querySelector('interest-button').addEventListener('click', function() {
    this.classList.toggle("clicked");
  });

let names = [];
let emails = [];
let hometowns = [];

async function submitSignup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const hometown = document.getElementById("hometown").value;
    const messageEmpty = document.getElementById("emptyField");
    const messageEmail = document.getElementById("invalidEmail");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    messageEmpty.style.display ="none";
    messageEmail.style.display ="none";

    if (!name || !email || !hometown) {
        messageEmpty.style.display = "block";
    }
    else if(!emailRegex.test(email)){
        messageEmail.style.display = "block";
    }
    else{
        names.push(name);
        emails.push(email);
        hometowns.push(hometown);
        window.location.href="interests.html";
    }
}

function passToPython()
{
    return (names, emails, hometowns)
}

function saveTarget() {
    const donationAmount = document.getElementById('donation-amount').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const frequency = document.getElementById('frequency').value;
    const messageEmpty = document.getElementById("emptyField");
    const amountError = document.getElementById('amount');
    const dateError = document.getElementById('dates');
    const dateOrder = document.getElementById('dateOrder');

    messageEmpty.style.display="none";
    amountError.style.display="none";
    dateError.style.display="none";
    dateOrder.style.display="none";

    if (!donationAmount || !startDate || !endDate || !frequency) {
        messageEmpty.style.display = "block";
    }
    else if (!donationAmount || isNaN(donationAmount) || donationAmount <= 0) {
        amountError.style.display = "block";
    }
    else if (!startDate || !endDate) {
        dateError.style.display = "block";
        return;
    }

    const start = new Date(startDate);
    const end = new Date(endDate);
    if (end <= start) {
        dateOrder.style.display = "block";
    }
}