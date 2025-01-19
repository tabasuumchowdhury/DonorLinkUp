# mcwicshacks

## 1.1 What your project does
### Briefly describe the purpose and functionality of your project. You can also talk about the goal of your project and the inspiration behind it.
"Be the change you want to see in the world". Many people follow this mantra and wish to help others by donating to charities. But then the struggle arises: How do I find the right charity for me? With Donor Link Up its never been any easier to be a better person. Simply create an account and choose your area of interest and where you would like to donate. This "tinder-fied" website allows you to click right or left to choose between different charities! You're able to check how much you've donated and goals that have been met. 

## 1.2How you built your project
### Explain the technologies, tools, and frameworks you used, along with a high-level overview of the architecture and design.

Firstly, we gathered the data from a Canadian government official website "open.canada.ca". C was used to replace certain columns with a different value, for instance the category which was once just numbers was replaced by the value each number represented. 

Then, we used the pandas library in python to parse through the data and an OOP approach to save each charity from the csv file into an object in an array of charities. The principle of polymorphism, allowed a 'Person' class to encapsulate each users information like their name, interests and the city where they would want to donate. A function goes through the array of charities and creates a new array with only the recommended charities for the user based on their filters. 

Libraries like Flash and Json allowed the backend to connect to the front end and javascript code, helping transmit data from the user into the python code and vice-versa. Using figma and canva, our website plan and logo was first designed. Then, using HTML and CSS the actual website was implemented.
**Add architecture and design**

## 1.3 How your project works
### This could be the demo portion of the presentation, where you guide the judges through how a user would interact with and utilize your project.
**demo**

## 1.4 Next steps for your project
### If you had additional time and resources, what enhancements or features would you have added to your project to make it better?
Firstly, we want to make the website mobile-friendly and develop an IOS app. Then, we want to upgrade the security of the login page by adding a password or a two-factor authentication. 

Animation would be added to the application with a tree growing as more money was being donated like a "money tree". Moreso, it would not be an application reserved for charity but it would also display volunteering opportunies and have a social aspect. Users would be able to share their kind acts (i.e. posts with captions) in hopes of encouraging their friends and families to join and also donate/volunteer. We wish to foster a community motivated to do better. 
