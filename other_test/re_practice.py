# -*- coding:utf-8 -*-
import re
import pyperclip
import requests
from bs4 import BeautifulSoup

#可以将正则表达式放在多行，并用re.VERBOSE参数忽略空白符和注释
#匹配电话号码的正则表达式
phoneRegex = re.compile(
    r'''(
        (\d{3}|\(\d{3}\))?                  # area code
        (\s|-|\.)?                          # seperater
        (\d{3})                             # first 3 digits
        (\s|-|\.)                           # seperater
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))?     # extension
    )''',re.VERBOSE
)

#测试嵌套分组顺序
regexObj = re.compile(r'(\d{3}(\d{3})\d{2}(\d{3}))')
print(regexObj.search('33344455666').group())
print(regexObj.search('33344455666').group(1))
print(regexObj.search('33344455666').group(2))
print(regexObj.search('33344455666').group(3))
'''输出为：
33344455666
33344455666
444
666
输出结果说明分组嵌套时group（1）为最大的那个范围
'''

#为E-mail创建一个正则表达式
emailRegex = re.compile(
    r'''(
        [0-9a-zA-Z._%+-]+                   # username
        @                                   # @ symbol
        [0-9a-zA-Z.-]+                      # domain name
        (\.[a-zA-Z]{2,4})                     # dot-somthing
    )''',re.VERBOSE
)
print(emailRegex.search('wnz28@sina.com').group())

'''
url = "https://nostarch.com/contactus.htm"
text1 = str(requests.get(url))
print(text1)
'''

#find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += groups[8]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

#copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email address found.')

#测试findall()对有分组的正则表达式的索引取值
testRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
for groups in testRegex.findall('Cell: 333-222-7777 Work: 333-555-9999'):
    print(groups[1])

'''
得到是元组的列表，元组的每一项是每个分组的匹配，元组是每个模式的总匹配
'''
