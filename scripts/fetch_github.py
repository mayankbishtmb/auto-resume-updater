import requests
import json

# 🔥 Function to clean project names
def clean_project_name(name):
    return name.replace("-", " ").replace("_", " ").title()

username = "Ayushraj2319"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

projects = []
languages = set()

if response.status_code == 200:
    repos = response.json()

    # Sort repos by latest update
    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    for repo in repos:
        # Clean project name
        clean_name = clean_project_name(repo["name"])
        projects.append(clean_name)

        # Add skills (ignore None)
        if repo["language"]:
            languages.add(repo["language"])

    # Final structured data
    data = {
        "name": "Ayush Raj",
        "role": "DevOps Enthusiast",
        "projects": projects[:5],
        "skills": sorted(list(languages))
    }

    # Save to JSON file
    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Clean resume data ready ✅")

else:
    print("Error fetching data")

