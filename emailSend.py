import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os
from dotenv import load_dotenv
import time

load_dotenv()

subject = "Seeking Guidance on Contract Review for University Project App"
html_body = """\
<html>
<body>
  <p>I hope this message finds you well. I'm reaching out about contracts for our university mentorship app project.</p>

  <p>Our original team of five brought on a legal/business advisor who's now drafting contracts. We need help understanding them.</p>

  <p>Can you:</p>
  <ol>
    <li>Point me to good contract review resources?</li>
    <li>Suggest key questions about:
      <ul>
        <li>Liability</li>
        <li>Money splits</li>
        <li>What happens if we lose/gain money</li>
      </ul>
    </li>
  </ol>

  <p>Need this simple and clear. Thanks.</p>
  <p>Best,<br>
  <strong>Tj Walsh</strong></p>
</body>
</html>
"""

sender = os.getenv("EA")
recipients = ["donal.gilligan.2024@mumail.ie","liam.king.2024@mumail.ie","thomas.walsh.2024@mumail.ie"]
password = os.getenv("EP")

# List of files to attach
files = [
    r"C:\Users\Thetj\OneDrive\Documents\del\dataprocagre.pdf",
    r"C:\Users\Thetj\OneDrive\Documents\del\teamopagre.pdf",
    r"C:\Users\Thetj\OneDrive\Documents\del\shareagre.pdf"
]

print("Loading...")

def send_email(subject, html_body, sender, recipients, password, files):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    
    # Attach HTML body
    msg.attach(MIMEText(html_body, "html"))
    
    # Attach files
    '''
    for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(Path(file_path).name))
            msg.attach(part)
        except FileNotFoundError:
            print(f"Warning: File not found - {file_path}")
            continue
    '''
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
for i in range(len(recipients)):
    time.sleep(5)
    send_email(subject, html_body, sender, recipients[i], password, files)
print("Complete")