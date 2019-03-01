# -*- coding:utf-8 -*
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from util.read_init import ReadIni
import smtplib
import os


class SendEmail:
    def __init__(self):
        config_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path = config_dir + "//config//EmailConfig.ini"
        self.read_ini = ReadIni(file_path)

    # ---发送邮件---
    def send_email(self, pass_list, fail_list):
        # 创建一个带附件的实例
        msg = MIMEMultipart()

        # 配置SMTP服务器
        smtp_server = self.read_ini.get_value("smtp_server", "Email")
        username = self.read_ini.get_value("username", "Email")
        password = self.read_ini.get_value("password", "Email")

        # 发件人和收件人
        sender = self.read_ini.get_value("sender", "Email")
        to_list = self.read_ini.get_value("to_list", "Email")
        to_list = to_list.split(',')

        # 定义邮件头
        msg['From'] = sender
        msg['To'] = ";".join(to_list)
        msg["Subject"] = u"up360接口自动化测试报告"

        # 定义邮件正文
        pass_num = int(len(pass_list))
        fail_num = int(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (
                    count_num, pass_num, fail_num, pass_result, fail_result)

        content = MIMEText(content, _subtype='html', _charset='utf-8')
        msg.attach(content)

        # 发送邮件
        try:
            server = smtplib.SMTP()
            server.connect(smtp_server)
            server.login(username, password)
            server.sendmail(sender, to_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(e)
            return False
