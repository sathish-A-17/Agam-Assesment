# Django User Management API

## Overview
### This project is a Django-based API for user management with JWT authentication and role-based access control. It includes features such as user registration, login, and admin functionalities for managing users.

## Features
  1.User Registration: Users can register with a unique email, username, and password.
  2.User Login: Authenticated users receive a JWT for session management.
  3.User Details: Retrieve and update details of the currently authenticated user.
  4.Admin Features: Admins can view and delete users.
  5.Swagger Documentation: Interactive API documentation.
  6.Postman Collection: Predefined API requests for testing.

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation Steps

### 1. Clone the repository:
   git clone https://github.com/sathish-A-17/UserManagement.git
### 2. Set Up a Virtual Environment
   - python -m venv venv
   - venv\Scripts\activate
### 3. Install Dependencies
   - pip install -r requirements.txt

### 4. Set Up Environment Variables
  Create a .env file in the root directory and add your environment variables.

### Run Migrations
    - python manage.py migrate
## Create a Superuser
### Create an initial admin user to access the Django admin panel:
    - python manage.py createsuperuser
### Run the Development Server
    - python manage.py runserver

## API Endpoints
#### The API will be available at http://127.0.0.1:8000/api/

### Register User
    URL: /api/register/
    Method: POST
    Request Body:
                  {
                "username": "string",
                "password": "string",
                "email": "string"
              }
### Login User
      URL: /api/login/
      Method: POST
      Request Body:
                {
                "username": "string",
                "password": "string"
                }
      Response:
      {
        "refresh": "string",
        "access": "string"
      }
### Get User Details
      URL: /api/user/
      Method: GET
      Headers:
          Authorization: Bearer <your-access-token>
### Update User Details
      URL: /api/user/
      Method: PUT
      Headers:
            Authorization: Bearer <your-access-token>
### Admin: View All Users
      URL: /api/admin/users/
      Method: GET
      Headers:
      Authorization: Bearer <your-access-token>
### Admin: Delete User
      URL: /api/admin/users/<user_id>/
      Method: DELETE
      Headers:
         Authorization: Bearer <your-access-token>
## API Documentation
#### The API is documented using Swagger. You can access the interactive documentation at: http://127.0.0.1:8000/api/swagger/
      


   
