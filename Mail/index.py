import pandas as pd
import smtplib
import numpy as np
import os
import time
from ssl import create_default_context

data = pd.read_excel('./Book1.xlsx')
name = pd.DataFrame(data, columns=['Name'])
email = pd.DataFrame(data, columns=['Email'])

'''print each value in dataframe'''
for i in range(len(name)):
    print(name.iloc[i, 0])
    username = (name.iloc[i, 0])
    print(email.iloc[i, 0])
    sender = 'ravikishan63392@gmail.com'
    receivers = [email.iloc[i, 0]]

    message = """From: From %s  
To: To Person %s  
  
MIME-Version:1.0  
Content-type:text/html  
  
  
Subject: Sending SMTP e-mail   
  
<h3>Python SMTP</h3>  
<strong>This is a test e-mail message.</strong>  
<a herf="https://www.instagram.com/ravikishan.69/">Instagram</a>
"""%(sender,receivers)    
    try:
        smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        smtpObj.starttls(context=create_default_context())
        smtpObj.ehlo()
        smtpObj.login('ravikishan63392@gmail.com', '8538976959')
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        smtpObj.close()
        print("Successfully sent email")
    except  smtplib.SMTPAuthenticationError:
        print("Authentication Error")
    except smtplib.SMTPException as e:
        print("Error: unable to send email" + str(e))
