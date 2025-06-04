from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.title}>'

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Display all notes on the home page"""
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    """Create a new note"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/notes/<int:id>/edit', methods=['GET', 'POST'])
def edit_note(id):
    """Edit an existing note"""
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', note=note)

@app.route('/notes/<int:id>/delete', methods=['POST'])
def delete_note(id):
    """Delete a note"""
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 