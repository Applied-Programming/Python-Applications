#! Python3.5

import smtplib
import sys

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()

# Insert your email address, password and address of the recipient between the quotes below:
your_own_email_id = "your-own-gmail-id@gmail.com"
your_own_email_password = "****yourpassword****"
email_id_of_the_recipient = "email-id-of-the-receiver@gmail.com"

# Log in to email account.
smtp_obj.login(your_own_email_id, your_own_email_password)

# Enter the body of the mail to be sent.
email_body = 'Hi there. This is an automated message sent specifically to you using a python script!'

print('Sending email...')
sendmail_status = smtp_obj.sendmail(your_own_email_id,email_id_of_the_recipient ,email_body)

# Print out the error message if the email wasn't properly sent.
if sendmail_status != {}:
    print('Oops! There was a problem sending email : %s' % (your_own_email_id, sendmail_status))
else:
    print ('Email successfully sent!')
smtp_obj.quit()
