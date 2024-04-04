from noticeTestDay import open_chatroom, kakao_sendtext, calculate_dday
import datetime
import time
from noticeLunchMenu import findTodaysLunch
import schedule, os
from noticeProblem import kakao_sendMedia

chatroom_name = '23년 도제반'

def main() -> None:
    open_chatroom(chatroom_name) 
    dDay = calculate_dday()
    lunchMenu = findTodaysLunch()
    if lunchMenu == -1: 
        pass
    else: 
        lunchMenu = '\n'.join(lunchMenu)

    lunchMsg = f"오늘의 급식은 \n{lunchMenu} 입니다" if lunchMenu != -1 else "오늘은 급식이 없네요"
    message = f"""===========================
정보처리기능사 실기 시험이 {dDay}일 남았습니다.
----------------------------------
{lunchMsg}
----------------------------------
오늘의 정보처리기능사 문제입니다
==========================="""
    fileDir = ""
    kakao_sendtext(chatroom_name, message)
    kakao_sendMedia(fileDir, chatroom_name)
    time.sleep(5)
    #os.system("shutdown -s -t 1")

schedule.every().day.at("07:00").do(main)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(1)