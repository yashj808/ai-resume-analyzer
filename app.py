import os
import io
from flask import Flask, render_template, request
from resume_checker import analyze_resume

import pdfplumber
import pytesseract
from PIL import Image

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting PDF: {e}")
    return text


# -------- IMAGE OCR EXTRACTION --------
def extract_text_from_image(file):
    try:
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error performing OCR on image: {e}")
        return ""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        job_desc = request.form.get("job_desc", "")
        resume_text = ""

        # -------- EXTRACT RESUME FROM FILE --------
        if "resume_file" in request.files:
            file = request.files["resume_file"]
            if file and file.filename != "":
                filename = file.filename.lower()

                # PDF
                if filename.endswith(".pdf"):
                    resume_text = extract_text_from_pdf(file)

                # Image
                elif filename.endswith((".png", ".jpg", ".jpeg")):
                    resume_text = extract_text_from_image(file)

        # -------- ANALYZE RESUME --------
        if resume_text.strip() and job_desc:
            result = analyze_resume(resume_text, job_desc)
        elif job_desc and not resume_text.strip():
            result = {
                "resume_score": 0,
                "match_score": 0,
                "skills": [],
                "all_resume_skills": [],
                "missing": [],
                "suggestions": [
                    "Could not extract readable text from the uploaded file.",
                    "Please upload a standard text PDF or clear image of your resume."
                ],
                "radar_labels": ["Technical Skills", "Tools", "Problem Solving", "Architecture", "Testing"],
                "radar_values": [0, 0, 0, 0, 0]
            }

    return render_template("index.html", result=result)


# -------- RUN SERVER --------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
