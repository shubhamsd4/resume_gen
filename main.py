import streamlit as st
from openai import OpenAI
import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
import json
import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import prompts
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import subprocess
from jinja2 import Template
import os

# Function to extract text from uploaded PDF file
def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

openai_key = 'sk-proj-GUxknP9fVy2zr52SNBy2T3BlbkFJtZxH18MEL0rJzNIeVT9m'
client = OpenAI(api_key=openai_key)

def get_openai_response(system_prompt, user_prompt):
    resume_sections = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return resume_sections.choices[0].message.content

system_prompt = prompts.system_prompt
user_prompt = prompts.user_prompt

system_prompt_improve = prompts.system_prompt_improve
user_prompt_improve = prompts.user_prompt_improve

# Streamlit UI
st.title("Resume Generator")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
#template_file = st.file_uploader("Upload Resume Format (PDF)", type=["pdf"])
job_description = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

if resume_file and job_description:
    st.write("Processing the resume...")
    
    # Extract text from PDF
    resume_text = extract_text_from_pdf(resume_file)
    resume_json = get_openai_response(system_prompt, user_prompt.format(resume=resume_text)) 

    #Improved Resume JSON
    improved_resume_json = get_openai_response(system_prompt_improve, user_prompt_improve.format(resume_json = json.dumps(resume_json), job_description = job_description ))
 
    col1, col2 = st.columns(2)
    with col1:
        st.write("Resume JSON")
        st.write(resume_json)

    with col2:
        st.write("Improved Resume JSON")
        st.write(improved_resume_json)

    # Read LaTeX template
    with open('resume_template3.tex') as template_file:
        latex_template = template_file.read()


    def replace_placeholders(template, data):
        for key, value in data.items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    if isinstance(subvalue, dict):
                        replacement = json.dumps(subvalue)  # Convert dictionary to JSON string
                    elif isinstance(subvalue, list):
                        replacement = ', '.join(map(str, subvalue))  # Convert list to comma-separated string
                    else:
                        replacement = str(subvalue)
                    template = template.replace(f"\\VAR{{{key}.{subkey}}}", replacement)
            elif isinstance(value, list):
                if key in ["achievements", "certifications", "skills"]:
                    replacement = "\\begin{itemize}\n" + "\n".join([f"\\item {item}" for item in value]) + "\n\\end{itemize}"
                else:
                    replacement = "\\begin{itemize}\n" + "\n".join([f"\\item {', '.join(map(str, item.values()))}" for item in value]) + "\n\\end{itemize}"
                template = template.replace(f"\\VAR{{{key}}}", replacement)
            else:
                template = template.replace(f"\\VAR{{{key}}}", str(value))
        return template



    # Generate the LaTeX resume
    latex_resume = replace_placeholders(latex_template, json.loads(improved_resume_json))
    st.code(latex_resume, language='latex')
    
    # Save the LaTeX content to a .tex file
    filename = "generated_resume.tex"
    with open(filename, "w") as f:
        f.write(latex_resume)

    # Compile LaTeX file to PDF
    subprocess.run(["pdflatex", "generated_resume.tex"])

    # Allow the user to download the PDF
    with open("generated_resume.pdf", "rb") as pdf_file:
        st.download_button(label="Download Resume as PDF", data=pdf_file, file_name="resume.pdf")
