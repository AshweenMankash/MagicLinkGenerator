from flask import Flask, request
from DatabaseOperations.VerifyMailOperations import VerifyMailOperations
from MailService.VerifyMail import VerifyMail
from random import randint
from time import sleep
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



@app.route("/sendMagic", methods = ["POST"])
def sendMagic():
    payload = request.json
    to_email:str = payload.get("email")
    ip_addr:str = request.remote_addr
    secret: str = payload.get("access_key")

    if not (to_email.__contains__("@") and to_email.__contains__(".")):
        return {
            "error": True,
            "msg": "Invalid Email Address"
        }

    try:
        code = randint(10000,99999)
        sleep(1)
        vOperations  = VerifyMailOperations()
        vOperations.store_mail_data_for_verification(email=to_email, ip_addr=ip_addr, code=code)
        
        vMail = VerifyMail(secret=secret)
        resp = vMail.sendVerificationMail(to_email, code, service=os.getenv("SERVICE_NAME"))
        if resp and resp.get("error"):
            return {
                "msg": resp.get("msg")
            }
        return {
            "msg": "Code Sent"
        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            "error": True,
            "msg": "Something went wrong"
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=int(os.getenv("PORT")))




