from jinja2 import Template
import json
from weasyprint import HTML

# Load GitHub data
with open("data/github_data.json") as f:
    data = json.load(f)

# Load LinkedIn data
with open("data/linkedin.json") as f:
    linkedin_data = json.load(f)

# Load template
with open("templates/resume.html") as f:
    template = Template(f.read())

# Render HTML
output = template.render(
    name=data.get("name", ""),
    role=data.get("role", ""),
    skills=data.get("skills", []),
    projects=data.get("projects", []),
    github=data.get("github", "#"),
    linkedin=data.get("linkedin", "#"),
    experience=linkedin_data.get("experience", []),
    education=linkedin_data.get("education", [])
)

# Save HTML
with open("output/resume.html", "w") as f:
    f.write(output)

# Generate PDF
HTML(string=output).write_pdf("output/resume.pdf")

print("Resume with LinkedIn data generated successfully ✅")
