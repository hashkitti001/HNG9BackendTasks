```markdown
# Person API Documentation

This documentation provides information on how to use the Person API.

## Base URL

The base URL for all API endpoints is:

```
http://127.0.0.1:5000
```

Replace this with the appropriate base URL if you deploy the API to a different server.

## Endpoints

### Create a New Person

- **URL:** `/persons`
- **Method:** `POST`
- **Description:** Create a new person record.

#### Request Body

```json
{
    "name": "John Doe",
    "age": 30
}
```

- Both "name" and "age" fields are required.

#### Response

- Status Code: `201 Created`

```json
{
    "message": "Person created successfully"
}
```

### Retrieve, Update, or Delete a Person

- **URL:** `/persons/<string:name>`
- **Method:** `GET`, `PUT`, `DELETE`
- **Description:** Retrieve, update, or delete a person record by name.

#### Retrieve a Person

- **Method:** `GET`

#### Response

- Status Code: `200 OK`

```json
{
    "name": "John Doe",
    "age": 30
}
```

- If the person is not found:

  - Status Code: `404 Not Found`

  ```json
  {
      "error": "Person not found"
  }
  ```

#### Update a Person

- **Method:** `PUT`

#### Request Body

```json
{
    "age": 35
}
```

- "age" field is required for updating.

#### Response

- Status Code: `200 OK`

```json
{
    "message": "Person updated successfully"
}
```

- If the person is not found:

  - Status Code: `404 Not Found`

  ```json
  {
      "error": "Person not found"
  }
  ```

- If the "age" field is missing:

  - Status Code: `400 Bad Request`

  ```json
  {
      "error": "Age is required for updating"
  }
  ```

#### Delete a Person

- **Method:** `DELETE`

#### Response

- Status Code: `200 OK`

```json
{
    "message": "Person deleted successfully"
}
```

- If the person is not found:

  - Status Code: `404 Not Found`

  ```json
  {
      "error": "Person not found"
  }
  ```

- Note: Replace `<string:name>` in the URL with the actual name of the person you want to retrieve, update, or delete.

This documentation provides the basic usage of the Person API. You can make HTTP requests to the specified endpoints to interact with the API and manage person records in the SQLite database.
```

This Markdown documentation outlines the API's endpoints, request and response formats, and expected status codes. You can expand on this documentation by adding more details, explanations, and examples as needed.