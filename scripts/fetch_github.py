import requests
import json
import os
from collections import Counter

def fetch_data(username):
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

    if user_res.status_code != 200 or repo_res.status_code != 200:
        print("❌ Failed to fetch data")
        return {}

    user_data = user_res.json()
    repos = repo_res.json()

    # 🔹 Basic Info
    avatar = user_data.get("avatar_url") or "https://via.placeholder.com/120"
    bio = user_data.get("bio") or "Passionate developer with interest in DevOps and automation."

    # 🔹 Sort repos by latest update
    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    projects = []
    languages = []

    for repo in repos:
        projects.append({
            "name": repo.get("name", ""),
            "description": repo.get("description") or "No description available",
            "url": repo.get("html_url", "#")
        })

        if repo.get("language"):
            languages.append(repo["language"])

    # 🔹 Default skills if none found
    if not languages:
        languages = ["Python", "Git", "Automation"]

    skill_count = Counter(languages)
    top_skills = [skill for skill, _ in skill_count.most_common(5)]

    # 🔹 Final Data
    data = {
        "name": user_data.get("name") or username,
        "role": "DevOps Enthusiast",
        "github_username": username,
        "github_url": f"https://github.com/{username}",
        "linkedin": "your-linkedin-id",  # 🔥 CHANGE THIS
        "avatar": avatar,
        "summary": bio,
        "repos": projects[:5],
        "skills": top_skills
    }

    # 🔹 Save JSON (optional backup)
    os.makedirs("data", exist_ok=True)
    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Data generated successfully!")

    return data


# 🔥 For standalone testing
if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    fetch_data(username)
