# utils/scorer.py
# Calculates a resume score out of 100 based on extracted data

def calculate_score(parsed_data):
    """
    Takes the dictionary returned by parse_resume() and calculates
    a score out of 100, broken down by category:

    Contact Information - 20 marks
    Skills              - 25 marks
    Projects            - 20 marks
    Education           - 15 marks
    Experience          - 10 marks
    Formatting          - 10 marks
    """
    score = 0
    breakdown = {}

    # ---------- CONTACT INFO (20 marks) ----------
    contact_score = 0
    if parsed_data['email'] != "Not found":
        contact_score += 10
    if parsed_data['phone'] != "Not found":
        contact_score += 10
    breakdown['contact'] = contact_score
    score += contact_score

    # ---------- SKILLS (25 marks) ----------
    # More skills detected = higher score, capped at 25
    num_skills = len(parsed_data['skills'])
    skills_score = min(num_skills * 3, 25)  # 3 marks per skill, max 25
    breakdown['skills'] = skills_score
    score += skills_score

    # ---------- PROJECTS (20 marks) ----------
    projects_score = 0
    if parsed_data['projects'] != "Not found" and len(parsed_data['projects']) > 20:
        projects_score = 20
    elif parsed_data['projects'] != "Not found":
        projects_score = 10
    breakdown['projects'] = projects_score
    score += projects_score

    # ---------- EDUCATION (15 marks) ----------
    education_score = 15 if parsed_data['education'] != "Not found" else 0
    breakdown['education'] = education_score
    score += education_score

    # ---------- EXPERIENCE (10 marks) ----------
    experience_score = 10 if parsed_data['experience'] != "Not found" else 0
    breakdown['experience'] = experience_score
    score += experience_score

    # ---------- FORMATTING (10 marks) ----------
    # Basic check: does the resume have a reasonable amount of text?
    # Too short usually means poor formatting/content
    word_count = len(parsed_data['raw_text'].split())
    formatting_score = 10 if word_count > 150 else 5
    breakdown['formatting'] = formatting_score
    score += formatting_score

    return {
        'total_score': score,
        'breakdown': breakdown
    }


def get_performance_label(score):
    """
    Converts the numeric score into a friendly label.
    """
    if score >= 85:
        return "Excellent"
    elif score >= 65:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Poor"


def generate_suggestions(parsed_data, breakdown):
    """
    Generates a list of improvement suggestions based on what's missing
    or weak in the resume.
    """
    suggestions = []

    if breakdown['contact'] < 20:
        suggestions.append("Add both a professional email and phone number.")

    if 'GitHub' not in parsed_data['skills']:
        suggestions.append("Add your GitHub profile link to showcase your code.")

    if breakdown['skills'] < 15:
        suggestions.append("List more relevant technical skills clearly in a dedicated section.")

    if breakdown['projects'] < 20:
        suggestions.append("Add more detailed project descriptions with technologies used.")

    if breakdown['education'] == 0:
        suggestions.append("Add a clear Education section with your degree and institution.")

    if breakdown['experience'] == 0:
        suggestions.append("Add any internships, part-time work, or relevant experience.")

    if breakdown['formatting'] < 10:
        suggestions.append("Expand your resume with more detail - it looks too short.")

    if not suggestions:
        suggestions.append("Great job! Your resume covers all the key areas well.")

    return suggestions


# Test this file directly: python utils/scorer.py
if __name__ == '__main__':
    import sys
    sys.path.append('.')
    from utils.resume_parser import parse_resume

    if len(sys.argv) > 1:
        parsed = parse_resume(sys.argv[1])
        result = calculate_score(parsed)
        label = get_performance_label(result['total_score'])
        suggestions = generate_suggestions(parsed, result['breakdown'])

        print(f"Total Score: {result['total_score']}/100")
        print(f"Performance: {label}")
        print(f"Breakdown: {result['breakdown']}")
        print("Suggestions:")
        for s in suggestions:
            print(f"  - {s}")