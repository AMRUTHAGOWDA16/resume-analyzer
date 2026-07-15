# 📄 Resume Analyzer

A full-stack web application that analyzes resumes (PDF/DOCX), extracts key information, calculates a resume score out of 100, and provides personalized suggestions for improvement — built to help job seekers strengthen their resumes before applying.

---

## 🚀 Features

- **User Authentication** — secure registration and login with hashed passwords (Werkzeug) and Flask session management
- **Resume Upload** — supports PDF and DOCX formats with file type validation
- **Resume Parsing** — automatically extracts:
  - Name, Email, Phone Number
  - Skills
  - Education
  - Projects
  - Experience
  - Certifications
- **Resume Scoring** — calculates a score out of 100 based on:
  - Contact Information (20)
  - Skills (25)
  - Projects (20)
  - Education (15)
  - Experience (10)
  - Formatting (10)
- **Visual Score Display** — animated circular progress bar with color-coded performance labels (Excellent / Good / Average / Poor)
- **Skill Badges** — detected technical skills displayed as colorful badges
- **Improvement Suggestions** — personalized, actionable feedback based on resume weaknesses
- **Upload History** — view and manage previously analyzed resumes
- **Delete History** — remove old resume records
- **Downloadable PDF Report** — generate a professional PDF summary of the analysis
- **Responsive Design** — works across desktop, tablet, and mobile

---

## 🛠️ Technologies Used

**Backend:** Python, Flask
**Frontend:** HTML, CSS, Bootstrap 5, JavaScript
**Database:** SQLite
**Libraries:**
- PyPDF2, pdfplumber — PDF text extraction
- python-docx — DOCX text extraction
- spaCy, NLTK — natural language processing
- scikit-learn, pandas, numpy — data handling
- reportlab — PDF report generation
- Werkzeug — password hashing & secure file handling

---

## 📁 Folder Structure
Q: How did the PDF download test go?
A: Yes, PDF downloaded and looks correct


Orchestrated remaining project setup tasks and configurations
Orchestrated remaining project setup tasks and configurations
Fantastic — that completes the core feature set! 🎉 Your Resume Analyzer now has every major feature from the original spec:

✅ Register/Login/Logout with hashed passwords
✅ Dashboard with cards
✅ Resume upload (PDF/DOCX) with validation
✅ Resume parsing (name, email, phone, skills, education, projects, experience, certifications)
✅ Resume scoring out of 100 with breakdown
✅ Circular progress bar visualization
✅ Skill badges
✅ Improvement suggestions
✅ Upload history with View/Delete
✅ Downloadable PDF report
What's left to make this GitHub/interview-ready:
.gitignore — so venv/, database.db, uploads/, reports/ don't get pushed to GitHub
README.md — professional documentation
LICENSE — open source license
Git setup — initialize repo and push to GitHub
(Optional) Quick responsive/mobile check
Let's knock these out. First, .gitignore — this is quick.

1. Open .gitignore (empty file in your project root) and paste this:

# Virtual environment
venv/

# Python cache files
__pycache__/
*.pyc

# Database
database.db

