from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import mimetypes
import os
import smtplib
from email.mime.text import MIMEText

def file_add_mess(mess, filepath:str):
    filename = os.path.basename(filepath)                    

    if os.path.isfile(filepath):                              
            ctype, encoding = mimetypes.guess_type(filepath)        
    if ctype is None or encoding is not None:               
            ctype = 'application/octet-stream'                  
    maintype, subtype = ctype.split('/', 1)                
    if maintype == 'text':                                  
        with open(filepath) as fp:                          
                file = MIMEText(fp.read(), _subtype=subtype)    
                fp.close()                                      
    elif maintype == 'image':                              
            with open(filepath, 'rb') as fp:
                file = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
    else:                                                   
        with open(filepath, 'rb') as fp:
                file = MIMEBase(maintype, subtype)              
                file.set_payload(fp.read())                     
                fp.close()
        encoders.encode_base64(file)                      
            
        mess.attach(file)  




def send_letter(mess_text:str, list_user: list, filepath:str):
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    sender = 'falchevskiy-kostya@mail.ru'
    password = 'S8MnKtVevfjUNhygRwQU'

    mess = MIMEMultipart() 
    mess['From'] = sender
    body = mess_text                                        
    mess.attach(MIMEText(body, 'plain'))


        
    for i in list_user:
        if len(i) != 0:
            try:
                mess['To'] = i
                server.login(sender, password)
                file_add_mess(mess=mess, filepath=filepath)
                server.send_message(mess)
                print(f'Messages succesfully sent on emails')

            except Exception as _ex:
                print(f'{_ex} Check e-mail and password')
            
        else:
            continue   



def main():
    send_letter(input(), ['falchevskiy-kostya@mail.ru',], 'Ларин 433.pdf')

if __name__ == "__main__":
    main()

