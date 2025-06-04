# Flask Notes App

A simple notes application built with Flask, SQLAlchemy, and SQLite, following modular application structure and best practices.

## Project Structure
```python
notes_app/
├── __init__.py           # Application factory
├── config.py            # Configuration settings
├── models/              # Database models
├── routes/              # Route blueprints
├── static/              # Static files (CSS, JS)
└── templates/           # HTML templates
```

## Features
- View all notes in a responsive grid layout
- Create new notes with title and content
- Edit existing notes
- Delete notes with confirmation
- Timestamps for note creation
- Bootstrap-based UI with custom styling

## Technologies Used
- Flask 3.0.2
- SQLAlchemy 2.0.28
- Flask-SQLAlchemy 3.1.1
- Bootstrap 5.3
- SQLite database

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd notes-app
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python run.py
```

6. Open http://localhost:5000 in your browser

Summary
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment (Windows)
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python run.py
```

## Development

### Project Organization
- Models are in `notes_app/models/`
- Routes are in `notes_app/routes/`
- Templates are in `notes_app/templates/`
- Static files are in `notes_app/static/`

### Database
- SQLite database will be created automatically as `notes_app/notes.db`
- Models can be modified in `notes_app/models/`

### Configuration
- Development config is in `notes_app/config.py`
- For production, set environment variable `SECRET_KEY`

## Contributing
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

