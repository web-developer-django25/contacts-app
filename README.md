# Contacts App

A modern web application for managing contacts built with Django, HTMX, and Tailwind CSS.

## Features

- 📱 Responsive, modern UI using Tailwind CSS
- ⚡ Real-time search with HTMX
- ✨ Full CRUD operations for contacts
- 🗂️ Contact categories for better organization
- 📝 Contact information includes:
  - Name
  - Email
  - Phone number
  - Address
  - Notes
  - Category
- 🔄 Automatic timestamps for creation and updates
- 📊 Paginated contact list (10 contacts per page)
- 🎯 Success messages for all operations
- 🔍 Instant search across all contact fields:
  - Name
  - Email
  - Phone number
  - Address
- 🎨 Clean and intuitive interface

## Technology Stack

- **Backend**: Django 5.1.6
- **Frontend**: 
  - HTMX for dynamic interactions
  - Tailwind CSS for styling
- **Database**: SQLite (can be easily switched to PostgreSQL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/web-developer-django25/contacts-app.git
cd contacts-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Usage

### Managing Contacts
- Visit the homepage to see your contacts list
- Use the "Add Contact" button to create new contacts
- Click on a contact to view details
- Use the edit or delete buttons to modify contacts

### Categories
- Create categories to organize your contacts
- Assign contacts to categories during creation or editing
- Filter contacts by category

### Search
- Use the search bar to instantly filter contacts
- Search works across all contact fields:
  - Name
  - Email
  - Phone number
  - Address
- Results update in real-time as you type

## Project Structure

```
contacts_app/              # Main project directory
├── contacts/             # Main application
│   ├── migrations/      # Database migrations
│   ├── templates/      # Application templates
│   │   ├── contacts/  # Contact-related templates
│   │   └── registration/ # Authentication templates
│   ├── admin.py       # Admin interface configuration
│   ├── apps.py        # Application configuration
│   ├── forms.py       # Form definitions
│   ├── models.py      # Database models
│   ├── tests.py       # Unit tests
│   ├── urls.py        # URL routing
│   └── views.py       # View logic
├── contacts_app/        # Project configuration
│   ├── static/        # Project-wide static files
│   │   ├── css/      # CSS files
│   │   └── img/      # Images
│   ├── templates/    # Project-wide templates
│   ├── settings.py   # Project settings
│   ├── urls.py       # Project URL configuration
│   ├── wsgi.py      # WSGI configuration
│   └── asgi.py      # ASGI configuration
├── staticfiles/        # Collected static files
├── .gitignore         # Git ignore rules
├── app.yaml           # Google Cloud App Engine configuration
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

### Key Components

1. **Application Layer (`contacts/`)**
   - Models: Database schema definitions
   - Views: Business logic and request handling
   - Templates: HTML templates with Tailwind CSS
   - Forms: Form definitions and validation
   - URLs: URL routing for the application

2. **Project Configuration (`contacts_app/`)**
   - Settings: Project-wide settings and configurations
   - Static Files: CSS, JavaScript, and images
   - Base Templates: Base HTML templates
   - URL Configuration: Root URL routing

3. **Deployment Configuration**
   - `app.yaml`: Google Cloud App Engine settings
   - `requirements.txt`: Python package dependencies
   - `.gitignore`: Source control exclusions

4. **Static Files**
   - Development: Served from `contacts_app/static/`
   - Production: Collected to `staticfiles/` and served from Google Cloud Storage

## API Endpoints

The application includes a REST API:

- `GET /api/contacts/` - List all contacts
- `POST /api/contacts/` - Create a new contact
- `GET /api/contacts/{id}/` - Retrieve a contact
- `PUT /api/contacts/{id}/` - Update a contact
- `DELETE /api/contacts/{id}/` - Delete a contact

## Deployment

This application is configured for deployment on Google Cloud Platform (App Engine) with PostgreSQL and Cloud Storage. Here's how to deploy:

### Prerequisites

1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. Have a Google Cloud account with billing enabled
3. Create a new project or select an existing one

### Setting up Google Cloud Resources

1. Create a Cloud SQL instance:
```bash
# Enable Cloud SQL Admin API
gcloud services enable sqladmin.googleapis.com

# Create a PostgreSQL instance
gcloud sql instances create contacts-db \
    --database-version=POSTGRES_13 \
    --tier=db-f1-micro \
    --region=us-central1

# Create a database
gcloud sql databases create contacts_db --instance=contacts-db

# Create a user
gcloud sql users create contacts_user \
    --instance=contacts-db \
    --password=YOUR_PASSWORD
```

2. Create a Cloud Storage bucket:
```bash
# Create a bucket for static files
gcloud storage buckets create gs://YOUR_BUCKET_NAME \
    --location=us-central1 \
    --uniform-bucket-level-access

# Set bucket permissions
gsutil iam ch allUsers:objectViewer gs://YOUR_BUCKET_NAME
```

3. Set up Secret Manager:
```bash
# Enable Secret Manager API
gcloud services enable secretmanager.googleapis.com

# Create a secret for Django
echo "your-secret-key" | \
gcloud secrets create django_secret \
    --data-file=- \
    --replication-policy="automatic"
```

### Configuration

1. Set environment variables in app.yaml:
```yaml
env_variables:
  DJANGO_SETTINGS_MODULE: "contacts_app.settings"
  DEBUG: "False"
  DB_NAME: "contacts_db"
  DB_USER: "contacts_user"
  DB_PASSWORD: "YOUR_PASSWORD"
  DB_HOST: "/cloudsql/YOUR_INSTANCE_CONNECTION_NAME"
  GS_BUCKET_NAME: "YOUR_BUCKET_NAME"
```

2. Update database connection:
```bash
# Get your instance connection name
gcloud sql instances describe contacts-db --format='value(connectionName)'
```

### Deployment Steps

1. Collect static files:
```bash
python manage.py collectstatic
```

2. Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Deploy to App Engine:
```bash
gcloud app deploy app.yaml
```

4. View your application:
```bash
gcloud app browse
```

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/web-developer-django25/contacts-app.git
cd contacts-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file
echo "DEBUG=True" > .env
echo "SECRET_KEY=your-secret-key" >> .env
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

### Production Considerations

1. Security:
   - SSL is enforced
   - HSTS is enabled
   - XSS protection is active
   - Content type sniffing prevention is enabled
   - Clickjacking protection is active

2. Performance:
   - Static files are served from Google Cloud Storage
   - WhiteNoise middleware is configured for efficient static file serving
   - Database connections are optimized for Cloud SQL

3. Monitoring:
   - Use Google Cloud Monitoring for application metrics
   - Set up logging with Cloud Logging
   - Configure alerts for critical errors

4. Maintenance:
   - Regularly update dependencies
   - Monitor database performance
   - Back up data periodically
   - Review security settings

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation
- HTMX
- Tailwind CSS
- Django REST Framework 