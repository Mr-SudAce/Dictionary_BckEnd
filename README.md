# Dictionary Backend System

A robust Backend system built with **Django** and **Django Rest Framework (DRF)**. This project serves as a Content Management System (CMS) and API provider for a Dictionary application, featuring management for words, blog posts, site pages, and UI configuration (headers/footers).

## Features

*   **RESTful API**: Comprehensive API endpoints for Words, Blogs, Pages, Headers, Footers, and Users.
*   **Custom Admin Dashboard**: A tailored administrative interface (separate from the standard Django Admin) for managing content.
*   **Rich Text Support**: Integration with `django-tinymce` for rich text editing in descriptions and blog posts.
*   **User Management**: Custom authentication flows (Login/Register) and user management.
*   **Media Management**: Handling of images for blogs, posts, and site logos.

## Tech Stack

*   **Language**: Python 3
*   **Framework**: Django
*   **API**: Django Rest Framework
*   **Database**: SQLite (Default)
*   **Libraries**:
    *   `django-tinymce`: For HTML fields.
    *   `requests`: (no longer required by backend; previously used for internal API calls which have been removed)
    *   `Pillow`: For image processing.

## Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd BackEnd
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django djangorestframework django-tinymce pillow
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

## Accessing the Application

*   **Dashboard**: Open `http://127.0.0.1:8000/` in your browser.
*   **Login**: `http://127.0.0.1:8000/login/`
*   **Register**: `http://127.0.0.1:8000/register/`

## API Endpoints

The application exposes the following API endpoints (Base URL: `/api/`):

### Words
*   `GET /api/all/word/` - Retrieve all words
*   `GET /api/word/<id>/` - Retrieve a specific word
*   `POST /api/word/` - Create a new word
*   `PUT /api/word/update/<id>/` - Update a word
*   `DELETE /api/word/delete/<id>/` - Delete a word

### Blogs & Posts
*   `GET /api/all/blog/` - Retrieve all blogs
*   `GET /api/all/post/` - Retrieve all posts
*   `GET /api/all/postcat/` - Retrieve post categories

### Site Configuration
*   `GET /api/all/header/` - Retrieve header configuration
*   `GET /api/all/footer/` - Retrieve footer configuration
*   `GET /api/all/page/` - Retrieve static pages

### Users
*   `GET /api/all/user/` - List all users
*   `POST /api/user/` - Create a user

## Project Structure

```
BackEnd/
├── api/
│   ├── admin.py        # Django Admin registration
│   ├── api_url.py      # API specific URL routing
│   ├── api_views.py    # DRF View functions
│   ├── forms.py        # Django forms for the Dashboard
│   ├── models.py       # Database Models (WordModel, BlogModel, etc.)
│   ├── serializers.py  # DRF Serializers
│   ├── urls.py         # Main URL routing (Dashboard + API inclusion)
│   └── views.py        # Dashboard View functions
├── manage.py
└── ...
```