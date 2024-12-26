# CAT Task

## 📝Table of Contents

- [API Documentation](#-api-documentation)
  - [📝Overview](#overview)
  - [🔗Endpoints](#endpoints)
    - [User Endpoints](#user-endpoints)
    - [Authentication Endpoints](#authentication-endpoints)
  - [📊Pagination](#pagination)
  - [⏳Throttling](#throttling)
- [Problem Solving](#problem-solving)

## 📚 API Documentation

### 📝Overview

---

This API provides endpoints for user management and authentication. It includes functionalities for registering users, retrieving user details, and handling authentication using JWT tokens.

### 🔗Endpoints

---

#### User Endpoints

| Description          | Role       | Method | Endpoint                | Response Message |
|----------------------|------------|--------|-------------------------|------------------|
| Register a new user  | Public     | POST   | `/api/auth/register`    | User details     |
| Get, update, or delete a user by ID | Admin/Owner | GET, PUT, DELETE | `/api/users/<int:pk>` | User details     |

- **Details:**

  - **Register a new user**
    - **Request Message Parmeters:**

        | Parameter | Type   | Description          |
        |-----------|--------|----------------------|
        | username  | string | The user's username  |
        | email     | string | The user's email     |
        | password  | string | The user's password  |

    - **Response Message Structure:**

        ```json
        {
        "id": 1,
        "username": "example",
        "email": "example@example.com",
        "role": "client"
        }
        ```

  - **Get, update, or delete a user by ID**
    - **Response Message:**
      - **GET:** User details  
      - **PUT:** Updated user details
      - **PATCH:** Updated user details
      - **DELETE:** No content

      ```json
        {
        "id": 1,
        "username": "example",
        "email": "example@e.com",
        "role": "client"
        }
        ```

#### Authentication Endpoints

| Description          | Role       | Method | Endpoint                |
|----------------------|------------|--------|-------------------------|
| Obtain JWT token     | Public     | POST   | `/api/auth/login`       |
| Refresh JWT token    | Public     | POST   | `/api/auth/refresh`     |

- **Details:**
  - **Obtain JWT token**
    - **Request Message Parmeters:**

        | Parameter | Type   | Description          |
        |-----------|--------|----------------------|
        | username  | string | The user's username  |
        | password  | string | The user's password  |

    - **Response Message:**

        ```json
        {
        "refresh": "string",
        "access": "string"
        }
        ```

  - **Refresh JWT token**
    - **Request Message Parmeters:**

        | Parameter | Type   | Description          |
        |-----------|--------|----------------------|
        | refresh   | string | The refresh token    |

    - **Response Message:**

        ```json
        {
        "access": "string",
        "refresh": "string"
        }
        ```

### 📊Pagination

---

The Users endpoint supports pagination to limit the number of items returned in a single response. The default page size is 10 items per page.

- **Response Message Structure:**

    ```json
    {
        "count": 100,
        "next": "127.0.0.1:8000/api/users/?page=2",
        "previous": "127.0.0.1:8000/api/users/?page=1",
        "results": [
            {
                "id": 1,
                "username": "example",
                "email": "example@example.com",
                "role": "client"
            },
            // More items...
        ]
    }
    ```

| Field     | Type   | Description                          |
|-----------|--------|--------------------------------------|
| count     | int    | Total number of items available      |
| next      | string | URL to the next page of items        |
| previous  | string | URL to the previous page of items    |
| results   | array  | List of items on the current page    |

### ⏳Throttling

---

To ensure fair usage and prevent abuse, the API implements throttling. The default rate limits are:

- **Anonymous users:** 5 requests per minute
- **Authenticated users:** 10 requests per minute

If the rate limit is exceeded, the API will return a `429 Too Many Requests` status code with the following response:

- **Response Message Structure:**

    ```json
    {
        "detail": "Request was throttled. Expected available in 60 seconds."
    }
    ```

| Field     | Type   | Description                          |
|-----------|--------|--------------------------------------|
| detail    | string | Message indicating the throttle limit and retry time |

## Problem Solving
