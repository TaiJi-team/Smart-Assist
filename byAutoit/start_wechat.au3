; fffff
Run("F:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
WinWaitActive("[CLASS:#WeChatLoginWndForPC]", "", 5)
;or use ControlClick
Sleep(2)
MouseClick("left",686,442,2)