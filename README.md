# Nadia's Garden
A Django-based online pizza shop.

## Project Setup
### Prerequisites
- Python (version 3.6 or later)
- pip (Python package installer)
- A code editor or IDE
## Installation
1. Clone the repository:
   ```sh
git clone https://github.com/bennyGitau/nadiasgarden-django-project.git
cd nadiasgarden
    ```


2. Create a virtual environment:
   ```sh
python -m venv venv
source venv/bin/activate  # On Unix-like systems
venv\Scripts\activate  # On Windows
    ```

3. Install dependencies:
   ```sh
pip install -r requirements.txt
    ```

4. Database migration:
   ```sh                
python manage.py migrate
    ```

5Create a superuser:
Bash
python manage.py createsuperuser
Use code with caution.

Running the Development Server
Bash
python manage.py runserver
Use code with caution.

Project Structure
nadias_garden: Main project directory.
core: App containing core functionalities like models, views, serializers, etc.
users: App for user management (optional).
orders: App for handling orders and payments.
pizzas: App for managing pizza options, sizes, toppings, etc.
static: Static files (CSS, JavaScript, images).
templates: HTML templates.
db.sqlite3: SQLite database file (for development).
manage.py: Django management script.
requirements.txt: List of project dependencies.
Environment Variables
SECRET_KEY: Replace 'django-secret-key' with a strong random key in settings.py.
DATABASE_URL: If using a production database, configure the database connection in settings.py.
EMAIL_BACKEND: Configure email settings for sending order confirmations, etc.
Additional Notes
Consider using environment variables for sensitive information like API keys and database credentials.
Implement proper error handling and logging.
Optimize database queries for performance.
Test your application thoroughly.
Deploy to a production server for public access.
Contributing
If you want to contribute to the project, feel free to fork the repository and submit pull requests.
