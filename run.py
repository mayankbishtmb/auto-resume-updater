import os
import shutil
import smtplib
from email.mime.text import MIMEText

print("🚀 Starting Resume Automation...\n")

# Step 1: Fetch GitHub data
print("📡 Fetching GitHub data...")
os.system("python3 scripts/fetch_github.py")

# Step 2: Generate Resume
print("\n📝 Generating Resume...")
os.system("python3 scripts/generate_resume.py")

# Step 3: Update Website
print("\n🌐 Updating website...")
shutil.copy("output/resume.html", "index.html")
shutil.copy("output/resume.pdf", "resume.pdf")

# Step 4: Email Notification (SAFE VERSION)
print("\n📧 Sending email notification...")

sender_email = os.getenv("EMAIL_USER")
receiver_email = sender_email
app_password = os.getenv("EMAIL_PASS")

if sender_email and app_password:
    message = MIMEText("Your resume has been updated successfully!")
    message["Subject"] = "Resume Update"
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

print("\n✅ Resume & website updated successfully!")
