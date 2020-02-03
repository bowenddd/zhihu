from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.header import  Header
import time
def getLatestMessage(browser):
    try:
        element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.ListShortcut')))
    except:
        print('ERROR')
    messages = browser.find_element_by_css_selector('.ListShortcut').find_elements_by_class_name('List-item')
    message = messages[0]
    t = message.find_element_by_class_name('ActivityItem-meta').find_elements_by_tag_name('span')[1].text
    option = message.find_element_by_class_name('ActivityItem-meta').find_elements_by_tag_name('span')[0].text
    title = message.find_element_by_class_name('ContentItem-title').text
    print(t)
    print(option+":"+title)
    content = option+":"+title
    return t,content

def sendMail(content):
    mail_host = 'smtp.xxx.com'
    mail_user = 'xxx@xxx.com'
    mail_pass = '*********'

    sender = 'xxx@xxx.com'
    receivers = ['xxx@xxx.com']
    message = MIMEText(content,'plain','utf-8')

    message['From'] = sender
    message['To'] = receivers[0]
    subject = '知乎动态更新！'
    message['Subject'] = Header(subject,'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print('邮件发送成功')
    except Exception as E:
        print(E)
if __name__ == '__main__':
    uid = 'xxx'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.zhihu.com/people/"+uid)
    while(True):
        t, content = getLatestMessage(browser)
        history = ''
        if content != history:
            sendMail(t+'    '+content)
            history = content
        time.sleep(4*60*60)
        browser.refresh()

