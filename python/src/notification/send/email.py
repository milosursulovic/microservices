import smtplib
import os
import json
from email.message import EmailMessage


def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message['mp3_fid']
        receiver_address = message['username']

        smtp_host = os.environ.get(
            "MAILTRAP_SMTP_HOST", "sandbox.smtp.mailtrap.io")
        smtp_port = int(os.environ.get("MAILTRAP_SMTP_PORT", 587))
        smtp_user = os.environ.get("MAILTRAP_SMTP_USER")
        smtp_pass = os.environ.get("MAILTRAP_SMTP_PASS")

        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
        msg['Subject'] = 'Your mp3 file is ready!'
        msg['From'] = "no-reply@example.com"
        msg['To'] = receiver_address

        session = smtplib.SMTP(smtp_host, smtp_port)
        session.starttls()
        session.login(smtp_user, smtp_pass)
        session.send_message(msg)
        session.quit()

    except Exception as err:
        return err
