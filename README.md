# Dictionary Backend Application

The server-side application for the Dictionary System. This project is built with Django and Django REST Framework to provide a robust API for the corresponding frontend application.

## Features

*   **Words API**: Full CRUD functionality for dictionary words, definitions, and related data.
*   **Content Management API**: Serves content for blogs, posts, and dynamic pages managed through the Django admin or other interfaces.
*   **Dynamic Site Configuration**: Endpoints to deliver site-wide configurations for elements like headers and footers.
*   **User Authentication**: Secure user registration and token-based authentication (e.g., JWT).
*   **Admin Interface**: Utilizes the built-in Django Admin for easy data management.

## Tech Stack

*   **Framework**: Django, Django REST Framework
*   **Database**: SQLite3 (for development), PostgreSQL (recommended for production)
*   **Environment**: Python 3.8+
*   **Authentication**: Simple JWT for DRF (or another token-based auth)

## Prerequisites

*   **Python** (3.8+ version recommended)
*   **Pip** (Python package installer)
*   `virtualenv` (for creating isolated Python environments)

## Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd BackEnd
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    # For Unix/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    It's recommended to have a `requirements.txt` file in your project root.
    ```bash
    pip install -r requirements.txt
    ```
    A typical `requirements.txt` might include:
    ```
    django
    djangorestframework
    djangorestframework-simplejwt
    django-cors-headers
    python-decouple # For environment variables
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the project root directory. This file will hold your secret keys and settings. Add it to your `.gitignore`!
    ```env
    SECRET_KEY='your-secret-key'
    DEBUG=True
    DATABASE_URL='sqlite:///db.sqlite3' # Example for SQLite
    # DATABASE_URL='postgres://user:password@host:port/dbname' # Example for PostgreSQL
    ```

5.  **Run Database Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser**
    This allows you to access the Django Admin.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000`.

## Project Structure

A typical project structure might look like this:

```
BackEnd/
├── dictionary_project/   # Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/                  # Main Django app for the API
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .env                  # Environment variables (gitignored)
├── .gitignore
├── manage.py             # Django's command-line utility
└── requirements.txt      # Python dependencies
```

## API Endpoints

The API is accessible under the `/api/` prefix.

*   **Auth**:
    *   `POST /api/token/`: Obtain JWT token pair.
    *   `POST /api/token/refresh/`: Refresh an access token.
    *   `POST /api/user/register/`: Register a new user. (This is a custom endpoint you might create)

*   **Words**:
    *   `GET /api/all/word/`: List all words.
    *   `GET /api/word/<id>/`: Retrieve a specific word by its ID.

*   **Content**:
    *   `GET /api/all/blog/`: List all blogs.
    *   `GET /api/all/post/`: List all posts.
    *   `GET /api/all/page/`: List all pages.

*   **Site Config**:
    *   `GET /api/all/header/`: Get header configuration.
    *   `GET /api/all/footer/`: Get footer configuration.

## Deployment

For production, ensure you have:
*   Set `DEBUG = False` in your settings.
*   Configured a production-ready database like PostgreSQL.
*   Set up a web server like Gunicorn or uWSGI.
*   Configured static file serving.

## Contributing

Contributions are welcome! Please open an issue to discuss your ideas or submit a pull request.
