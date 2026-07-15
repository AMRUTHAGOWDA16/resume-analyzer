# utils/report_generator.py
# Generates a downloadable PDF report summarizing the resume analysis

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os


def generate_pdf_report(record, skills, breakdown, suggestions, output_path):
    """
    Creates a PDF file summarizing the resume analysis.

    record      - the database row (dictionary-like) with candidate info and score
    skills      - list of detected skills
    breakdown   - dictionary of score breakdown by category
    suggestions - list of improvement suggestions
    output_path - where to save the generated PDF file
    """
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                             topMargin=20*mm, bottomMargin=20*mm)
    styles = getSampleStyleSheet()

    # Custom style for the main title
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Title'], fontSize=22,
        textColor=colors.HexColor('#203a43'), spaceAfter=10
    )
    heading_style = ParagraphStyle(
        'HeadingStyle', parent=styles['Heading2'], fontSize=14,
        textColor=colors.HexColor('#203a43'), spaceBefore=14, spaceAfter=6
    )
    normal_style = styles['Normal']

    elements = []

    # ---------- TITLE ----------
    elements.append(Paragraph("Resume Analysis Report", title_style))
    elements.append(Spacer(1, 10))

    # ---------- CANDIDATE INFO ----------
    elements.append(Paragraph("Candidate Information", heading_style))
    info_data = [
        ["Name", record['candidate_name']],
        ["Email", record['email']],
        ["Phone", record['phone']],
        ["File", record['filename']],
    ]
    info_table = Table(info_data, colWidths=[100, 350])
    info_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#203a43')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ]))
    elements.append(info_table)

    # ---------- SCORE ----------
    elements.append(Paragraph("Overall Score", heading_style))
    elements.append(Paragraph(
        f"<b>{record['score']} / 100</b> &nbsp;&nbsp; ({record['performance_label']})",
        normal_style
    ))

    # ---------- SCORE BREAKDOWN ----------
    elements.append(Paragraph("Score Breakdown", heading_style))
    breakdown_data = [["Category", "Score"]]
    max_marks = {
        'contact': 20, 'skills': 25, 'projects': 20,
        'education': 15, 'experience': 10, 'formatting': 10
    }
    for key, value in breakdown.items():
        breakdown_data.append([key.capitalize(), f"{value}/{max_marks.get(key, '')}"])

    breakdown_table = Table(breakdown_data, colWidths=[250, 100])
    breakdown_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#203a43')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(breakdown_table)

    # ---------- SKILLS ----------
    elements.append(Paragraph("Detected Skills", heading_style))
    skills_text = ", ".join(skills) if skills else "No skills detected."
    elements.append(Paragraph(skills_text, normal_style))

    # ---------- SUGGESTIONS ----------
    elements.append(Paragraph("Suggestions for Improvement", heading_style))
    for suggestion in suggestions:
        elements.append(Paragraph(f"• {suggestion}", normal_style))

    # Build and save the PDF file
    doc.build(elements)
    return output_path