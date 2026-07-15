# app.py
# Main Flask application file - handles all routes and app logic

from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models.db import get_db_connection, init_db
from utils.resume_parser import parse_resume
from utils.report_generator import generate_pdf_report
from utils.scorer import calculate_score, get_performance_label, generate_suggestions
import os
import json

# Create the Flask application object
app = Flask(__name__)

# Secret key is required for Flask sessions to work securely
# It's used to encrypt session data (like login status) stored in cookies
app.secret_key = 'replace_this_with_a_random_secret_key_later'

# Folder where uploaded resumes will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Only allow these file extensions to be uploaded (security measure)
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    """Checks if the uploaded file has an allowed extension (pdf or docx)."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize the database and tables when the app starts
init_db()


# ---------------- HOME ROUTE ----------------
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


# ---------------- REGISTER ROUTE ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, password_hash)
            )
            conn.commit()
            conn.close()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except conn.IntegrityError:
            conn.close()
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')


# ---------------- LOGIN ROUTE ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


# ---------------- LOGOUT ROUTE ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ---------------- DASHBOARD ROUTE (protected) ----------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')


# ---------------- UPLOAD ROUTE ----------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'resume' not in request.files:
            flash('No file selected.', 'danger')
            return redirect(url_for('upload'))

        file = request.files['resume']

        if file.filename == '':
            flash('No file selected.', 'danger')
            return redirect(url_for('upload'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # ---- PARSE the resume to extract information ----
            parsed_data = parse_resume(filepath)

            # ---- SCORE the resume ----
            score_result = calculate_score(parsed_data)
            total_score = score_result['total_score']
            breakdown = score_result['breakdown']
            performance_label = get_performance_label(total_score)
            suggestions = generate_suggestions(parsed_data, breakdown)

            # ---- SAVE everything into the database ----
            conn = get_db_connection()
            cursor = conn.execute('''
                INSERT INTO resume_history (
                    user_id, filename, candidate_name, email, phone,
                    score, performance_label, skills, education, projects,
                    experience, certifications, breakdown, suggestions
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                session['user_id'],
                filename,
                parsed_data['name'],
                parsed_data['email'],
                parsed_data['phone'],
                total_score,
                performance_label,
                json.dumps(parsed_data['skills']),
                parsed_data['education'],
                parsed_data['projects'],
                parsed_data['experience'],
                parsed_data['certifications'],
                json.dumps(breakdown),
                json.dumps(suggestions)
            ))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()

            return redirect(url_for('result', resume_id=new_id))
        else:
            flash('Invalid file type. Only PDF and DOCX are allowed.', 'danger')
            return redirect(url_for('upload'))

    return render_template('upload.html')


# ---------------- RESULT ROUTE ----------------
@app.route('/result/<int:resume_id>')
def result(resume_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    record = conn.execute(
        'SELECT * FROM resume_history WHERE id = ? AND user_id = ?',
        (resume_id, session['user_id'])
    ).fetchone()
    conn.close()

    if record is None:
        flash('Resume not found.', 'danger')
        return redirect(url_for('history'))

    skills = json.loads(record['skills'])
    breakdown = json.loads(record['breakdown'])
    suggestions = json.loads(record['suggestions'])

    return render_template(
        'result.html',
        record=record,
        skills=skills,
        breakdown=breakdown,
        suggestions=suggestions
    )


# ---------------- DOWNLOAD REPORT ROUTE ----------------
@app.route('/download_report/<int:resume_id>')
def download_report(resume_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    record = conn.execute(
        'SELECT * FROM resume_history WHERE id = ? AND user_id = ?',
        (resume_id, session['user_id'])
    ).fetchone()
    conn.close()

    if record is None:
        flash('Resume not found.', 'danger')
        return redirect(url_for('history'))

    skills = json.loads(record['skills'])
    breakdown = json.loads(record['breakdown'])
    suggestions = json.loads(record['suggestions'])

    os.makedirs('reports', exist_ok=True)

    output_filename = f"report_{resume_id}.pdf"
    output_path = os.path.join('reports', output_filename)

    generate_pdf_report(record, skills, breakdown, suggestions, output_path)

    return send_file(output_path, as_attachment=True, download_name=output_filename)


# ---------------- HISTORY ROUTE ----------------
@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    records = conn.execute(
        'SELECT * FROM resume_history WHERE user_id = ? ORDER BY uploaded_at DESC',
        (session['user_id'],)
    ).fetchall()
    conn.close()

    return render_template('history.html', records=records)


# ---------------- DELETE HISTORY ROUTE ----------------
@app.route('/delete/<int:resume_id>', methods=['POST'])
def delete_history(resume_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute(
        'DELETE FROM resume_history WHERE id = ? AND user_id = ?',
        (resume_id, session['user_id'])
    )
    conn.commit()
    conn.close()

    flash('Resume record deleted successfully.', 'success')
    return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True)