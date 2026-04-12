import requests
import json
from collections import Counter

username = "Ayushraj2319"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()

    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    projects = []
    languages = []

    for repo in repos:
        projects.append(repo["name"])

        if repo["language"]:
            languages.append(repo["language"])

    skill_count = Counter(languages)
    top_skills = [skill for skill, _ in skill_count.most_common(5)]

    data = {
        "name": "Ayush Raj",
        "role": "DevOps Enthusiast",
        "github": "https://github.com/Ayushraj2319",
        "linkedin": "https://linkedin.com/in/YOUR_LINKEDIN",
        "projects": projects[:5],
        "skills": top_skills
    }

    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Clean resume data ready ✅")
else:
    print("Error fetching data")
