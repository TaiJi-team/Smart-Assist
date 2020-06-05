; fffff
Run("C:\Program Files (x86)\Sangfor\SSL\EasyConnect\EasyConnect.exe")
Dim $d=WinWaitActive("[CLASS:#dlgWindow_1]", "", 10)

;or use ControlClick
MouseClick("left", 783, 393, 1)
;ControlSetText ($d,"","","18700836437")；
Send("18700836437")
Sleep(2)
MouseClick("left",868, 498,1)

;弹窗输入验证码的操作为生效
;Sleep(6)
;MouseClick("left",560, 406,1)
;Send("333333")
;Sleep(3)
;MouseClick("left",688, 475,1)
