# Hospital Management Web Application

A web-based Hospital Management System built with Django. It allows patients to register and book appointments with doctors, while doctors and admins can manage patient records, doctor profiles, and appointment schedules.

## Features

- **User Authentication** — sign up, sign in, sign out, update profile and password
- **Doctor Management** — add, view, update, and delete doctor records (name, phone, email, specialization, availability, profile picture, intro video)
- **Patient Management** — add, view, update, and delete patient records (name, phone, email, age, profile picture, symptoms audio)
- **Appointment Booking** — create, view, update, and delete appointments linking patients, doctors, and users, with optional document uploads
- **Media Handling** — supports image, video, audio, and document uploads for doctors, patients, and appointments
- **Django Admin Panel** — manage all data from the built-in admin interface

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS (Django templates)
- **Image handling:** Pillow

## Project Structure

```
Hospital_Management/
├── Hospital_Management/     # Project settings, URLs, WSGI/ASGI config
├── authen/                  # Authentication app (signup, signin, profile)
├── base/                    # Core app (doctors, patients, appointments)
├── static/                  # Static files (CSS)
├── templates/               # Base HTML templates
├── media/                   # Uploaded images, videos, audio, documents
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hospital-management-web-application.git
   cd hospital-management-web-application
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the app**
   Visit `http://127.0.0.1:8000/` in your browser.
   Visit `http://127.0.0.1:8000/admin/` to access the admin panel.

## Usage

- Sign up as a new user or sign in with existing credentials.
- Add doctors and patients through the respective forms.
- Book an appointment by selecting a doctor, patient, date, and time.
- Update or delete doctors, patients, and appointments as needed.
- Use the Django admin panel for full database control.

## Requirements

```
Django==5.2.17
Pillow==12.3.0
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Developed by Shivam.
