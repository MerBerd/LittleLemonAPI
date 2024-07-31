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

**Menu-items endpoints**

|**Endpoint**|**Role**|**Method**|**Purpose**|
|------------|--------|----------|-----------|
|/api/menu-items |Customer, delivery crew|GET|Lists all menu items. Return a 200 – Ok HTTP status code|
|/api/menu-items|Customer, delivery crew|POST, PUT, PATCH, DELETE|Denies access and returns 403 – Unauthorized HTTP status code|
|/api/menu-items/{menuItem}|Customer, delivery crew|GET|Lists single menu item|
|/api/menu-items/{menuItem}  |Customer, delivery crew|POST, PUT, PATCH, DELETE|Returns 403 - Unauthorized|
|/api/menu-items  |Manager|GET|Lists all menu items|
|/api/menu-items  |Manager|POST|Creates a new menu item and returns 201 - Created|
|/api/menu-items/{menuItem}  |Manager|GET|Lists single menu item|
|/api/menu-items/{menuItem}  |Manager|PUT, PATCH|Updates single menu item|
|/api/menu-items/{menuItem}  |Manager|DELETE|Deletes menu item|
