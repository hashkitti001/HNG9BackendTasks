## HNG Backend Task 2
### How to run the server
Pre-Requisites
Developers using this project should have Python 3 installed on their local machines
### Install Dependencies
- Flask - Follow instructions to install Flask in [https://flask.palletsprojects.com/en/2.1.x/] 
- SQLite3 - the sqlite3 module come preinstalled with any Python3 installation 
### Running the Server 
After installing Python3, in the root directory run the following commands to install the necessary dependencies and start the server
```bash
# Install Flask
pip install Flask
# Run the server
flask --app main.py
```
API endpoints 
`GET '/people'`
- Sample: `curl https://hng-backend-task1.vercel.app/persons/Abel Tesfaye`

```json
{
  age: 30,
  name: "Abel Tesfaye"
}
```
