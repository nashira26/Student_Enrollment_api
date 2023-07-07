# Enrollment Funnel API Documentation

## 1. Get list of Funnel statuses
- Endpoint : GET '/funnelstatus/all/'
- Method : GET
- Description : Retrieve the list of all funnel statuses.

### Example:
**Response body**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "statuses": [
        {
            "id": 1,
            "name": "Applied"
        },
        {
            "id": 2,
            "name": "Application accepted"
        },
        {
            "id": 3,
            "name": "Interviewed"
        },
        {
            "id": 4,
            "name": "Offered"
        }
    ]
}
````

## 2. Create new Funnel status
- Endpoint : POST '/funnelstatus/'
- Method : POST
- Description : Create a new funnel status.

### Example
**Request body:**
- POST '/funnelstatus/'
- Content-Type: application/json
````json
{
    "name": "Application Accepted",
}
````
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 2,
    "name": "Application Accepted",
}
````

## 3. Get a Funnel status
- Endpoint : GET '/funnelstatus/<status_id>/'
- Method : GET
- Description : Retrieve an existing funnel status.

### Example
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 1,
    "name": "Applied",
}
````

## 4. Update a Funnel status
- Endpoint : PUT '/funnelstatus/<status_id>/'
- Method : PUT
- Description : Update an existing funnel status.

### Example
**Request body:**
- PUT '/funnelstatus/1/'
- Content-Type: application/json
````json
{
    "name": "Application Accepted",
}
````
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 1,
    "name": "Application Accepted",
}
````

## 5. Delete a Funnel status
- Endpoint : DELETE '/funnelstatus/<status_id>/'
- Method : DELETE
- Description : Delete an existing funnel status.

**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{}
````

## 6. Create new Student
- Endpoint : POST '/student/'
- Method : POST
- Description : Create a new student.

### Example
**Request body:**
- POST '/student/'
- Content-Type: application/json
````json
{
    "name": "Harry",
}
````
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 1,
    "name": "Harry",
    "status": "Applied"
}
````

## 7. Get a Student
- Endpoint : GET '/student/<student_id>/'
- Method : GET
- Description : Retrieve an existing student.

### Example
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 1,
    "name": "Harry",
    "status": "Interviewed"
}
````

## 8. Update a Student
- Endpoint : PUT '/student/<student_id>/'
- Method : PUT
- Description : Update an existing student's details.

### Example
**Request body:**
- PUT '/student/1/'
- Content-Type: application/json
````json
{
    "name" : "Henry",
    "status": "Application Accepted"
}
````
**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
{
    "id": 1,
    "name": "Henry",
    "status": "Application Accepted"
}
````

## 9. Retrieve 50 latest logs
- Endpoint : GET '/logs/'
- Method : GET
- Description : Retrieve 50 latest logs with pagination.

**Response body:**
- Status code: HTTP 200 OK
- Content-Type: application/json
````json
[
    {
        "id": 8,
        "student_name": {
            "id": 7,
            "name": "Ron",
            "status": "Application accepted"
        },
        "status_before": {
            "id": 1,
            "name": "Applied"
        },
        "status_after": {
            "id": 2,
            "name": "Application accepted"
        },
        "timestamp": "2023-07-05T13:49:20.575719Z"
    },
    {
        "id": 7,
        "student_name": {
            "id": 8,
            "name": "Hermoine",
            "status": "Application accepted"
        },
        "status_before": {
            "id": 1,
            "name": "Applied"
        },
        "status_after": {
            "id": 2,
            "name": "Application accepted"
        },
        "timestamp": "2023-07-05T12:59:53.698353Z"
    }
]

````
## Error Responses

If an error occurs, API will respond with an error message in JSON format and will contain following fields.

**Example 1:**
Using the wrong request method.

- Status code: HTTP 405 Method Not Allowed
- Content-Type: application/json

### Example
```json
{
    "detail": "Method \"GET\" not allowed."
}
```

**Example 2:**
Requested data is not available in the database.

- Status code: HTTP 404 Not Found
- Content-Type: application/json
```json
{
    "error": "Resource not found", 
    "message" : "The requested resource does not exist."
}

```

**Example 3:**
Malformed syntax or invalid parameters.

- Status code: HTTP 400 Bad request
- Content-Type: application/json

### Example
```json
{
    "status": [
        "Object with name=Declined does not exist."
    ]   
}
