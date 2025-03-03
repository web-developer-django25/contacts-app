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
contacts_app/
├── contacts/                 # Main application
│   ├── models.py            # Contact and Category models
│   ├── views.py             # Views and HTMX handlers
│   ├── forms.py             # Contact and Category forms
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
├── static/                  # Static files
│   ├── css/                # Custom CSS
│   └── img/                # Images
└── templates/              # Base templates
```

## API Endpoints

The application includes a REST API:

- `GET /api/contacts/` - List all contacts
- `POST /api/contacts/` - Create a new contact
- `GET /api/contacts/{id}/` - Retrieve a contact
- `PUT /api/contacts/{id}/` - Update a contact
- `DELETE /api/contacts/{id}/` - Delete a contact

## Deployment

This application can be deployed to any platform that supports Django. Some recommended options:

- Heroku
- DigitalOcean
- AWS Elastic Beanstalk
- Python Anywhere

### Deployment Steps

1. Update `settings.py` for production:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Configure your production database
   - Set up static files hosting

2. Install production dependencies:
```bash
pip install gunicorn psycopg2-binary
```

3. Configure your web server (e.g., Nginx)

4. Set up SSL certificate

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