import smtplib
from email.mime.text import MIMEText
from email.header import Header

# smtpserver = 'imap.139.com'
# user='13515260240@139.com'
# password='Q973906567QPP,'
# sender='13515260240@139.com'
# receivers='973906567@qq.com'
# subject='hhhh'
# msg=MIMEText('<html><h1>love you</h1></html>','html','utf-8')
# msg['Subject']=Header(subject,'utf-8')



# smtp=smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()

# sender='13515260240@139.com'
sender='973906567@qq.com'
receivers=['1009502337@qq.com']
# receivers=['1277987140@qq.com']
pwd='uwcuaisrypurbddc'

message=MIMEText('love')
message['From']=Header('邮件测试','utf-8')
message['To']=Header('邮件测试','utf-8')

subject='python邮件测试'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.login(sender,pwd)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('发送成功')

except smtplib.SMTPException as e:
    print('无法发送')