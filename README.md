# Potential Nomac

Potential Nomac is a Django app built with Python 3.11. It provides the authentication api's using Django’s authentication, connecting with Redis for getting the cached data and providing the analytics based api for visualizing the data.

## Prerequisites

Ensure you have the following installed:
- Python 3.11 or above
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rafimashood/nomac-poc-be.git
    cd potential_nomac
    ```

2. **Create a virtual environment:**

    It is recommended to use a virtual environment to manage dependencies.

    ```bash
    python3.11 -m venv venv
    ```

3. **Activate the virtual environment:**

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

4. **Install the required dependencies:**

    Make sure you are in the project directory, then install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Setup Database (if applicable):**

    If your app uses a database, you need to run the migrations:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    After setting up, you can start the Django development server:

    ```bash
    python manage.py runserver
    ```

    The server will be available at `http://127.0.0.1:8000/`.

## Usage

To run your Django app, you can use the following commands:

- Run the development server:
    ```bash
    python manage.py runserver
    ```

- Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

## Additional Notes

- If you need to install specific dependencies for your environment, edit `requirements.txt` or install them manually using `pip install package_name` and add to the `requirements.txt` later use.
- Make sure to set up your env variable configurations in `.env`

