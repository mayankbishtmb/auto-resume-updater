import requests
import json
import os
from collections import Counter

username = input("Enter GitHub username: ").strip()

# 🔥 GET TOKEN
token = os.getenv("GITHUB_TOKEN")

# 🔥 HEADERS (IMPORTANT FIX)
headers = {
    "Accept": "application/vnd.github+json"
}

if token:
    headers["Authorization"] = f"Bearer {token}"

print("Using token:", "YES" if token else "NO")

# API URLs
user_url = f"https://api.github.com/users/{username}"
repo_url = f"https://api.github.com/users/{username}/repos"

print("Fetching data from GitHub...")

user_res = requests.get(user_url, headers=headers)
repo_res = requests.get(repo_url, headers=headers)

print("User API status:", user_res.status_code)
print("Repo API status:", repo_res.status_code)

if user_res.status_code == 200 and repo_res.status_code == 200:

    user_data = user_res.json()
    repos = repo_res.json()

    avatar = user_data.get("avatar_url", "")
    bio = user_data.get("bio", "No bio available")

    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    projects = []
    languages = []

    for repo in repos:
        projects.append(repo.get("name", ""))

        if repo.get("language"):
            languages.append(repo["language"])

    if not languages:
        languages = ["GitHub", "Open Source"]

    skill_count = Counter(languages)
    top_skills = [skill for skill, _ in skill_count.most_common(5)]

    data = {
        "name": username,
        "role": "GitHub Developer",
        "github": f"https://github.com/{username}",
        "linkedin": "https://linkedin.com/in/YOUR_LINKEDIN",
        "avatar": avatar,
        "bio": bio,
        "projects": projects[:5],
        "skills": top_skills
    }

    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Data generated successfully!")

else:
    print("❌ Failed to fetch data")
    print("User response:", user_res.text)
