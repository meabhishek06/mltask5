import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
# You can also input you password here since entering password while running lead to security issues
senderemail="abhiccv1998@gmail.com"
senderpass = "houseofdead"
receipientemail ="meabhishekarora06@gmail.com"
mail_content = "ipblocked"
file_location = '/root/mltask5/iptobeblocked.txt'
msg = MIMEMultipart()
msg['From'] = senderemail
msg['To'] = receipientemail
msg['Subject'] = 'IP Blocked!!!'
#msg.attach(MIMEText(iptobeblocked.txt, 'plain'))
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# Attach the attachment to the MIMEMultipart object
msg.attach(part)
#Using Gmail SMTP server 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderemail, senderpass)
text = msg.as_string()
server.sendmail(senderemail, receipientemail, text)
server.quit()
print('Your mail regarding Suspicious activity is Sent!!')



