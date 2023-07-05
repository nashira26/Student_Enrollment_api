# Enrollment Funnel API Documentation

## 1. Get list of Funnel statuses
- Endpoint : 'funnelstatus/'
- Method : GET
- Description : Retrieve the list of all funnel statuses.

**Response body:**
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
- Endpoint : 'funnelstatus/create/'
- Method : POST
- Description : Create a new funnel status.

## 3. Get a Funnel status
- Endpoint : 'funnelstatus/<status_id>/'
- Method : GET
- Description : Retrieve an existing funnel status.

**Response body:**
````json
{
    "id": 1,
    "name": "Applied",
}
````

## 4. Update a Funnel status
- Endpoint : 'funnelstatus/<status_id>/update/'
- Method : PUT
- Description : Update an existing funnel status.

**Response body:**
````json
{
    "id": 1,
    "name": "Application Accepted",
}
````

## 5. Delete a Funnel status
- Endpoint : 'funnelstatus/<status_id>/delete/'
- Method : DELETE
- Description : Delete an existing funnel status.

**Response body:**
````json
{}
````

## 6. Create new Student
- Endpoint : 'student/create/'
- Method : POST
- Description : Create a new student.

## 7. Get a Student
- Endpoint : 'student/<student_id>/'
- Method : GET
- Description : Retrieve an existing student.

**Response body:**
````json
{
    "id": 1,
    "name": "Harry",
    "status": "Interviewed"
}
````

## 8. Update a Student
- Endpoint : 'student/<student_id>/update/'
- Method : PUT
- Description : Update an existing student.

## 9. Delete a Student
- Endpoint : 'student/<student_id>/delete/'
- Method : DELETE
- Description : Delete an existing student.

## 10. Retrieve 50 latest logs
- Endpoint : 'logs/'
- Method : GET
- Description : Retrieve 50 latest logs with pagination.

**Response body:**
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

**Example error responses**

### Example 1:
Using the wrong request method.
```json
HTTP 405 Method Not Allowed
Content-Type: application/json

{
    "detail": "Method \"GET\" not allowed."
}
```

### Example 2:
Requested data is not available in the database.
```json
HTTP 404 Not Found
Content-Type: application/json

{
    "error": "Resource not found", 
    "message" : "The requested resource does not exist."
}

```

### Example 4:
Malformed syntax or invalid parameters.
```json
HTTP 400 Bad request
Content-Type: application/json

{
    "status": [
        "Object with name=Declined does not exist."
    ]
    
}