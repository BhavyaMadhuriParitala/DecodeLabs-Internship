# Job Recommendation System

jobs = {
    "Data Scientist": ["Python", "Machine Learning", "SQL", "Statistics"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "Artificial Intelligence"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "TensorFlow", "Deep Learning"],
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI"],
    "Software Developer": ["Python", "Java", "Git", "C Programming"],
    "Backend Developer": ["Python", "SQL", "Git", "API Development"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "Python"],
    "Cloud Engineer": ["AWS", "Python", "Linux"],
    "DevOps Engineer": ["Linux", "Python", "Docker", "Git"],
    "Cyber Security Analyst": ["Python", "Networking", "Linux"],
    "Embedded Systems Engineer": ["C Programming", "Microcontrollers", "Electronics"],
    "IoT Engineer": ["C Programming", "Python", "Embedded Systems"],
    "Game Developer": ["C++", "C Programming", "Unity"],
    "Mobile App Developer": ["Java", "Kotlin", "Android"],
    "Database Administrator": ["SQL", "Database Management"],
    "Business Intelligence Analyst": ["Power BI", "SQL", "Excel"],
    "Computer Vision Engineer": ["Python", "Machine Learning", "OpenCV"],
    "NLP Engineer": ["Python", "Machine Learning", "Artificial Intelligence"],
    "Robotics Engineer": ["Python", "C Programming", "Machine Learning"],
    "Research Assistant (AI)": ["Python", "Machine Learning", "Artificial Intelligence"],
    # Arts & Design
    "Graphic Designer": ["Photoshop", "Illustrator", "Creativity"],
    "UI/UX Designer": ["Figma", "Wireframing", "User Research"],
    "Animator": ["Animation", "Creativity", "Storyboarding"],
    "Fashion Designer": ["Creativity", "Fashion Design", "Sketching"],

    # Media & Communication
    "Content Writer": ["Writing", "Creativity", "Research"],
    "Journalist": ["Writing", "Communication", "Research"],
    "Digital Marketing Specialist": ["SEO", "Content Marketing", "Social Media"],
    "Public Relations Officer": ["Communication", "Writing", "Networking"],

    # Commerce & Business
    "Accountant": ["Accounting", "Excel", "Taxation"],
    "Financial Analyst": ["Finance", "Excel", "Statistics"],
    "Investment Banker": ["Finance", "Economics", "Communication"],
    "Business Analyst": ["Excel", "Communication", "Problem Solving"],
    "Human Resources Manager": ["Communication", "Recruitment", "Leadership"],
    "Sales Executive": ["Communication", "Negotiation", "Marketing"],

    # Law
    "Lawyer": ["Legal Research", "Communication", "Law"],
    "Legal Advisor": ["Law", "Legal Research", "Drafting"],
    "Judge": ["Law", "Legal Research", "Decision Making"],

    # Science
    "Research Scientist": ["Research", "Statistics", "Scientific Writing"],
    "Biotechnologist": ["Biology", "Research", "Laboratory Skills"],
    "Chemist": ["Chemistry", "Laboratory Skills"],
    "Physicist": ["Physics", "Mathematics", "Research"],
    "Environmental Scientist": ["Environmental Science", "Research"],

    # Healthcare
    "Doctor": ["Biology", "Medicine", "Patient Care"],
    "Nurse": ["Patient Care", "Biology", "Communication"],
    "Pharmacist": ["Medicine", "Chemistry", "Patient Care"],
    "Physiotherapist": ["Patient Care", "Biology"],

    # Education
    "Teacher": ["Teaching", "Communication", "Subject Knowledge"],
    "Professor": ["Teaching", "Research", "Communication"],
    "School Counselor": ["Counseling", "Communication", "Psychology"],

    # Government & Civil Services
    "Civil Servant": ["General Knowledge", "Leadership", "Communication"],
    "Police Officer": ["Leadership", "Physical Fitness", "Communication"],
    "Foreign Service Officer": ["Communication", "International Relations"],
    "Defense Officer": ["Leadership", "Discipline", "Decision Making"],

    # Hospitality & Tourism
    "Hotel Manager": ["Management", "Communication", "Customer Service"],
    "Tour Guide": ["Communication", "History", "Customer Service"],
    "Event Manager": ["Management", "Communication", "Planning"],

    # Psychology & Social Work
    "Psychologist": ["Psychology", "Counseling", "Communication"],
    "Social Worker": ["Communication", "Empathy", "Community Service"],

    # Agriculture
    "Agricultural Officer": ["Agriculture", "Research"],
    "Agronomist": ["Agriculture", "Research", "Biology"],

    # Architecture
    "Architect": ["AutoCAD", "Creativity", "Mathematics"],
    "Interior Designer": ["Creativity", "Design", "Communication"]
}

print("================================")
print(" AI JOB RECOMMENDATION SYSTEM ")
print("================================")

print("\nEnter your skills separated by commas")

user_input = input("Skills: ")

skill_alias = {
    "py": "Python",
    "python": "Python",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",

    "dbms": "Database Management",
    "database": "Database Management",

    "sql": "SQL",

    "c": "C Programming",
    "c++": "C++",

    "java": "Java",

    "aws": "AWS",

    "dl": "Deep Learning",
    "deep learning": "Deep Learning",
    
    "communication": "Communication",
    "writing": "Writing",
    "research": "Research",
    "finance": "Finance",
    "accounting": "Accounting",
    "law": "Law",
    "biology": "Biology",
    "chemistry": "Chemistry",
    "physics": "Physics",
    "psychology": "Psychology",
    "teaching": "Teaching",
    "leadership": "Leadership",
    "management": "Management",
    "marketing": "Marketing",
    "seo": "SEO",
    "design": "Design",
    "creativity": "Creativity",
    "customer service": "Customer Service",
    "agriculture": "Agriculture"
}

user_skills = []

for skill in user_input.split(","):

    skill = skill.strip().lower()

    if skill in skill_alias:
        user_skills.append(skill_alias[skill])
    else:
        user_skills.append(skill.title())

recommendations = []

for job, skills in jobs.items():

    score = 0

    matched_skills = []

    for skill in user_skills:
        if skill in skills:
            score += 1
            matched_skills.append(skill)

    match_percent = (score / len(skills)) * 100

    recommendations.append(
        (job, score, matched_skills, match_percent)
    )

recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\n===== Recommended Jobs =====\n")

found = False
fully_suitable_jobs = []

for job, skills in jobs.items():
    if all(skill in user_skills for skill in skills):
        fully_suitable_jobs.append(job)
        found = True

print("\nTop Recommended Jobs:\n")

for job, score, matched_skills, match_percent in recommendations[:5]:
    print(f"Job: {job}")
    print(f"Match Score: {score}")
    print(f"Match Percentage: {match_percent:.2f}%")
    print(f"Matched Skills: {', '.join(matched_skills)}")
    print("-" * 40)

print()

if fully_suitable_jobs:
    print("===== Fully Suitable Jobs =====\n")

    for job in fully_suitable_jobs:
        print(f"{job} is fully suitable for your present skills.")
else:
    print("Fully suitable jobs are not found.")
    print("Semi suitable jobs are found based on your matching skills.")