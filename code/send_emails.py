import smtplib
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.text import MIMEText
import random

from_addr = 'admin<freezer712@qq.com>' #sender username and address
address = from_addr.split('<')[1].split('>')[0]##sender addr
password = 'xjnwigxjrssbcbbg'

def message(length:int):
    code = rand(length)
    mail_msg = '''<html>
        <body>
        <span>您的验证码是：</span>
        <span><b>{0}</b></span>
        </body>
        </html>
'''.format(code)
    return code, mail_msg


def rand(length:int):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(length):
        temp = random.randint(0, 61)
        result += alphabet[temp]
    return result


def send_mail(to_addr):
    code, content = message(10)
    msg = MIMEText(content, 'html', 'utf-8') ## 'plain' for txt and 'html' for html codes
    name, addr = parseaddr(from_addr)
    msg['From'] = formataddr((Header(name, 'utf-8').encode(), addr))
    name, addr = parseaddr(to_addr)
    msg["To"] = formataddr((Header(name, 'utf-8').encode(), addr)) # just for single user
    msg["Subject"] = Header('删库跑路确认操作', 'utf-8').encode()

    server = smtplib.SMTP_SSL('smtp.qq.com', 465) # 'smtp.qq.com' for qq Mail,and 'smtp.exmail.qq.com' for tencent enterprise email
    server.login(address, password)
    server.set_debuglevel(2)
    server.sendmail(address, to_addr, msg.as_string())
    #
    server.quit()
    print("Emails sent successfully.")
    return code


if __name__ == '__main__':
    send_mail("191250067@smail.nju.edu.cn")
