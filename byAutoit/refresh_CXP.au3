; click icon at bottom
MouseClick("left",281,745,1)
Sleep(1)
; click page tab
MouseClick("left",136,18,1)
WinWaitActive("Citrix XenApp - 已注销 - Google Chrome","")

; click someplace
MouseClick("left",359,223,1)
;Send("{F5}")


;MouseClick("left",682,439,1)
WinWaitActive("Citrix XenApp - 登录 - Google Chrome","")

;MouseClick("left",704,430,1)
Send("9{DOWN}{ENTER}{TAB}{TAB}{ENTER}")


WinWaitActive("Citrix XenApp - 应用程序 - Google Chrome","")
; click image button
;MouseClick("left",321,292,1)
MouseMove(330,300)
MouseDown("left")
MouseMove(329,300)
MouseClick("left",329,300,2)

