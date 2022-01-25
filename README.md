![EpicEvents](EpicEventsPreview.jpg)

# EPIC EVENTS CRM 

## **Description**

This application is a customer relationship manager build for EpicEvents
 society. 
 This app will ease the management of client's data, contracts and events.


## **Clone the repository**

Download the repository from this link to the local folder you want: 

``git clone https://github.com/MargueriteT/EpicEvents.git``

## **Installation**

First, make sure you already have python3 install on your computer. 
If not, please go to this link: https://www.python.org/downloads/ and follow the instructions. 
Open your Cmd and proceed as indicated:
  
Navigate to your repository folder: `cd path/to/your/folder`
    
Create a virtual environment: ``python -m venv env (windows) python3 -m venv env (macos ou Linux)``

Navigate to the EpicEvents folder : ``cd EpicEvents``

Activate this virtual environment: ``env\Scripts\activate (windows) ou source env/bin/activate (macos ou linux)``

Install project dependencies: ``pip install -r requirements.txt``

Navigate to EpicEvents app : ``cd EpicEvents/EpicEvents``

Create a new python file named configuration.py : ``copy con configuration.py``

Add the secret key to the file : ``SECRET_KEY = 'yoursecretkey'``

Go back to the EpicEvents folder : ``cd ..``

Create the database : ``python manage.py migrate``

Run the program: ``python manage.py runserver``

## **Connection to EpicEvents**

Go to the following url : http://127.0.0.1:8000/admin/
Enter the username and password you were given to connect to the CRM.
Your access will be restricted based on your status within the company.

## **EpicEvents API**

### Login

POST/admin/

API endpoint to log in. Two key must be passed in the body : 
- username, 
- password.

   
     successful request : http status 200 
     account doesn't exist or password error : http status 401
     missing field : http status 400

### Users list

GET/users/

API endpoint to access the user's list. This endpoint can be access only
 with a management status.
Token must be provided to access this page.

 
     successful request : http status 200 
     user status is not management  : http status 403
     no token : http status 401

### Create a new user

POST/users/

API endpoint to create a new user. This endpoint can be access only
 with a management status. Token must be provided. 
 
The user must provided :
- username
- first_name
- last_name
- email
- status
- password


    successful request : http status 201 
    no token : http status 401
    missing field : http status 400
    user status is not management  : http status 403

### User's details

POST/users/{user_id}/

API endpoint to access details on an user. This endpoint can be access only
 with a management status.
Token must be provided to access this page.

  
    successful request : http status 200 
    no token : http status 401
    non-existent user : http status 404
    user status is not management  : http status 403


### Update an user

PUT/users/{user_id}/

API endpoint to update details on an user. This endpoint can be access only
 with a management status.
Token must be provided to access this page. 

The user must provide some data to update:
- username
- first_name
- last_name
- email
- status
- password


    succesful request : http status 200 
    no token : http status 401
    non-existent user : http status 404
    user status is not management  : http status 403


### Delete an user

DELETE/users/{user_id}/

API endpoint to delete an user. This endpoint can be access only
 with a management status. 
Token must be provided to access this page.

    sucessful request : http status 204
    no token : http status 401
    non-existent user : http status 404
    user status is not management : http status 403
    
### Clients list

GET/clients/

API endpoint to access the clients's list. This endpoint is accessible
 regardless of status but user status will defined the specific restriction. 
 A manager can access any clients such as a seller, a support user however
  will only be able to access the clients is working for.
Token must be provided to access this page.

 
     successful request : http status 200 
     no token : http status 401

### Create a new client

POST/clients/

API endpoint to create a new client. The access to this endpoint is
 restricted to user with manager or seller status. Token must be provided. 
 
The user must provided :
- society_name
- number
- street
- zip_code
- city_name
- email
- phonenumber
- is_a_client
- sale_user (optional)


    successful request : http status 201 
    no token : http status 401
    missing field : http status 400
    user status is support  : http status 403

### Client's details

POST/clients/{client_id}/

API endpoint to access details on a client. This endpoint is accessible
 regardless of status but user' status will defined the specific restriction. 
 A manager can access any clients such as a seller, a support user however
  will only be able to access the clients is working for.
Token must be provided to access this page.

  
    successful request : http status 200 
    no token : http status 401
    non-existent client : http status 404


### Update a client

PUT/clients/{client_id}/

API endpoint to update details on a contract. The access to this endpoint is
 restricted to user with manager or seller status.
Token must be provided to access this page. 