# Uploaded files and generated reports (user data, shouldn't be in Git)
uploads/*
!uploads/.gitkeep
reports/*
!reports/.gitkeep

# VS Code settings
.vscode/

# Environment variables (if you add any later)
.env
2. Save with Ctrl+S.

Quick explanation
venv/ — your virtual environment shouldn't go on GitHub; it's huge and anyone cloning your repo will create their own.
database.db — your personal test data shouldn't be public; anyone running the project will get a fresh database automatically (remember, init_db() creates it).
uploads/* and reports/* — same reason: these are user-uploaded files, not source code.
!uploads/.gitkeep — the ! means "don't ignore this one file." Since Git doesn't track empty folders, we add a tiny placeholder file called .gitkeep just so the empty uploads and reports folders still get created when someone clones your repo.
Let's create those placeholder files now. In the terminal, run:

echo. > uploads\.gitkeep
echo. > reports\.gitkeep
Let me know once that's done, and we'll move to writing the README.md next.

echo. : The term 'echo.' is not recognized as the name of a cmdlet, function, script file, or 
operable program. Check the spelling of the name, or if a path was included, verify that the path 
is correct and try again.
At line:1 char:1
+ echo. > uploads\.gitkeep
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (echo.:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Thought for 2s
Thought for 2s
Ah, that's a PowerShell quirk — echo. (no space) is a old CMD trick that doesn't work the same in PowerShell. Let's use PowerShell's own command instead.

Run these two commands instead:

powershell
New-Item -Path "uploads\.gitkeep" -ItemType File -Force
New-Item -Path "reports\.gitkeep" -ItemType File -Force
This creates an empty file at each path. Let me know once both run successfully.

yes done

Perfect. Now let's write the README.md — this is what people see first on your GitHub repo, so let's make it professional.

1. Open README.md and paste this:

markdown
# 📄 Resume Analyzer

A full-stack web application that analyzes resumes (PDF/DOCX), extracts key information, calculates a resume score out of 100, and provides personalized suggestions for improvement — built to help job seekers strengthen their resumes before applying.

---

## 🚀 Features

- **User Authentication** — secure registration and login with hashed passwords (Werkzeug) and Flask session management
- **Resume Upload** — supports PDF and DOCX formats with file type validation
- **Resume Parsing** — automatically extracts:
  - Name, Email, Phone Number
  - Skills
  - Education
  - Projects
  - Experience
  - Certifications
- **Resume Scoring** — calculates a score out of 100 based on:
  - Contact Information (20)
  - Skills (25)
  - Projects (20)
  - Education (15)
  - Experience (10)
  - Formatting (10)
- **Visual Score Display** — animated circular progress bar with color-coded performance labels (Excellent / Good / Average / Poor)
- **Skill Badges** — detected technical skills displayed as colorful badges
- **Improvement Suggestions** — personalized, actionable feedback based on resume weaknesses
- **Upload History** — view and manage previously analyzed resumes
- **Delete History** — remove old resume records
- **Downloadable PDF Report** — generate a professional PDF summary of the analysis
- **Responsive Design** — works across desktop, tablet, and mobile

---

## 🛠️ Technologies Used

**Backend:** Python, Flask
**Frontend:** HTML, CSS, Bootstrap 5, JavaScript
**Database:** SQLite
**Libraries:**
- PyPDF2, pdfplumber — PDF text extraction
- python-docx — DOCX text extraction
- spaCy, NLTK — natural language processing
- scikit-learn, pandas, numpy — data handling
- reportlab — PDF report generation
- Werkzeug — password hashing & secure file handling

---

## 📁 Folder Structure
resume-analyzer/
├── app.py # Main Flask application (routes & logic)
├── requirements.txt # Python dependencies
├── .gitignore
├── README.md
├── LICENSE
├── uploads/ # Uploaded resume files
├── reports/ # Generated PDF reports
├── templates/ # HTML pages
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── upload.html
│ ├── result.html
│ ├── history.html
│ ├── navbar.html
│ └── footer.html
├── static/
│ ├── css/style.css
│ ├── js/
│ └── images/
├── utils/
│ ├── resume_parser.py # Resume text extraction & data parsing
│ ├── scorer.py # Resume scoring logic
│ └── report_generator.py # PDF report generation
└── models/
└── db.py # Database connection & schema setup


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
http://127.0.0.1:5000


---

## 📸 Screenshots

*(Add screenshots of your Login, Dashboard, Upload, and Result pages here)*

---

## 🔮 Future Scope

- Add AI-powered resume vs job-description matching
- Support for multiple resume templates and export formats
- Admin panel for managing all users' resumes
- Email notifications with analysis reports
- Integration with LinkedIn for auto-profile import

---

## 👩‍💻 Author

**Amrutha V R Gowda**
Final-year Computer Science Engineering Student

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
2. Save with Ctrl+S.

Quick note
Replace YOUR_USERNAME in the clone URL with your actual GitHub username once you create the repo (we'll do that in the next step).

Reply DONE and we'll write the LICENSE file next (quick, standard MIT license), then move to Git/GitHub setup.

[AMRUTHAGOWDA16](https://github.com/AMRUTHAGOWDA16) this is  my username give me entire thing to copy now


Identified need to update README with correct username
Identified need to update README with correct username
Here's the complete README.md with your actual GitHub username filled in — copy everything below and replace the entire file:

markdown
# 📄 Resume Analyzer

A full-stack web application that analyzes resumes (PDF/DOCX), extracts key information, calculates a resume score out of 100, and provides personalized suggestions for improvement — built to help job seekers strengthen their resumes before applying.

---

## 🚀 Features

- **User Authentication** — secure registration and login with hashed passwords (Werkzeug) and Flask session management
- **Resume Upload** — supports PDF and DOCX formats with file type validation
- **Resume Parsing** — automatically extracts:
  - Name, Email, Phone Number
  - Skills
  - Education
  - Projects
  - Experience
  - Certifications
- **Resume Scoring** — calculates a score out of 100 based on:
  - Contact Information (20)
  - Skills (25)
  - Projects (20)
  - Education (15)
  - Experience (10)
  - Formatting (10)
- **Visual Score Display** — animated circular progress bar with color-coded performance labels (Excellent / Good / Average / Poor)
- **Skill Badges** — detected technical skills displayed as colorful badges
- **Improvement Suggestions** — personalized, actionable feedback based on resume weaknesses
- **Upload History** — view and manage previously analyzed resumes
- **Delete History** — remove old resume records
- **Downloadable PDF Report** — generate a professional PDF summary of the analysis
- **Responsive Design** — works across desktop, tablet, and mobile

---

## 🛠️ Technologies Used

**Backend:** Python, Flask
**Frontend:** HTML, CSS, Bootstrap 5, JavaScript
**Database:** SQLite
**Libraries:**
- PyPDF2, pdfplumber — PDF text extraction
- python-docx — DOCX text extraction
- spaCy, NLTK — natural language processing
- scikit-learn, pandas, numpy — data handling
- reportlab — PDF report generation
- Werkzeug — password hashing & secure file handling

---

## 📁 Folder Structure
resume-analyzer/
├── app.py # Main Flask application (routes & logic)
├── requirements.txt # Python dependencies
├── .gitignore
├── README.md
├── LICENSE
├── uploads/ # Uploaded resume files
├── reports/ # Generated PDF reports
├── templates/ # HTML pages
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── upload.html
│ ├── result.html
│ ├── history.html
│ ├── navbar.html
│ └── footer.html
├── static/
│ ├── css/style.css
│ ├── js/
│ └── images/
├── utils/
│ ├── resume_parser.py # Resume text extraction & data parsing
│ ├── scorer.py # Resume scoring logic
│ └── report_generator.py # PDF report generation
└── models/
└── db.py # Database connection & schema setup

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/AMRUTHAGOWDA16/resume-analyzer.git
cd resume-analyzer
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
http://127.0.0.1:5000
---

## 📸 Screenshots

*(Add screenshots of your Login, Dashboard, Upload, and Result pages here)*

---

## 🔮 Future Scope

- Add AI-powered resume vs job-description matching
- Support for multiple resume templates and export formats
- Admin panel for managing all users' resumes
- Email notifications with analysis reports
- Integration with LinkedIn for auto-profile import

---

## 👩‍💻 Author

**Amrutha V R Gowda**
Final-year Computer Science Engineering Student
GitHub: [@AMRUTHAGOWDA16](https://github.com/AMRUTHAGOWDA16)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.