# Skill-Based Career Recommendation System 🚀

## Overview

The **Skill-Based Career Recommendation System** is a Python-based application that recommends suitable career paths based on a user's skills. The system analyzes the skills entered by the user, compares them with predefined job requirements, and generates ranked job recommendations.

The project supports both **technical** and **non-technical** career domains, making it useful for students and professionals from diverse backgrounds such as Technology, Business, Science, Arts, Law, Healthcare, Education, and more.

---

## Features

✅ Accepts multiple skills as user input

✅ Supports skill aliases (e.g., `py` → Python, `ml` → Machine Learning)

✅ Calculates match scores for each job

✅ Calculates match percentages

✅ Displays Top Recommended Jobs

✅ Identifies Fully Suitable Jobs

✅ Identifies Semi-Suitable Jobs when no complete match is found

✅ Supports both Technical and Non-Technical Career Paths

✅ Easy to expand with new jobs and skills

---

## Technologies Used

* Python 3
* Dictionaries
* Lists
* Loops
* Conditional Statements
* Sorting Algorithms

---

## How It Works

1. User enters skills separated by commas.
2. The system normalizes the skills using predefined aliases.
3. Each job role is compared against the user's skills.
4. A match score and match percentage are calculated.
5. Jobs are ranked according to the match score.
6. The system displays:

   * Top Recommended Jobs
   * Match Percentage
   * Matched Skills
   * Fully Suitable Jobs (if any)
   * Semi-Suitable Job Recommendations

---

## Example

### Input

```text
Skills: python, sql, machine learning
```

### Output

```text
Top Recommended Jobs:

Job: Data Scientist
Match Score: 3
Match Percentage: 75.00%
Matched Skills: Python, SQL, Machine Learning

Job: AI Engineer
Match Score: 2
Match Percentage: 50.00%
Matched Skills: Python, Machine Learning

Fully suitable jobs are not found.
Semi suitable jobs are found based on your matching skills.
```

---

## Supported Career Domains

### Technology

* Data Scientist
* AI Engineer
* Machine Learning Engineer
* Software Developer
* Backend Developer
* Full Stack Developer
* Cloud Engineer
* DevOps Engineer
* Cyber Security Analyst
* Database Administrator
* Computer Vision Engineer
* NLP Engineer
* Robotics Engineer

### Business & Commerce

* Accountant
* Financial Analyst
* Business Analyst
* Human Resources Manager
* Sales Executive

### Science

* Research Scientist
* Biotechnologist
* Chemist
* Physicist
* Environmental Scientist

### Healthcare

* Doctor
* Nurse
* Pharmacist
* Physiotherapist

### Law

* Lawyer
* Legal Advisor
* Judge

### Arts & Design

* Graphic Designer
* UI/UX Designer
* Animator
* Fashion Designer

### Media & Communication

* Content Writer
* Journalist
* Digital Marketing Specialist
* Public Relations Officer

### Education

* Teacher
* Professor
* School Counselor

### Government Services

* Civil Servant
* Police Officer
* Foreign Service Officer
* Defense Officer

### Hospitality & Tourism

* Hotel Manager
* Tour Guide
* Event Manager

### Psychology & Social Work

* Psychologist
* Social Worker

### Agriculture

* Agricultural Officer
* Agronomist

### Architecture & Design

* Architect
* Interior Designer

---

## Future Enhancements

* Missing Skills Detection
* Personalized Learning Roadmap
* Career Confidence Score
* Salary Range Estimation
* Career Descriptions
* Domain-Based Recommendations
* Graphical User Interface (GUI)
* Database Integration
* Machine Learning-Based Recommendations
* AI-Powered Career Advisor

---

## Project Structure

```text
career-recommendation-system/
│
├── main.py
├── README.md
└── requirements.txt (optional)
```

---

## Learning Outcomes

This project demonstrates:

* Python Programming Fundamentals
* Data Structures (Lists & Dictionaries)
* Algorithmic Thinking
* Data Processing
* Recommendation System Basics
* Career Guidance System Design

---

## Author

Developed as a learning project to explore recommendation systems, career guidance applications, and future AI-based career prediction models.

⭐ Future Goal: Transform this Skill-Based Recommendation System into an AI-Powered Career Recommendation Platform using Machine Learning.
