import re
from enum import Enum

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from config import TWILIO

client = TWILIO.enabled and Client(TWILIO.account_sid, TWILIO.auth_token)
verify_client = TWILIO.enabled and client.verify.services(TWILIO.verify_sid)


class PhoneVerificationStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    EXPIRED = "expired"


def validate_phone(phone: str):
    # + isn't optional for Twilio
    return bool(re.match(r"^\+[1-9]\d{1,14}$", phone))


def send_sms_code(to: str) -> bool:
    if TWILIO.enabled:
        try:
            verify_client.verifications.create(to=to, channel='sms')
            return True
        except TwilioRestException as e:
            if e.code in (60200, 60205):
                # number does not exist
                # 60205 stands for landline number that can't handle SMS
                return False
            raise e
    return True


def verify_sms_code(phone: str, sms: str):
    if not TWILIO.enabled:
        if sms == '000000':
            return PhoneVerificationStatus.APPROVED
        else:
            return PhoneVerificationStatus.REJECTED
    try:
        res = verify_client.verification_checks.create(to=phone, code=sms)
        return PhoneVerificationStatus(res.status)
    except TwilioRestException as e:
        # Twilio returns 404 after validation expires (10 minutes) or gets approved
        if e.code == 20404:
            return PhoneVerificationStatus.EXPIRED
        raise e
