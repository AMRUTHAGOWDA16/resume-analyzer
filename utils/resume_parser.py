# utils/resume_parser.py
# This file contains all the logic for extracting information from resumes

import re  # Built-in library for pattern matching (finding emails, phone numbers, etc.)
import PyPDF2
import pdfplumber
import docx


# ---------- LIST OF SKILLS WE WANT TO DETECT ----------
# We'll search the resume text for these exact words (case-insensitive)
SKILL_KEYWORDS = [
    'Python', 'Java', 'C', 'C++', 'JavaScript', 'HTML', 'CSS', 'SQL',
    'Machine Learning', 'Flask', 'Django', 'React', 'NodeJS', 'Node.js',
    'Git', 'GitHub', 'Android', 'Firebase', 'MySQL'
]


def extract_text_from_pdf(filepath):
    """
    Extracts all readable text from a PDF file.
    We try pdfplumber first (more accurate), and fall back to PyPDF2
    if pdfplumber fails for any reason.
    """
    text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception:
        # Fallback method using PyPDF2 if pdfplumber has trouble
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(filepath):
    """
    Extracts all readable text from a DOCX (Word) file.
    python-docx reads the document paragraph by paragraph.
    """
    doc = docx.Document(filepath)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def extract_text(filepath):
    """
    Decides which extraction method to use based on the file extension.
    Returns the raw extracted text as a single string.
    """
    if filepath.lower().endswith('.pdf'):
        return extract_text_from_pdf(filepath)
    elif filepath.lower().endswith('.docx'):
        return extract_text_from_docx(filepath)
    else:
        return ""


def extract_email(text):
    """
    Uses a regular expression (regex) to find an email address in the text.
    Regex pattern explanation:
    - Looks for: letters/numbers/dots/underscores + @ + letters/numbers/dots + a domain like .com
    """
    match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    return match.group(0) if match else "Not found"


def extract_phone(text):
    """
    Uses regex to find a phone number - looks for 10-digit numbers,
    optionally with a country code like +91.
    """
    match = re.search(r'(\+?\d{1,3}[-.\s]?)?\d{10}', text)
    return match.group(0) if match else "Not found"


def extract_name(text):
    """
    Simple heuristic to guess the candidate's name:
    We assume the name appears in the first non-empty line of the resume,
    which is true for most standard resume formats.
    """
    lines = text.strip().split('\n')
    for line in lines:
        clean_line = line.strip()
        # Skip empty lines and lines that look like emails/phone numbers
        if clean_line and '@' not in clean_line and not re.search(r'\d{5,}', clean_line):
            return clean_line
    return "Not found"


def extract_skills(text):
    """
    Searches the resume text for each skill in our SKILL_KEYWORDS list.
    Returns a list of skills that were actually found.
    Case-insensitive matching so "python" and "Python" both match.
    """
    found_skills = []
    text_lower = text.lower()
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return found_skills


def extract_section(text, section_names):
    """
    Generic helper to extract a "section" of the resume (like Education or Projects).
    It looks for a line containing one of the section_names (e.g. "Education"),
    then collects the following lines until it hits another known section heading.
    """
    lines = text.split('\n')
    section_text = []
    capturing = False

    # Common section headings that signal "stop capturing" once we hit them
    all_known_headings = [
        'education', 'experience', 'projects', 'skills', 'certifications',
        'internships', 'languages', 'objective', 'summary', 'contact'
    ]

    for line in lines:
        clean_line = line.strip()
        lower_line = clean_line.lower()

        # Check if this line is the heading we're looking for
        if any(name.lower() in lower_line for name in section_names) and len(clean_line) < 40:
            capturing = True
            continue

        # If we're capturing and we hit a DIFFERENT known heading, stop
        if capturing and any(heading in lower_line for heading in all_known_headings) and len(clean_line) < 40:
            if not any(name.lower() in lower_line for name in section_names):
                break

        if capturing and clean_line:
            section_text.append(clean_line)

    return "\n".join(section_text) if section_text else "Not found"


def parse_resume(filepath):
    """
    Main function that ties everything together.
    Given a file path, it returns a dictionary with all extracted information.
    """
    text = extract_text(filepath)

    result = {
        'raw_text': text,
        'name': extract_name(text),
        'email': extract_email(text),
        'phone': extract_phone(text),
        'skills': extract_skills(text),
        'education': extract_section(text, ['education', 'academic']),
        'projects': extract_section(text, ['projects']),
        'experience': extract_section(text, ['experience', 'work experience']),
        'certifications': extract_section(text, ['certifications', 'certificates']),
    }

    return result


# Allows testing this file directly: python utils/resume_parser.py
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        result = parse_resume(sys.argv[1])
        for key, value in result.items():
            if key != 'raw_text':
                print(f"{key}: {value}")