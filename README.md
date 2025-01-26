
# Project Management API

This is a project management API built using Django and Django Rest Framework (DRF). It provides functionalities to manage projects, tasks, and users, and allows users to create, update, and manage tasks within various projects. This API is designed to be used in project management applications, where users can track the progress of tasks, assign tasks to team members, and manage project deadlines.

## Features

- **User Authentication:** Secure user authentication using JWT tokens.
- **Project Management:** Create and manage projects.
- **Task Management:** Create and manage tasks within projects, assign tasks to users, and track their status.
- **Task Status:** The status of tasks can be updated to "To Do", "In Progress", or "Done".

## Installation
## Step 1:
Clone the repository:

```bash
  git clone https://github.com/Sohail342/Project-Management-Tool.git

```


## Step 2:
Set up the virtual environment:

```bash
python -m venv .venv

```
Activate the virtual environment:
- On Windows:
```bash
.venv\Scripts\activate

```
- On macOS/Linux:
```bash
source .venv/bin/activate

```


## Step 3:
Install dependencies 
```bash
pip install -r requirements.txt

```

## Step 4:
Apply migrations

```bash
  python manage.py migrate

```
## Step 5:
Create a superuser (Optional)

```bash
  python manage.py createsuperuser

```
## Step 6:
Run Local Server

```bash
  python manage.py runserver

```

### API Endpoints Overview



| Endpoint               | Method | Description                        | Authentication |
|------------------------|--------|------------------------------------|------------|
| `/api/user/register/`           | POST   | Register a new user | No        |
| `/api/user/login/`   | POST   | Log in a user and get JWT tokens       | No        |
| `/api/users/`           | GET   | Get the authenticated user's Detail | Yes (JWT)        |
| `/api/users/<id>/`           | GET   | Get Specific authenticated user Detail | Yes (JWT)        |
| `/api/users/<id>/`           | DELETE   | Delete Specific authenticated user  | Yes (JWT)        |
| `/api/users/<id>/`           | PUT   | Update Specific authenticated user Details| Yes (JWT)        |
| `/api/users/<id>/`           | PATCH   | Update Specific authenticated user field | Yes (JWT)        |
| `/api/projects/`           | GET   | Get all projects| Yes (JWT)        |
| `/api/projects/`           | POST   | Create new project | Yes (JWT)        |
| `/api/projects/<id>/`           | DELETE   | Delete Specific project | Yes (JWT)        |
| `/api/projects/<id>/`           | PUT   | Update Specific project details | Yes (JWT)        |
| `/api/projects/<id>/`           | PATCH   | Update Specific project field | Yes (JWT)        |
| `/api/projects/<project_id>/tasks/`           | GET   | Get all tasks associated with specific project  | Yes (JWT)        |
| `/api/projects/<project_id>/tasks/`           | POST   | Create new task and assign it to a specific project  | Yes (JWT)        |
| `/api/tasks/<task_id>/comments/`           | POST   | Create new comment and assign it to a specific task  | Yes (JWT)        |
| `/api/tasks/<task_id>/comments/`           | GET   | Get all comments associated with specific task  | Yes (JWT)        |

### API Endpoints 

- **/api/user/register/ (POST)**
This endpoint is used for user registration. When a user sends a POST request with necessary details (such as username, password, etc.), a new user is created in the system. No authentication is required for this endpoint, as it is open for new users to sign up.

- **/api/user/login/ (POST)**
The login endpoint allows a registered user to log in by submitting their username and password. If the credentials are correct, the API responds with a JWT token that can be used for subsequent authenticated requests. No authentication is required here since this is the login process.

- **/api/users/ (GET)**
This endpoint retrieves the details of the authenticated user. The user must be logged in and provide a valid JWT token in the request header. This will return the user’s profile information such as username, email, etc.

- **/api/users/<id>/ (GET)**
This endpoint fetches the details of a specific user identified by their unique id. The request requires a valid JWT token for authentication, ensuring that only authorized users can view other users' information.

- **/api/users/<id>/ (DELETE)**
This endpoint allows an authenticated user (with a valid JWT token) to delete a specific user by their id. Only users with appropriate authorization (like an admin or the user themselves) can perform this action.

- **/api/users/<id>/ (PUT)**
The PUT request to this endpoint is used to update the details of a specific user identified by their id. It requires authentication via JWT and will allow modifying fields such as username, email, etc. The request body should contain the updated information for the user.

- **/api/users/<id>/ (PATCH)**
Similar to the PUT method, the PATCH request is used to update a specific field of a user, identified by their id. This is a partial update, meaning you only need to send the fields that need to be updated, not the entire user object. JWT authentication is required.

- **/api/projects/ (GET)**
This endpoint retrieves a list of all projects. The request needs to be authenticated with a valid JWT token. It will return a collection of project details that the authenticated user has access to.

- **/api/projects/ (POST)**
The POST method at this endpoint allows an authenticated user to create a new project. The user must provide project details in the request body. JWT authentication is required, and the user must have the appropriate permissions to create a project.

- **/api/projects/<id>/ (DELETE)**
This endpoint allows a user to delete a specific project by its id. The user needs to be authenticated with a valid JWT token and must have sufficient privileges (e.g., project owner or admin) to delete the project.

- **/api/projects/<id>/ (PUT)**
The PUT request allows for updating the details of a specific project. The request must include a valid JWT token for authentication. The request body should contain the updated project data, and only authorized users can modify the project.

- **/api/projects/<id>/ (PATCH)**
This endpoint is used for partially updating the details of a specific project identified by its id. It requires JWT authentication and allows for the modification of specific fields, such as project name, description, or deadline.

- **/api/projects/<project_id>/tasks/ (GET)**
This endpoint retrieves a list of tasks associated with a specific project identified by project_id. JWT authentication is required, and the response will include all tasks related to the specified project.

- **/api/projects/<project_id>/tasks/ (POST)**
The POST method here allows authenticated users to create a new task and associate it with a specific project identified by project_id. The request body should contain task details such as title, description, priority, etc., and JWT authentication is required.

- **/api/tasks/<task_id>/comments/ (POST)**
This endpoint allows users to create a new comment on a specific task identified by task_id. The comment can provide feedback, clarification, or updates related to the task. Authentication via JWT is required.

- **/api/tasks/<task_id>/comments/ (GET)**
This GET request retrieves all comments associated with a specific task. Users must authenticate with a valid JWT token to access the task’s comment data, and the response will include all the comments for the specified task.







## Contact
If you have any questions or feedback, feel free to reach out:
<p align="left">
<a href="https://wa.me/+923431285354" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>