The user must provide some data to update:
- society_name
- number
- street
- zip_code
- city_name
- email
- phonenumber
- is_a_client
- sale_user (optional)


    succesful request : http status 200 
    no token : http status 401
    non-existent client : http status 404
    user status is support  : http status 403


### Delete a client

DELETE/clients/{client_id}/

API endpoint to delete an client. The access to this endpoint is restricted 
to user with manager or seller status. Token must be provided to access this
 page.

    sucessful request : http status 204
    no token : http status 401
    non-existent client : http status 404
    user status is support : http status 403
    
    
### Contracts list

GET/contracts/

API endpoint to access the contracts's list. This endpoint can be access only
 with a management status or sale status : a manager can access to all
  contracts however a seller will have a restricted access (only to his own
   contracts).
Token must be provided to access this page.

 
     successful request : http status 200 
     user status is support  : http status 403
     no token : http status 401

### Create a new contract

POST/contracts/

API endpoint to create a new contract. This endpoint can be access only
 with a management status or sale status : a manager can create a new
  contract for any seller however a seller can only create a contract with
   him as sale_user. Token must be provided. 
 
The user must provided :
- title
- sale_user
- client
- content
- signed


    successful request : http status 201 
    no token : http status 401
    missing field : http status 400
    user status is support  : http status 403

### Contracts's details

POST/contracts/{contract_id}/

API endpoint to access details on a contract. This endpoint can be access only
 with a management status or sale status. Sellers can only access their own
  contracts however manager can access any contracts.
Token must be provided to access this page.

  
    successful request : http status 200 
    no token : http status 401
    non-existent contract : http status 404
    user status is support  : http status 403


### Update a contract

PUT/contracts/{contract_id}/

API endpoint to update details on a contract. This endpoint can be access only
 with a management status or sale status. Sellers can only update their own
  contracts however manager can update any contracts.
Token must be provided to access this page. 

The user must provide some data to update:
- title
- sale_user
- client
- content
- signed


    succesful request : http status 200 
    no token : http status 401
    non-existent contract : http status 404
    user status is support  : http status 403


### Delete a contract

DELETE/contracts/{contract_id}/

API endpoint to delete an user. This endpoint can be access only
 with a management status or sale status. Sellers can only delete their own
  contracts however manager can delete any contracts.
Token must be provided to access this page.

    sucessful request : http status 204
    no token : http status 401
    non-existent contract : http status 404
    user status is support : http status 403
    
### Events list

GET/events/

API endpoint to access the events's list. This endpoint is accessible
 regardless of status but user' status will defined the specific restriction. 
 A manager can access any events however support or sale user will only be able
  to access the events they're linked with.
Token must be provided to access this page.

 
     successful request : http status 200 
     no token : http status 401

### Create a new event

POST/events/

API endpoint to create a new event. This endpoint can be access only
 with a management status or sale status : a manager can create a new
  event for any seller however a seller can only create an event with
   him as sale_user. Token must be provided. 
 
The user must provided :
- event_title
- contract
- type
- event_date
- sale_user
- support_user (optional)


    successful request : http status 201 
    no token : http status 401
    missing field : http status 400
    user status is support  : http status 403

### Events's details

POST/events/{event_id}/

API endpoint to access details on an event. This endpoint is accessible
 regardless of status, but user' status will defined the specific restriction. 
 A manager can access any events however support or sale user will only be able
  to access the events they're linked with.
Token must be provided to access this page.

  
    successful request : http status 200 
    no token : http status 401
    non-existent contract : http status 404


### Update a event

PUT/events/{event_id}/

API endpoint to update details on a contract. This endpoint is accessible
 regardless of status, but user' status will defined the specific restriction. 
 A manager can update any events however support or sale user will only be able
  to update the events they're linked with.
Token must be provided to access this page. 

The user must provide some data to update:
- event_title
- contract
- type
- event_date
- sale_user
- support_user (optional)


    succesful request : http status 200 
    no token : http status 401
    non-existent contract : http status 404


### Delete an event

DELETE/events/{event_id}/

API endpoint to delete an user. This endpoint is accessible
 regardless of status, but user' status will defined the specific restriction. 
 A manager can delete any events however support or sale user will only be able
  to delete the events they're linked with.
Token must be provided to access this page.

    sucessful request : http status 204
    no token : http status 401
    non-existent contract : http status 404



    
## **Contributor**

Marguerite Teulon - as part of OpenClassrooms' Project 12:
Develop a secure back-end architecture using Django ORM