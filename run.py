import os
import shutil
import smtplib
from email.mime.text import MIMEText

print("🚀 Starting Resume Automation...\n")

os.system("python scripts/fetch_github.py")
os.system("python scripts/generate_resume.py")

shutil.copy("output/resume.html", "index.html")
shutil.copy("output/resume.pdf", "resume.pdf")

sender_email = os.getenv("EMAIL_USER")
receiver_email = sender_email
app_password = os.getenv("EMAIL_PASS")

message = MIMEText("Resume updated successfully!")
message["Subject"] = "Resume Update"
message["From"] = sender_email
message["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(message)
    server.quit()
    print("Email sent ✅")
except Exception as e:
    print("Email error:", e)
