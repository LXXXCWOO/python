import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# 메일 컨텐츠의 몸통역할
recipient = ['flex2w64@gmail.com', 'cwstyle01@naver.com']

message = MIMEMultipart()
message['Subject'] = '[Test] 메일 전송 테스트'  # 제목
message['From'] = "cwstyle01@naver.com"  # 수신자
message['To'] = ",".join(recipient)  # 발신자

# HTML 메일 컨텐트
content = """
    <html>
    <body>
        <h2>{title}</h2>
        <p>메일 전송 테스트입니다</p>
    </body>
    </html>
""".format(
    title='메일.. 받으셨나요..?'
)

mimetext = MIMEText(content, 'html')
message.attach(mimetext)

# SMTP를 사용해 메일을 보낸다.
email_id = 'cwstyle01'
email_pw = 'Dhdnjfmay5%%'

server = smtplib.SMTP('smtp.naver.com', 587)
server.ehlo()
server.starttls()
server.login(email_id, email_pw)
server.sendmail(message['From'], recipient, message.as_string())
server.quit()
