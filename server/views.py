from phonenumber_field.formfields import PhoneNumberField
from models.otp_user import Phone_Token

# Create your views here.
class GenerateOTP:
    def __init__(self, phone_number: PhoneNumberField, language: Phone_Token.Language) -> None:
        self.phone_number = phone_number
        self.language = language

    def post(self):
        otp = Phone_Token.generate_otp(4)
        phone_token = Phone_Token(phone_number=self.phone_number,
                                  otp=otp,language=self.language)
        phone_token.save()
        
        #it is not going to return if sms sends to phone_number not by telegram
        return otp 

class ValidateOTP:

    def __init__(self, user_id, otp) -> None:
        self.user_id = user_id
        self.otp = otp

    def validate(self):
        try:
            user = Phone_Token.objects.filter(user_id=self.user_id,
                                            otp=self.otp)
            return user
        except:
            return None


class LanguageHandler:
    def __init__(self, language) -> None:
        self.language = language
        # something_wrong ={
        #     ""
        # }.get(language)

    def greeting(self):
        return {
            "UZ": "Assalomu Alleykum",
            "EN": "HELLO"
        }.get(self.language)
    
    def enter_otp(self):
        return {
            "UZ": "OTP kiriting",
            "EN": "Enter OTP"
        }.get(self.language)
    
    def otp_correct(self):
        return {
            "UZ": "Qabul qilindi",
            "EN": "Excepted"
        }.get(self.language)
    
    def otp_wrong(self):
        return {
            "UZ": "OTP notog'ri",
            "EN": "OTP is wrong"
        }.get(self.language)
    