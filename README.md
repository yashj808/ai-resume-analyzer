# AI Resume Analyzer

AI Resume Analyzer is a web application that analyzes resumes against job descriptions to help candidates improve their chances of passing Applicant Tracking Systems (ATS).

The system extracts text from resumes, detects relevant skills, identifies missing skills based on job descriptions, and provides actionable suggestions to improve the resume.

## Live Demo

The application is deployed on Render.

Live Application:
https://ai-resume-analyzer-ugm0.onrender.com



## Features

- ATS-style resume scoring
- Job description matching
- Automatic skill detection
- Missing skills analysis
- Dynamic skill radar chart visualization
- Actionable resume improvement suggestions
- Resume file upload support (PDF / image)
- OCR-based text extraction for scanned resumes



## Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- Chart.js

### Resume Processing
- pdfplumber
- Tesseract OCR
- Pillow

### Deployment
- Render (Cloud Hosting)
- GitHub (Version Control)



## Installation

Clone the repository:
```bash
git clone https://github.com/rutvanj/ai-resume-analyzer.git
cd ai-resume-analyzer
```

Install dependencies:
```bash
pip install -r requirements.txt
```



## Running the Application Locally

Start the Flask server:
```bash
python app.py
```

Open your browser and go to:
http://127.0.0.1:5000



## Deployment

The backend is deployed on Render.
Render automatically redeploys the application when new code is pushed to GitHub.



## Future Improvements

- AI-based resume rewriting
- ATS keyword optimization
- NLP-based resume scoring
- Job recommendation engine



## Author

Rutva Jakhiya
B.Tech Information Technology
A. D. Patel Institute of Technology
