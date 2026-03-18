import os

print("🚀 Starting Resume Automation...\n")

# Step 1: Fetch GitHub data
print("📡 Fetching GitHub data...")
os.system("python scripts/fetch_github.py")

# Step 2: Generate Resume
print("\n📝 Generating Resume...")
os.system("python scripts/generate_resume.py")

print("\n✅ Resume updated successfully!")
