from flask import Flask, request
from DatabaseOperations.VerifyMailOperations import VerifyMailOperations
from MailService.VerifyMail import VerifyMail
from random import randint
import traceback
import os
from dotenv import load_dotenv
import logging
load_dotenv()

app = Flask(__name__)

log = logging.Logger(__name__)

@app.route("/health")
def health():
    return {}


@app.route("/send-verification-mail", methods=["POST"])
def sendMagic():
    payload = request.json
    to_email: str = payload.get("email")
    ip_addr: str = request.remote_addr
    secret: str = payload.get("access_key")

    if not (to_email.__contains__("@") and to_email.__contains__(".")):
        return {"error": True, "msg": "Invalid Email Address"}

    try:
        code = randint(10000, 99999)
        vOperations = VerifyMailOperations()
        vOperations.store_mail_data_for_verification(
            email=to_email, ip_addr=ip_addr, code=code
        )

        vMail = VerifyMail(secret=secret)
        resp = vMail.sendVerificationMail(
            to_email, code, service=os.getenv("SERVICE_NAME")
        )
        if resp and resp.get("error"):
            return {"msg": resp.get("msg")}
        return {"msg": "Code Sent"}
    except Exception as e:
        log.error(traceback.format_exc())
        return {"error": True, "msg": "Something went wrong"}


@app.route("/verify-code", methods=["POST"])
def verifyCode():
    payload = request.json

    email = payload.get("email")
    code = payload.get("code")
    access_key = payload.get("access_key")

    if access_key != os.getenv("SECRET"):
        return {"msg": "Invalid Access Key", "verification_status": False}

    resp = VerifyMailOperations().verify_mail_data_for_verification(
        email=email, code=code
    )

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
