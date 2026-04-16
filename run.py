import os
import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from scripts.fetch_github import fetch_data

print("🚀 Starting Resume Automation...\n")

# 🔹 Step 1: Fetch GitHub Data
print("📡 Fetching GitHub data...")
username = input("Enter GitHub username: ").strip()

data = fetch_data(username)

if not data:
    print("❌ Stopping due to error.")
    exit()

# 🔹 Step 2: Generate Resume Website
print("\n📝 Generating Resume Website...")

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume.html")

output = template.render(data)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ index.html generated")

# 🔹 Step 3: (Optional) Keep PDF if exists
if os.path.exists("resume.pdf"):
    print("📄 Resume PDF already exists")
else:
    print("⚠️ No resume.pdf found (optional)")

# 🔹 Step 4: Email Notification
print("\n📧 Sending email notification...")

sender_email = os.getenv("EMAIL_USER")
receiver_email = sender_email
app_password = os.getenv("EMAIL_PASS")

if sender_email and app_password:
    message = MIMEText("✅ Your resume website has been updated successfully!")
    message["Subject"] = "Resume Updated"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)
        server.quit()
        print("✅ Email sent successfully")
    except Exception as e:
        print("❌ Email failed:", e)
else:
    print("⚠️ Email skipped (no credentials set)")

print("\n🎉 Resume Website Updated Successfully!")
