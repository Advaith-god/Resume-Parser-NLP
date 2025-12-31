import re

# Load resume text
with open("sample_resume.txt", "r") as file:
    text = file.read()

# Extract email
email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

# Extract phone number
phone = re.findall(r"\b\d{10}\b", text)

# Extract name (basic heuristic)
lines = text.split("\n")
name = lines[0] if lines else "Not Found"

# Extract skills
skills_list = [
    "python", "machine learning", "nlp", "sql", "java",
    "javascript", "data analysis", "deep learning"
]

found_skills = []
for skill in skills_list:
    if re.search(rf"\b{skill}\b", text.lower()):
        found_skills.append(skill.capitalize())

# Output parsed data
print("📄 Parsed Resume Details\n")
print("Name:", name)
print("Email:", email[0] if email else "Not Found")
print("Phone:", phone[0] if phone else "Not Found")
print("Skills:", ", ".join(found_skills) if found_skills else "Not Found")
