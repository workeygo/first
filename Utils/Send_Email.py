import smtplib
from Config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#    定义：发送邮件，发送最新测试报告html
class Send_Email():
    def send_email(self,newfile):
        # 打开文件
        with open(newfile,'rb') as f:
            # 读取文件内容
            mail_body = f.read()

        # 发送邮箱服务器
        smtpserver = Config.smtpserver
        # 发送邮箱用户名/密码
        user = Config.user
        password = Config.password
        # 发送邮箱
        sender = Config.sender
        # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
        receiver = Config.receiver
        # 发送邮件主题
        subject = Config.subject

        # 编写 HTML类型的邮件正文
        # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
        #    msg = MIMEText(mail_body,'html','utf-8')

        msg = MIMEMultipart('mixed')

        # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
        #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
        # 中文测试ok
        text = "Dear all!\n附件是最新的测试报告。\n请下载后使用GoogleChrome浏览器查看。\n请知悉，谢谢。"
        msg_plain = MIMEText(text,'plain', 'utf-8')
        msg.attach(msg_plain)

        # msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        # msg.attach(msg_html1)

        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)

        # 以附件的方式发送：但是会报554，倍163退信。--此路不通。
        #    msg_html = MIMEText(mail_body,'base64','utf-8')
        #    msg_html["Content-Type"] = 'application/octet-stream'
        #    msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
        #    msg.attach(msg_html)

        # 要加上msg['From']这句话，否则会报554的错误。
        # 要在163有限设置授权码（即客户端的密码），否则会报535
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = Header('发件人兴证国际 <280932267@qq.com>','utf-8')
        msg['To'] = ";".join(receiver)


        # 连接发送邮件
        smtp = smtplib.SMTP()
        try:
            smtp.connect(smtpserver, 25)
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            print("邮件已发送")
        except smtplib.SMTPException:
            print("邮件发送失败")
        finally:
            smtp.quit()
