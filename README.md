LATE SHOW EPISODES API

Project Description
The Late Show Episodes API is a Flask-based web application designed to manage episodes, guests, and their appearances on a late-night show. The project offers functionality to create, read, update, and manage episodes, guest information, and guest appearances, allowing users to interact with this data through a RESTful API.

The project was built using Flask for rapid development and scalability. SQLite is used as the database engine, while SQLAlchemy handles ORM for database interactions.

The API provides various endpoints for accessing episode details, guests, and their appearances, making it easy to integrate into other applications or services.

Table of Contents
Project Structure
Installation and Setup
How to Use
Technologies Used
API Endpoints
License
Project Structure
bash
Copy code
Late_Show_API/
│
├── instance/
│   └── late_show-db/  # SQLite database
├── migrations/        # Alembic migrations
│   ├── versions/
│   ├── alembic.ini
│   ├── envy.py
│   ├── script.py.mako
├── app.py             # Main Flask application
├── models.py          # SQLAlchemy models (Episode, Guest, Appearance)
├── routes.py          # Web routes for rendering pages
├── seed_data.py       # Seed data for episodes and guests
├── guests.csv         # CSV file for guest data
├── Pipfile            # Pipenv for managing dependencies
├── Pipfile.lock
├── README.md          # Project README file
├── requirements.txt   # Python dependencies
Installation and Setup
Follow these steps to clone and set up the project on your local machine:

Clone the repository:

bash
Copy code
git clone git@github.com:Benga21/phase-4-lateshow.git
cd phase-4-lateshow
Install dependencies using Pipenv:

bash
Copy code
pipenv install
Activate the virtual environment:

bash
Copy code
pipenv shell
Initialize the database:

bash
Copy code
flask db upgrade
Seed the database with initial data 

bash
Copy code
python seed_data.py
Run the Flask application:

bash
Copy code
flask run
The app will now be running locally at http://localhost:5000.

How to Use
You can access the API endpoints using a tool like Postman or via a browser. Here’s how you can interact with the available resources:

Here are the full URLs for accessing the specified endpoints based on a local environment running at http://localhost:5000:

Get all episodes:

URL: http://localhost:5000/episodes
Description: Retrieves a list of all episodes.
Get a specific episode:

URL: http://localhost:5000/episodes/<int:id>
Example: http://localhost:5000/episodes/1 (for the episode with ID )
Description: Retrieves a specific episode by its ID.
Get all guests:

URL: http://localhost:5000/guests
Description: Retrieves a list of all guests.
Get a specific guest:

URL: http://localhost:5000/guests/<int:id>
Example: http://localhost:5000/guests/1 (for the guest with ID )
Description: Retrieves a specific guest by their ID.
Get all appearances:

URL: http://localhost:5000/appearances
Description: Retrieves a list of all guest appearances.
Get a specific appearance:

URL: http://localhost:5000/appearances/<int:id>
Example: http://localhost:5000/appearances/1 (for the appearance with ID )
Description: Retrieves a specific appearance by its ID.
Create a new appearance:

URL: http://localhost:5000/appearances
Method: POST
Description: Creates a new appearance for a guest in a specific episode.
Make sure your Flask application is running on localhost:5000 or the relevant server URL if deployed elsewhere.


URL: POST /appearances
Description: Creates a new appearance for a guest in a specific episode.
Body:
json
Copy code
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1
}
Technologies Used
Flask: A lightweight WSGI web application framework for Python.
SQLite: A C library that provides a lightweight, serverless database.
SQLAlchemy: A Python SQL toolkit and ORM.
Pipenv: A dependency manager for Python projects.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
MIT License

Copyright (c) [2024] [DEGRACE BENGA]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files  to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
