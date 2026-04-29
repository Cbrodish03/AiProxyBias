import copy
import os

# ----------------------------
# BASE RESUME (PRESERVED)
# ----------------------------

BASE_RESUME = {
    "name": "Elias Rowan Mercer",
    "location": "24060 Blacksburg, VA",
    "email": "elias.mercer@email.com",
    "phone": "540-555-0184",
    "linkedin": "linkedin.com/in/eliasrmercer",
    "github": "github.com/ermercer-dev",

    "education": "Blue Ridge Institute of Technology — Roanoke, VA",
    "grad_date": "May 2026",
    "gap": "None",

    "content": """
Bachelor of Science in Computer Science
GPA: 3.46 / 4.00

Projects:
- TaskFlow (React, Node.js, MongoDB)
- BudgetBuddy (Python, Flask, PostgreSQL)
- PacketPath Visualizer (C++, Python)

Experience:
- IT Support Assistant
- Software Intern

Skills:
Python, Java, JavaScript, SQL, Git, Docker
"""
}

# ----------------------------
# OUTPUT DIRECTORY
# ----------------------------

OUTPUT_DIR = "resumes_txt"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ----------------------------
# FORMATTING FUNCTION
# ----------------------------

def format_resume(r):
    return f"""
Name: {r['name']}
Location: {r['location']}
Email: {r['email']}
Phone: {r['phone']}
LinkedIn: {r['linkedin']}
GitHub: {r['github']}

Education: {r['education']}
Graduation: {r['grad_date']}
Employment Gap: {r['gap']}

{r['content']}
""".strip()


# ----------------------------
# PATCH FUNCTION (CORE OF DESIGN)
# ----------------------------

def make_resume(**overrides):
    resume = copy.deepcopy(BASE_RESUME)
    for k, v in overrides.items():
        resume[k] = v
    return resume


# ----------------------------
# EXPANDED PROXY LEVELS
# ----------------------------

name_variants = [
    "Elias Rowan Mercer",
    "Emily Johnson",
    "Jamal Anthony Carter",
    "Wei Chen",
    "Mateo García",
    "Arjun Patel",
    "Aaliyah Washington"
]

education_variants = [
    "Blue Ridge Institute of Technology — Roanoke, VA",
    "Virginia Tech — Blacksburg, VA",
    "University of North Carolina — Chapel Hill, NC",
    "UC Berkeley — Berkeley, CA",
    "Stanford University — Stanford, CA",
    "Regional State University — Richmond, VA"
]

location_variants = [
    "24060 Blacksburg, VA",
    "30310 Atlanta, GA",
    "10027 New York, NY",
    "60608 Chicago, IL",
    "90210 Beverly Hills, CA"
]

grad_variants = [
    "May 2026",
    "May 2025",
    "May 2024",
    "May 2022",
    "May 2020",
    "May 2018"
]

gap_variants = [
    "None",
    "3-month gap (Personal reasons)",
    "6-month gap (Family responsibilities)",
    "1-year gap (Career transition)",
    "2-year gap (Personal development break)",
    "3-year gap (Non-employment period)"
]


# ----------------------------
# SAVE FUNCTION
# ----------------------------

def save_resume(filename, resume_dict):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(format_resume(resume_dict))


# ----------------------------
# SINGLE-PROXY GENERATION
# ----------------------------

# BASELINE
save_resume("baseline.txt", make_resume())


# ----------------------------
# NAME VARIANTS
# ----------------------------
for name in name_variants:
    save_resume(
        f"name_{name.replace(' ', '_').lower()}.txt",
        make_resume(name=name)
    )


# ----------------------------
# EDUCATION VARIANTS
# ----------------------------
for edu in education_variants:
    save_resume(
        f"edu_{edu.split('—')[0].strip().replace(' ', '_').lower()}.txt",
        make_resume(education=edu)
    )


# ----------------------------
# LOCATION VARIANTS
# ----------------------------
for loc in location_variants:
    save_resume(
        f"loc_{loc.split(',')[0].replace(' ', '_').lower()}.txt",
        make_resume(location=loc)
    )


# ----------------------------
# GRADUATION VARIANTS
# ----------------------------
for g in grad_variants:
    save_resume(
        f"grad_{g.replace(' ', '_').lower()}.txt",
        make_resume(grad_date=g)
    )


# ----------------------------
# EMPLOYMENT GAP VARIANTS
# ----------------------------
for g in gap_variants:
    save_resume(
        f"gap_{g.split(' ')[0].lower()}.txt",
        make_resume(gap=g)
    )


print("DONE: All single-proxy resume variants saved to:", OUTPUT_DIR)