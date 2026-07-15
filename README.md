# 📄 Resume Analyzer

A full-stack web application built using **Flask** that analyzes resumes (PDF/DOCX), extracts important information, calculates a resume score out of 100, and provides personalized suggestions to improve the resume before applying for jobs.

---

## 🌟 Features

- 🔐 Secure User Authentication (Register/Login)
- 🔑 Password Hashing using Werkzeug
- 📄 Upload Resume (PDF & DOCX)
- 📝 Automatic Resume Parsing
- 👤 Extracts:
  - Name
  - Email
  - Phone Number
  - Skills
  - Education
  - Projects
  - Experience
  - Certifications
- 📊 Resume Score (Out of 100)
- 📈 Circular Progress Score Visualization
- 🏷️ Skill Badge Display
- 💡 Personalized Improvement Suggestions
- 🕒 Resume Upload History
- 🗑️ Delete Previous Resume Records
- 📥 Download Resume Analysis Report as PDF
- 📱 Responsive User Interface
- 💾 SQLite Database Integration

---

# 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database
- SQLite

### Libraries Used

- PyPDF2
- pdfplumber
- python-docx
- spaCy
- NLTK
- pandas
- numpy
- scikit-learn
- reportlab
- Werkzeug

---

# 📁 Project Structure

```text
resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── database.db
│
├── uploads/
├── reports/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── result.html
│   ├── history.html
│   ├── navbar.html
│   └── footer.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── utils/
│   ├── resume_parser.py
│   ├── scorer.py
│   └── report_generator.py
│
└── models/
    └── db.py
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AMRUTHAGOWDA16/resume-analyzer.git
cd resume-analyzer
```

### 2️⃣ Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5️⃣ Run the Project

```bash
python app.py
```

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## 🔐 Login Page

> Add screenshot here

![Login](screenshots/login.png)

---

## 📝 Register Page

> Add screenshot here

![Register](screenshots/register.png)

---

## 🏠 Dashboard

> Add screenshot here

![Dashboard](screenshots/dashboard.png)

---

## 📤 Upload Resume

> Add screenshot here

![Upload](screenshots/upload.png)

---

## 📊 Resume Analysis

> Add screenshot here

![Analysis](screenshots/result.png)

---

## 🕒 Resume History

> Add screenshot here

![History](screenshots/history.png)

---

# 📈 Resume Scoring Criteria

| Section | Marks |
|----------|------:|
| Contact Information | 20 |
| Skills | 25 |
| Projects | 20 |
| Education | 15 |
| Experience | 10 |
| Formatting | 10 |
| **Total** | **100** |

---

# 🔮 Future Improvements

- 🤖 AI-powered Resume Analysis
- 🎯 Resume vs Job Description Matching
- 📧 Email Report Delivery
- ☁️ Cloud Deployment
- 📄 Multiple Resume Templates
- 🔗 LinkedIn Profile Integration
- 📊 Analytics Dashboard
- 🌍 Multi-language Resume Support

---

# 👩‍💻 Author

**Amrutha V R Gowda**

Computer Science & Engineering Student

GitHub: **https://github.com/AMRUTHAGOWDA16**

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository and submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.