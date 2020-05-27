#coding=utf-8
#!/usr/bin/python
import os
import time

def open_app(app_dir):
    os.startfile(app_dir)

if __name__ == "__main__":
    dir_list = ["F:\Program Files\Snipaste-2.3-Beta-x64\Snipaste.exe", "F:\Program Files (x86)\Tencent\WeChat\WeChat.exe", 
            "C:\Program Files (x86)\Sangfor\SSL\EasyConnect\EasyConnect.exe", "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    for dir in dir_list:
        print(dir)
        open_app(dir)
        time.sleep(5)
	  