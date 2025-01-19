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
    messageEmpty.style.display ="none";
    messageEmail.style.display ="none";

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

const selectedInterests = new Set();

function toggleSelection(button) {
    const interest = button.textContent.trim();
    if (selectedInterests.has(interest)) {
        selectedInterests.delete(interest);
        button.classList.remove('selected');
    } else {
        selectedInterests.add(interest);
        button.classList.add('selected');
    }
}

function submitSignup() {
    const selectedArray = Array.from(selectedInterests);
    console.log("Selected interests:", selectedArray);
    alert("Your selections have been saved:\n" + selectedArray.join(", "));
}