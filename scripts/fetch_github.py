import requests
import json
import os
from collections import Counter

username = input("Enter GitHub username: ").strip()

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github+json"
}

if token:
    headers["Authorization"] = f"Bearer {token}"

user_url = f"https://api.github.com/users/{username}"
repo_url = f"https://api.github.com/users/{username}/repos"

user_res = requests.get(user_url, headers=headers)
repo_res = requests.get(repo_url, headers=headers)

if user_res.status_code == 200 and repo_res.status_code == 200:

    user_data = user_res.json()
    repos = repo_res.json()

    avatar = user_data.get("avatar_url") or "https://via.placeholder.com/120"
    bio = user_data.get("bio") or "Passionate developer with interest in DevOps and automation."

    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    projects = []
    languages = []

    for repo in repos:
        projects.append({
            "name": repo.get("name", ""),
            "desc": repo.get("description") or "No description available",
            "url": repo.get("html_url", "#")
        })

        if repo.get("language"):
            languages.append(repo["language"])

    if not languages:
        languages = ["Python", "Git", "Automation"]

    skill_count = Counter(languages)
    top_skills = [skill for skill, _ in skill_count.most_common(5)]

    data = {
        "name": username,
        "role": "DevOps Enthusiast",
        "github": f"https://github.com/{username}",
        "linkedin": "https://linkedin.com/in/YOUR_LINKEDIN",
        "avatar": avatar,
        "bio": bio,
        "projects": projects[:5],
        "skills": top_skills,
        "education": [
            "B.Tech in Computer Science - KIET Group of Institutions"
        ],
        "experience": [
            "Built automated resume system using CI/CD pipelines",
            "Integrated GitHub API for dynamic data fetching",
            "Implemented scheduled automation using GitHub Actions"
        ]
    }

    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Data generated successfully!")

else:
    print("❌ Failed to fetch data")
