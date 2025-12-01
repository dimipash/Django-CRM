# Django CRM

This project is a comprehensive Django-based Customer Relationship Management (CRM) application built from scratch. It integrates Google Contacts for seamless contact synchronization, implements time-series analytics using TimescaleDB, and features production-ready automation with modern Python tools.

![Screenshot of Django CRM](screenshot.png)

## Key Features

- **Google Contacts Sync:** Automatically sync contacts from your Google account.
- **Time-Series Analytics:** Track and analyze user events over time with TimescaleDB for powerful insights.
- **Modern UI:** A clean and responsive user interface built with Tailwind CSS and Flowbite.
- **Data Visualization:** Visualize analytics with Chart.js.
- **Automated Workflows:** Automate contact syncing using GitHub Actions.
- **User Activity Tracking:** Monitor user actions with a dedicated event tracking system using Django signals.

## Tech Stack

- **Backend:** 🕹️ Django
- **Database:** 🕹️ Tiger Cloud & TimescaleDB (Time-series optimized PostgreSQL)
- **Authentication & APIs:** 🕹️ Google OAuth & People API
- **Frontend:** 🕹️ Tailwind CSS & Flowbite
- **Data Visualization:** 🕹️ Chart.js
- **Package Management:** 🕹️ uv (Python) & npm (Node.js)
- **Automation:** 🕹️ GitHub Actions

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.14
- [uv](https://github.com/astral-sh/uv) installed
- Node.js and npm

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dimipash/Django-CRM.git
    cd Django-CRM
    ```

2.  **Set up the Python environment and install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

4.  **Set up your environment variables:**
    Copy the sample environment file and fill in your details.
    ```bash
    cp .env.sample .env
    ```
    You will need to provide the following values in your `.env` file:
    ```
    DATABASE_URL="postgresql://user:password@host:port/database"
    DJANGO_SECRET_KEY="your-django-secret-key"
    DJANGO_DEBUG="True"
    GOOGLE_OAUTH_CLIENT_ID="your-google-client-id"
    GOOGLE_OAUTH_CLIENT_SECRET="your-google-client-secret"
    ```

5.  **Run database migrations:**
    ```bash
    python src/manage.py migrate
    ```

6.  **Build the CSS:**
    To build the Tailwind CSS files, run the following command:
    ```bash
    npm run build:css
    ```
    This command will watch for changes and automatically rebuild the CSS.

7.  **Run the development server:**
    ```bash
    python src/manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Project Highlights

This project serves as a practical guide to building a production-ready Django application. You will learn how to:

✅ Set up a modern Django project with `uv`.
✅ Build Django models with foreign keys and relationships.
✅ Implement Google OAuth authentication.
✅ Create dynamic templates with Django's templating system.
✅ Track user events with Django signals and generic foreign keys.
✅ Analyze time-series data with TimescaleDB.
✅ Sync and parse data from the Google People API.
✅ Build custom Django management commands.
✅ Visualize analytics with Chart.js.
✅ Automate contact syncing with GitHub Actions.
