from jinja2 import Template
import json
from weasyprint import HTML

with open("data/github_data.json") as f:
    data = json.load(f)

with open("data/linkedin.json") as f:
    linkedin_data = json.load(f)

total_projects = len(data.get("projects", []))
total_skills = len(data.get("skills", []))

with open("templates/resume.html") as f:
    template = Template(f.read())

output = template.render(
    name=data.get("name", ""),
    role=data.get("role", ""),
    skills=data.get("skills", []),
    projects=data.get("projects", []),
    github=data.get("github", "#"),
    linkedin=data.get("linkedin", "#"),
    experience=linkedin_data.get("experience", []),
    education=linkedin_data.get("education", []),
    total_projects=total_projects,
    total_skills=total_skills
)

with open("output/resume.html", "w") as f:
    f.write(output)

HTML(string=output).write_pdf("output/resume.pdf")

print("Resume generated with advanced features ✅")
