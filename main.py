from noticeTestDay import open_chatroom, kakao_sendtext, calculate_dday
import datetime
import time
from noticeLunchMenu import findTodaysLunch
import schedule

chatroom_name = '23년 도제반'

def main() -> None:
    open_chatroom(chatroom_name) 
    dDay = calculate_dday()
    lunchMenu = '\n'.join(findTodaysLunch())
    message = f"""=============================
정보처리기능사 실기 시험이 {dDay}일 남았습니다.
-----------------------------------------------
오늘의 급식은 \n{lunchMenu} 입니다.
============================="""
    kakao_sendtext(chatroom_name, message)

schedule.every().day.at("07:00").do(main)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(1)