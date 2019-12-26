import time
# now 生成测试报告时间
now = time.strftime('%Y-%m-%d_%H_%M_%S_')
# SendEmailTime 发送邮件时间
SendEmailTime = time.strftime('%Y-%m-%d %H:%M:%S')

# test_dir 测试用例路径      如果用/可以不用r
test_dir = r'C:\\Users\\user\\PycharmProjects\\Interface_Test_Project\\Test_cases'
# 测试报告的路径
test_report_dir = r'C:\\Users\\user\\PycharmProjects\\Interface_Test_Project\\Report'



# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户名/密码
user = '498413828@qq.com'
# password = 'hhhjymzyvbmsbijb'
password = 'sehynbylfdndbicf'
# 发送邮箱
sender = '498413828@qq.com'
# 多个接收邮箱，单个收件人的话，直接是receiver='xxx@xxx.com'
receiver = ['wanbaolin@testbird.com', '24273714@qq.com']
# 发送邮件主题
subject = '自动定时发送测试报告'+SendEmailTime
# 发件人地址
fromsender = '发件人兴证国际 <498413828@qq.com>'
# 编码格式
code ='utf-8'
