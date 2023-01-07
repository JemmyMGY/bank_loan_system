# bank_loan_system
This is the source code of loan requester task 

# Features  

## Customer:
- You will have many customers who can sign up.
Each customer will login and can create many loans.
- The customer will enter the parameters of the desired loan.
- Customers can only enter the amount and the term of loan in years, and then he will be able to see the amortisation 
- The customer can then apply for the loan.
- The status of the application should be pending. 
- ### My Status : **Done**

## Admin:
- Admin user can 
1. See the pending applications 
2. Approve the loan.
- The loan status becomes approved.
- Then the customer can see it.

- ### My Status : **Done**

# Notes
- I have used Pure django v4.1 without using django rest as a beginner i see that i should konw how the framework works and how the things operated/done under the hood 
- All requests are used by AnonymouseUser and i know that is not a production level but i really did my best to learn Django in this short period and maybe will do it if you need that but i will require more time and assume that we are using auth
- Regarding the past note, i make sure that the user is in our database to view the dashboard_page or the loan_request_page so we are not that bad as just our users can manipulate each other accounts XD (I Know that is not secure but for now i have to start in the Admin feature)   
- My loan generated sheet results don't exactly match the results in the [Provided sheet](https://docs.google.com/spreadsheets/d/1cqAqK4fVlMmggEUZNAT984QplJyf3-3O4w6nSvlvsw4/edit#gid=0) but this may be an accuracy difference as i did **reverse engineering** to know the name of used functions and utilized the **numpy_financial** library ones which may be not the same as used in the sheet, i only suspect that but we may argue  

- i know that there would be a lot of best practices but as my approach to solve the task is **first get things done, then optimise later**

# Try the app
## Admin
- log in page url is **[localhost:8000/bank_admin]**, there is one admin right now with 
    - **email: *admin@tryd.com***
    - **password: 05012023**

## User
- For user log in page, just hit the **[localhost:8000]** you may find many users registered for testing purpose, for example [*memo@gmail.com*, *mo.gamal.yousseef@gmail.com*] and all users have the same **[password = 123456789]**, but for sure you can make your own account by clicking on **Create new account**. 


# To be added Features 

1. Authentication for Users and Admin also, as my app would redirect to User's loan dashboard as long as you hit the loans dash board url with the user email kwarg 
2. Improve the code quality and use the rest framework to just use the pre-made components which are definitely well tested and more functional instead of handling every thing on my own code
3. For sure the UI is just django template + some CSS and this might be replaced by UI framework like **React.js, Vue.js** and so on, so again we can use the pre-made components and great UI and get away from the headache of handling every single point. **[note: i'm not that good in UI, UX and never worked with such frameworks before]**
4. Deploy the app to the production line by any provided host  