# LittleLemonAPI
LittleLemonAPI project (Meta API course on Coursera)


## **API endpoints**

Here are all the required API routes for this project grouped into several categories.

**User registration and token generation endpoints**

|**Endpoint**|**Role**|**Method**|**Purpose**|
|------------|--------|----------|-----------|
|/api/users  |No role required|POST|Creates a new user with name, email and password|
|/api/users/users/me/|Anyone with a valid user token|GET|Displays only the current user|
|/token/login/|Anyone with a valid username and password|POST|Generates access tokens that can be used in other API calls in this project|
