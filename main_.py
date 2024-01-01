from google_gmail import Mymail


def main():
    
    myMail = Mymail()
    myMail.auth_google()
    myMail.get_message_service()
    myMail.get_message_id()
    myMail.get_message_payload()
    dic, images = myMail.get_message()
    
    print("image",images)
   
    
    
    
if __name__ == '__main__':
    main()
    