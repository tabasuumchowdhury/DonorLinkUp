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

    if (!donationAmount || isNaN(donationAmount) || donationAmount <= 0) {
        alert("Please enter a valid donation amount (a positive number).");
        return;
    }
    else if (!startDate || !endDate) {
        alert("Please select both a start date and an end date.");
        return;
    }

    const start = new Date(startDate);
    const end = new Date(endDate);
    if (end <= start) {
        alert("End date must be after the start date. Please correct the dates.");
        return;
    }

    const diffTime = Math.abs(end - start);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    let donationPerPeriod;
    if (frequency === "day") {
        donationPerPeriod = donationAmount / diffDays;
    } else if (frequency === "week") {
        donationPerPeriod = donationAmount / (diffDays / 7);
    } else if (frequency === "month") {
        donationPerPeriod = donationAmount / (diffDays / 30);
    }

    alert(`Your target has been saved:\n\n` +
        `Donation Amount: ${donationAmount} CAD\n` +
        `Start Date: ${startDate}\n` +
        `End Date: ${endDate}\n` +
        `Timeline: ${diffDays} days\n` +
        `Donation Frequency: ${frequency}\n` +
        `Amount to donate per ${frequency}: ${donationPerPeriod.toFixed(2)} CAD`);
}