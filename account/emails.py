from django.core.mail import send_mail
import random
from django.conf import settings
from .models import CustomUser

import string




def send_otp_email(email):
    subject = 'Your account verification email is'
    otp  = random.randint(1000, 9999)
    from_email = settings.EMAIL_HOST
    message = f'This is Your  OTP {otp}'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()


# def send_otp_email(email):
#     subject = 'Your account verification email is'
#     otp  = random.randint(1000, 9999)
#     from_email = settings.EMAIL_HOST
#     message = f'This is Your  OTP {otp}'
#
#
#     send_mail(subject, message, from_email, [email])
#     user_obj = CustomUser.objects.get(email=email)
#     user_obj.otp = otp
#     user_obj.save()



