from flask import Blueprint, render_template, request, redirect, url_for
from notes_app import db
from notes_app.models.note import Note

# Create blueprint
bp = Blueprint('notes', __name__)

@bp.route('/')
def index():
    """
    Home page route - Display all notes
    
    Retrieves all notes from the database, ordered by creation date (newest first)
    and renders them using the index.html template.
    """
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes)

@bp.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    """
    Create new note route - Handles both form display and note creation
    
    GET request: Displays the empty note form
    POST request: Creates a new note with the submitted data
    
    Form fields:
    - title: The note's title (required)
    - content: The note's content (required)
    """
    if request.method == 'POST':
        # Extract form data
        title = request.form['title']
        content = request.form['content']
        
        # Create and save the new note
        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()
        
        # Redirect to home page after successful creation
        return redirect(url_for('notes.index'))
    
    # Display the empty form for GET request
    return render_template('form.html')

@bp.route('/notes/<int:id>/edit', methods=['GET', 'POST'])
def edit_note(id):
    """
    Edit note route - Handles both form display and note updates
    
    GET request: Displays the form pre-filled with note data
    POST request: Updates the note with the submitted data
    
    Parameters:
    - id: The ID of the note to edit
    
    Returns 404 if note is not found
    """
    # Get the note or return 404 if not found
    note = Note.query.get_or_404(id)
    
    if request.method == 'POST':
        # Update note with form data
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        
        # Redirect to home page after successful update
        return redirect(url_for('notes.index'))
    
    # Display the form with existing note data for GET request
    return render_template('form.html', note=note)

@bp.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    """
    Delete note route - Handles note deletion
    
    Only accepts POST requests to prevent accidental deletions from GET requests
    
    Parameters:
    - id: The ID of the note to delete
    
    Returns 404 if note is not found
    """
    # Get the note or return 404 if not found
    note = Note.query.get_or_404(id)
    
    # Delete the note and commit the change
    db.session.delete(note)
    db.session.commit()
    
    # Redirect to home page after successful deletion
    return redirect(url_for('notes.index')) 