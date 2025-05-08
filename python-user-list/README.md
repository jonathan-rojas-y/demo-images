# Python User List

This project is a simple Flask application that displays a list of users. It serves as a demonstration of how to create a web application using Flask.

## Project Structure

```
python-user-list
├── app
│   ├── __init__.py
│   ├── main.py
│   └── templates
│       └── users.html
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-user-list
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app/main.py
   ```

5. **Access the user list:**
   Open your web browser and go to `http://127.0.0.1:5000/users`.

## Docker Instructions

To build and run the application using Docker, follow these steps:

1. **Build the Docker image:**
   ```
   docker build -t python-user-list .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 python-user-list
   ```

3. **Access the user list:**
   Open your web browser and go to `http://localhost:5000/users`.

## Usage

The application displays a list of users. You can modify the user data in the `main.py` file to see different results.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.