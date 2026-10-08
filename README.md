# Django

A collection of two small **Django** practice projects that cover the core building blocks of the framework: URL routing, views, templates with inheritance, static files, models and migrations, the admin site, form handling, flash messages and user authentication. Both projects use **SQLite** and **Bootstrap 5**, so there is no database server to set up.

| Project | What it is |
| --- | --- |
| [`Hello`](./Hello) | "Ice Cream" website with Home, About, Services and Contact pages. Contact form messages are saved to the database and shown in the admin site. |
| [`userproject`](./userproject) | Login and logout demo using Django's built-in authentication. |

## Project 1: Hello (Ice Cream website)

### Features

- Four pages (Home, About Us, Services, Contact Us) sharing one `base.html` layout through **template inheritance**
- Responsive Bootstrap navbar with a Services dropdown and a search box
- Home page with an image **carousel** and a grid of ice cream cards, using images from the `static/img` folder
- Context variables passed from a view to a template (`index` view)
- **Contact form** that saves the name, email and message with the date to the `Contact` model, then shows a dismissible success message using Django's messages framework
- **Admin site** with the `Contact` model registered and a custom "Ice Cream Admin" header and titles

### Routes

| URL | View | Page |
| --- | --- | --- |
| `/` | `index` | Home |
| `/about` | `about` | About Us |
| `/services` | `services` | Services |
| `/contact` | `contact` | Contact form (GET shows the form, POST saves a message) |
| `/admin/` | Django admin | Admin site |

### Model

`Contact` has `name` (up to 50 characters), `email` (up to 70 characters), `desc` (text) and `date`.

### Structure

```
Hello/
├── manage.py
├── db.sqlite3
├── Hello/              # Project settings, urls, wsgi/asgi
├── home/               # App: models, views, urls, admin, migrations
├── templates/          # base.html, index.html, about.html, services.html, contact.html
└── static/img/         # Carousel and card images
```

## Project 2: userproject (Login demo)

### Features

- Login page (Bootstrap sign-in layout) that checks the username and password with `authenticate()` and starts a session with `login()`
- Protected home page that greets the logged-in user and redirects anonymous visitors to the login page
- Logout view that ends the session and redirects to the login page
- "Invalid credentials" error shown on a failed login

### Routes

| URL | View | Page |
| --- | --- | --- |
| `/` | `index` | Welcome page (requires login, otherwise redirects to `/login`) |
| `/login` | `login` | Login form |
| `/logout` | `logout` | Logs the user out |
| `/admin/` | Django admin | Admin site |

### Structure

```
userproject/
├── manage.py
├── db.sqlite3
├── userproject/        # Project settings, urls, wsgi/asgi
├── home/               # App: views and urls
└── templates/          # login.html, index.html
```

## Tech Stack

| Technology | Usage |
| --- | --- |
| Python 3.10+ | Language |
| Django 5.2 | Web framework (projects were generated with Django 5.2.7) |
| SQLite | Default database |
| Bootstrap 5.3.8 | Styling and components, loaded from the jsDelivr CDN |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- An internet connection for the Bootstrap files (loaded from a CDN)

### Run a project locally

1. Clone the repository:
   ```bash
   git clone https://github.com/AmanPatil2002/Django.git
   cd Django
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Install Django:
   ```bash
   pip install "django>=5.2,<5.3"
   ```
4. Go into the project you want to run (`Hello` or `userproject`):
   ```bash
   cd Hello
   ```
5. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
6. Create an admin user. In `userproject` you also need this to have an account to log in with:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
8. Open http://127.0.0.1:8000/ in your browser. The admin site is at http://127.0.0.1:8000/admin/.

On some systems the command is `python3` instead of `python`.

## Notes and Known Limitations

- **Committed databases:** both `db.sqlite3` files are in the repository and contain user accounts and, in `Hello`, saved contact form messages. Remove them from the repository, add `db.sqlite3` to a `.gitignore`, and use `migrate` to create a fresh database instead.
- **Development settings only:** both projects have `DEBUG = True` and a hardcoded `SECRET_KEY`. Do not deploy them as they are. Load the secret key and debug flag from environment variables first. In `Hello`, `ALLOWED_HOSTS` is empty, so it only works for local development.
- **Placeholder content in `Hello`:** the About and Services pages only show a short placeholder sentence, the "Softy" and "Family pack" menu items link to `#`, and the search box does nothing.
- **Contact form:** it has no server-side validation, and it does not redirect after saving, so refreshing the page after submitting sends the form again. The name input also uses `type="name"`, which is not a valid HTML input type (use `type="text"`).
- **`userproject`:** there is no registration page, so accounts must be created with `createsuperuser` or in the admin site. Logout is a plain link (a GET request), and the login page title is still "Bootstrap demo".
- **Repository clutter:** `__pycache__/` folders are committed, and `.vscode/` contains C/C++ build settings that are not related to this project. Add a `.gitignore` with `__pycache__/` and `.vscode/` to keep the repository clean.

## Author

**Aman Patil** – [@AmanPatil2002](https://github.com/AmanPatil2002)

## License

This repository is for learning and practice purposes. Add a license of your choice if you plan to share or reuse it.
