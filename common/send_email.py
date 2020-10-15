# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/2

E-mail:keen2020@outlook.com

=================================


"""

import smtplib
from email.mime.text import MIMEText  # 构造邮件文本内容
from email.header import Header  # 构造邮件标题
from email.mime.application import MIMEApplication  # 发送带附件的邮件
from email.mime.multipart import MIMEMultipart  # 发送带附件的邮件
# import win32com.client as win32


class SendEmail(object):

    @staticmethod
    def send_qq_file_mail(title, message, file_path, file_name):

        # 创建一个SMTP对象并连接smtp服务
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)

        # 登录SMTP服务器
        msg_from = '3023087535@qq.com'
        passwd = 'riinowwxativdfgb'

        # msg_to = ['415250069@qq.com', '87313199@qq.com', 'keen2020@outlook.com', "zuowei6971@dingtalk.com",
        #           "zhangyuzong@hczypay.com", "baocl@hczypay.com", "tonglei@hczypay.com", "1425491509@qq.com"]
        msg_to = ['415250069@qq.com', '87313199@qq.com', 'keen2020@outlook.com', "zuowei6971@dingtalk.com"]

        s.login(user=msg_from, password=passwd)

        # 构建邮件内容
        # message = "这是W1935的自动化测试报告，请注意查收！"
        # 创建一个邮件，文本类型
        content = MIMEText(message, _charset='utf8')

        # 构造附件
        # part = MIMEApplication(open(file_path, 'rb').read(), _subtype=False)
        part = MIMEApplication(open(file_path, 'rb').read())
        # 自定义文件名称
        part.add_header('content-disposition', 'attachment', filename=file_name)

        # 封装邮件添加邮件主题
        msg = MIMEMultipart()
        # 添加文本内容和附件
        msg.attach(content)
        msg.attach(part)
        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = msg_from  # 可以修改成任意名称
        msg['To'] = ','.join(msg_to)

        # 发送邮件
        try:
            s.sendmail(from_addr=msg_from, to_addrs=msg["To"].split(','), msg=msg.as_string())
            print("Send qq_email successfully")
        except Exception as e:
            print("Send qq_mail failed")
            raise e
        finally:
            s.quit()


if __name__ == '__main__':

    import os
    from common.constant import DATA_DIR

    mail_title = "这是测试邮件"
    mail_message = "这是测试邮件"

    SendEmail.send_qq_file_mail(
        title=mail_title,
        message=mail_message,
        file_path=os.path.join(DATA_DIR, 'api_automation_course.xlsx'),
        file_name='api_automation_course.xlsx')


