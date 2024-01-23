from MailService.Base import Base
from email.message import EmailMessage
from email.mime.text import MIMEText

class VerifyMail(Base):

    def sendVerificationMail(self, email, code, service):
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
        text=f"Your Login Code is {code}"
        # p1 = MIMEText(text, "plain")
        # p2 = MIMEText(html, "html")
        # msg.attach(p1)
        # msg.attach(p2)
        msg.set_content(text)
        msg.add_alternative(html,subtype="html")
        str_msg = msg.as_string()
        print(str_msg)
        resp = self.send_mail(email=email, msg=str_msg)
        return resp

