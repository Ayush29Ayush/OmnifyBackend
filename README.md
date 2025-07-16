# Fitness Studio Booking API

A Django REST Framework service for listing fitness classes and booking spots, secured with JWT and documented via Swagger.

---

## 🚀 Quickstart

### 1\. Clone & Enter Repository

```bash
git clone https://github.com/Ayush29Ayush/OmnifyBackend.git
cd OmnifyBackend/
```

### 2\. Create Virtual Environment & Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3\. Configure Environment

Copy the example environment file and edit it with your settings.

```bash
cd fitness_studio/
cp env.example .env
```

Update `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `TIME_ZONE` in the newly created `.env` file.

### 4\. Database Setup & Seed Data

Run migrations and populate the database with initial data.

```bash
cd ..
python manage.py migrate
python manage.py seed_data
```

### 5\. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6\. Run the Development Server

```bash
python manage.py runserver
```

---

## 📦 Endpoints

### Public

* `GET /api/classes/`
  * Lists all upcoming fitness classes.

### Authentication (JWT)

* `POST /api/token/`

  * Request a new access and refresh token.
  * **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
* `POST /api/token/refresh/`

  * Obtain a new access token using a refresh token.
  * **Request Body:**
    ```json
    {
        "refresh": "your_refresh_token"
    }
    ```

### Protected (Requires `Authorization: Bearer <access_token>`)

* `POST /api/book/`

  * Book a spot in a fitness class.
  * **Request Body:**
    ```json
    {
        "fitness_class": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }
    ```
* `GET /api/bookings/?client_email=<email>`

  * Lists all bookings associated with a specific client email.

---

## 📄 API Docs

Interactive API documentation is available via Swagger UI and a downloadable OpenAPI schema.

* **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
* **OpenAPI Schema (JSON):** `http://127.0.0.1:8000/api/schema/`

---

## 🧪 Testing

Run the test suite using `pytest`. All tests marked with `django_db` ensure full coverage of the booking flows.

```bash
pytest
```

---

## 📂 Logging

The application logs to both the console and a rotating file located at `logs/fitness_studio.log`.

* **Handler:** `RotatingFileHandler`
* **Max File Size:** 5 MB
* **Backup Files:** 5
* **Format:** `[timestamp] LEVEL logger_name: message`

---

## ⚙️ Configuration

Environment variables can be set in the `.env` file.

| Variable          | Description                            | Default      |
| ----------------- | -------------------------------------- | ------------ |
| `SECRET_KEY`    | Django's secret key for security.      | *required* |
| `DEBUG`         | Toggles Django's debug mode.           | `True`     |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts. | `empty`    |
| `TIME_ZONE`     | The application's time zone.           | `UTC`      |

---
