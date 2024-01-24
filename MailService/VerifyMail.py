from MailService.Base import Base
from email.message import EmailMessage
from email.mime.text import MIMEText
import logging

log = logging.Logger(__name__)

class VerifyMail(Base):
    def sendVerificationMail(self, email, code, service):
        log.info("Generating Email")
        msg = EmailMessage()

        msg["Subject"] = f"Verify your mail for {service}"
        msg["To"] = email
        msg["From"] = self.email
        html = f"""
                <html>
                    <body>
                        <h3> Your verification code for {service} is {code}</h3>    
                    </body>
                </html>
            """
        text = f"Your Login Code is {code}"
        msg.set_content(text)
        msg.add_alternative(html, subtype="html")
        str_msg = msg.as_string()
        resp = self.send_mail(email=email, msg=str_msg)
        return resp
