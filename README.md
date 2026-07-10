# 💬 Sentiment Analysis Web Application

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-orange)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-red?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)
![Render](https://img.shields.io/badge/Render-Deployed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

# 🌐 Live Demo

🚀 **Try the application here**

### https://sentiment-analysis-web-app-oe8k.onrender.com/

---

# 📖 Project Overview

The **Sentiment Analysis Web Application** is a Flask-based Natural Language Processing (NLP) project that analyzes user-entered text and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral**.

The application uses the **TextBlob** library to calculate:

- Sentiment Classification
- Polarity Score
- Subjectivity Score

The system provides real-time sentiment analysis through a clean and responsive web interface.

---

# 🎯 QSkill Internship Objective

This project was developed as part of the **QSkill Python Development Internship**.

### Problem Statement

Develop a web application using **Flask** or **Django** that:

- Accepts text input from users
- Performs sentiment analysis using TextBlob
- Displays Positive, Negative or Neutral sentiment
- Shows Polarity Score
- Shows Subjectivity Score

---

# 🚀 Features

✅ Professional Flask Web Application

✅ Real-Time Sentiment Analysis

✅ Positive Detection

✅ Negative Detection

✅ Neutral Detection

✅ Polarity Score

✅ Subjectivity Score

✅ Beautiful Responsive UI

✅ Input Validation

✅ Render Deployment

✅ GitHub Ready

---

# 🛠 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Backend | Flask |
| NLP Library | TextBlob |
| Frontend | HTML5 |
| Styling | CSS3 |
| Template Engine | Jinja2 |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 🧠 What is Sentiment Analysis?

Sentiment Analysis is a Natural Language Processing (NLP) technique used to determine whether a piece of text expresses a positive, negative, or neutral opinion.

Example:

Positive:

```
This application is amazing.
```

Negative:

```
I don't like this website.
```

Neutral:

```
The meeting starts at 10 AM.
```

---

# 📊 Understanding the Scores

## Polarity

Measures emotional orientation.

Range:

```
-1.0  ← Negative

 0.0  ← Neutral

+1.0  ← Positive
```

---

## Subjectivity

Measures whether text expresses facts or opinions.

Range:

```
0.0 → Objective

1.0 → Subjective
```

---

# ⚙ Project Workflow

```
User enters text
        │
        ▼
Flask receives input
        │
        ▼
Input Validation
        │
        ▼
TextBlob Processing
        │
        ▼
Calculate Polarity
        │
        ▼
Calculate Subjectivity
        │
        ▼
Determine Sentiment
        │
        ▼
Display Results
```

---

# 🏗 System Architecture

```
          User
            │
            ▼
      Flask Web App
            │
            ▼
       TextBlob NLP
            │
     ┌──────┴──────┐
     │             │
Polarity     Subjectivity
     │             │
     └──────┬──────┘
            │
            ▼
 Sentiment Classification
            │
            ▼
      Browser Display
```

---

# 📂 Project Structure

```
Sentiment_Analysis_Web_App
│
├── static
│   └── css
│       └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 💻 Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project

```bash
cd Sentiment_Analysis_Web_App
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

Run Flask Application

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 🌍 Deployment

The application is deployed on **Render**.

### Live URL

https://sentiment-analysis-web-app-oe8k.onrender.com/

---

# 📋 Example Inputs

### Positive

```
This project is amazing.
```

Output

```
Positive

Polarity: 0.6

Subjectivity: 0.9
```

---

### Negative

```
This service is terrible.
```

Output

```
Negative

Polarity: -0.8

Subjectivity: 0.9
```

---

### Neutral

```
The train leaves at 8 PM.
```

Output

```
Neutral

Polarity: 0.0

Subjectivity: 0.0
```

---

# 🎯 Applications

- Customer Feedback Analysis

- Product Review Analysis

- Social Media Monitoring

- Opinion Mining

- Brand Monitoring

- Survey Analysis

- Business Intelligence

---

# 📈 Future Improvements

- Multi-language Support

- Voice Input

- Sentiment History

- Database Integration

- User Authentication

- Dashboard Analytics

- AI-powered Emotion Detection

- Transformer Models (BERT)

- Docker Deployment

---

# 📚 Learning Outcomes

Through this project, I learned:

- Flask Web Development

- Natural Language Processing

- TextBlob Library

- Sentiment Analysis

- HTML & CSS Integration

- Jinja2 Templates

- Git & GitHub

- Render Deployment

- Full Project Deployment Workflow

---

# 👨‍💻 Author

## Kamal Solanki

**Computer Science & Engineering**

**3rd Year**

**SAL Institute of Technology Engineering & Research**

---

# 🔗 Project Links

### 🌐 Live Application

https://sentiment-analysis-web-app-oe8k.onrender.com/

### 💻 GitHub Repository

YOUR_GITHUB_REPOSITORY_LINK

---

# ⭐ Support

If you found this project useful,

please consider giving it a ⭐ on GitHub.

It helps support future open-source projects.

---

# 📄 License

This project is licensed under the MIT License.

---

#  Thank You

Thank you for visiting this repository.

Feel free to fork, contribute, and improve this project.