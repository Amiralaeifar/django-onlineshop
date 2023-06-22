from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('Your api key')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'Your verification code is {code}'
        }
        response = api.sms_send(params)
        
    except APIException as e:
        print(e.decode('utf-8'))
        
    except HTTPException as e:
        print(e.decode('utf-8'))
    
    