# Overview

This is my application for the capstone project of CS50W. This application uses Django on the back end and in the front end I use HTML/CSS, Bootstrap and Javascript. 

In this application the user has to register and login on the website. After that the user can make bankaccounts and put some money on it to start. It is also possible for a user to create a shared account with another user, both users have access to the account and can make transactions with it.

The user can make transactions between different bank accounts. These transaction can be between accounts from the same user or from a different user. It is also possible to make deposits to an account. But it is not possible to have a transaction from and to the same account. This way the user can get new money in his account to make new transactions again.

# Distinctiveness and Complexity

I think my project satisfies the distinctiveness and complexity requirement. The application uses Django on the back end and has 3 data models. It also includes Javascript on the front-end. My website is also mobile responsive because all the pages will shrink according to the size of the device. The header also changes into a fold-out menu if the screen is too small to have it displayed normally. In the project I also use all the programming languages that are used in the course. In this project I also used new concepts like the Group by in the HTMl Template and new Javascript functions and events. I also used Bootstrap to make the header and all the forms.

I think the project is also destinctive enough from the other projects in this course. This is because with this project I had to build it from scratch. You also had to come up with the idea and the design for the website yourself. That's why I found this a very interesting project to make!

# File contents:

## Front End:

The front end of the website contains HTML, CSS, Bootstrap and Javascript files.
- ./statics/bank:
    - index.js:
        - The Javascript code in this file adds event listeners to every account. When you click on the account you will be send to the account page where you can see all the transactions.
    - account.js:
        - In this file the Javascript code puts event listeners on every transaction to fold out the extra information.
    - create_account.js:
        - The Javascript code in this file hides or shows the menu to select another user to create a shared bank account.
    - transactions.js:
        - When the user selects an account in the dropdown menu, the code in this file loads in the additional information of that account. It does it for the sender and also the receiver of the transaction.
    - layout.js:
        - When the user is on a mobile device and the header doesn’t fit then the Javascript in this file makes the button for the dropdown menu work.
    - style.css:
        - The CSS in this file is for the formatting of all the pages on the website.
    - Icon.png:
        - This is the picture that is visible as an icon in the tablet.
    - Logo.png:
        - This is the logo that I use in the header of the website.
- ./statics/templates/bank:
    - layout.html:
        - HTML template for the header of every page.
    - index.html:
        - HTML template for the index page.
    - account.html:
        - HTML template for every bank account.
    - create_account.html:
        - HTML template for creating an account page.
    - login.html:
        - HTML template for the login page.
    - register.html:
        - HTML template for the register page.
    - transaction.html:
        - HTML template for the page where you can create transactions.

## Back End:

The back end of the website contains the following files:  init,py, admin.py, apps.py, models.py, test.py, urls.py and views.py.

I made the following models:
- User:
    - This is the model to save the data of every user that makes an account on this website. This model extends the Abstractuser model.
- Bankaccount:
    - This model saves the data of every bank account that a user makes.
- Transaction:
    - This model saves the data of every transaction that is made between bank accounts.

# Instructions

- python manage.py makemigrations bank
- python manage.py migrate
- python manage.py runserver