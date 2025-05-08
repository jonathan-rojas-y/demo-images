# Python Web Interface

This project is a simple web interface built using Flask. It allows users to upload images and serves as a demonstration for deploying applications on OpenShift.

## Project Structure

```
python-web-interface
├── app
│   ├── __init__.py
│   ├── main.py
│   └── templates
│       └── index.html
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-web-interface
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

5. **Access the web interface:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Docker Instructions

To build and run the application using Docker, follow these steps:

1. **Build the Docker image:**
   ```
   docker build -t python-web-interface .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 python-web-interface
   ```

3. **Access the web interface:**
   Open your web browser and go to `http://localhost:5000`.

## Usage

The web interface allows users to upload images. Once uploaded, the images can be processed or displayed as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.