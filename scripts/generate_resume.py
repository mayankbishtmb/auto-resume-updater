from jinja2 import Template
import json
from weasyprint import HTML

with open("data/github_data.json") as f:
    data = json.load(f)

with open("templates/resume.html") as f:
    template = Template(f.read())

output = template.render(**data)

with open("output/resume.html", "w") as f:
    f.write(output)

HTML(string=output).write_pdf("output/resume.pdf")

print("✅ Resume generated")
