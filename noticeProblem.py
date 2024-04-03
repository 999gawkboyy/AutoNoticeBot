import win32con, win32api, win32gui, time
from noticeTestDay import SendReturn

def callback(h, p):
    if win32gui.GetClassName(h) == "EVA_Window_Dblclk":
        p.append(h)
    return True

def kakao_sendMedia(fileDir, chatroom_name):
    chatHwnd = win32gui.FindWindow(None, chatroom_name)
    win32gui.SetForegroundWindow(chatHwnd)
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(0x54, 0, 0, 0) 
    win32api.keybd_event(0x54, 0, win32con.KEYEVENTF_KEYUP, 0)  
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    openFileHwnd = win32gui.FindWindow(None, "열기")
    comboBoxEx = win32gui.FindWindowEx(openFileHwnd, None, "ComboBoxEx32", None)
    comboBox = win32gui.FindWindowEx(comboBoxEx, None, "ComboBox", None)
    edit = win32gui.FindWindowEx(comboBox, None, "Edit", None)
    win32api.SendMessage(edit, win32con.WM_SETTEXT, None, fileDir )
    SendReturn(edit)
    time.sleep(1)
    l = []
    win32gui.EnumWindows(callback, l)
    SendReturn(l[0])