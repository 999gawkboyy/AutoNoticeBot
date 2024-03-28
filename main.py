from noticeTestDay import open_chatroom, kakao_sendtext, calculate_dday
import datetime
import time
from noticeLunchMenu import findTodaysLunch

chatroom_name = '23년 도제반'

if __name__ == '__main__':
    today = int(datetime.datetime.now().day)
    tomorrow = today + 1
    while 1:
        today = int(datetime.datetime.now().day)
        if (today == tomorrow):
            if (int(datetime.datetime.now().hour) == 7):       
                open_chatroom(chatroom_name) 
                dDay = calculate_dday()
                lunchMenu = '\n'.join(findTodaysLunch())
                message = f"""=============================
            정보처리기능사 실기 시험이 {dDay}일 남았습니다.
            -----------------------------------------------
            오늘의 급식은 \n{lunchMenu} 입니다.
            ============================="""
                kakao_sendtext(chatroom_name, message)
                tomorrow = today + 1
        print(today, tomorrow)
        time.sleep(60)
