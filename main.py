from noticeTestDay import open_chatroom, kakao_sendtext, calculate_dday
import datetime
import time
from noticeLunchMenu import findTodaysLunch
import schedule, os
from noticeProblem import kakao_sendMedia
from getGameTime import get_minsu_last_game

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
정보처리산업기사 시험이 {dDay}일 남았습니다.
----------------------------------
{lunchMsg}
----------------------------------
민수의 마지막 게임시간입니다.

League of Legends: {get_minsu_last_game("lol")}
Eternal Return: 개발중
TeamFight Tactics: {get_minsu_last_game("tft")}
===========================
"""
    
    # f = open("t.txt", "r")
    # index = int(f.readline())
    # print(index)

    # fileDir = f"C:\\projects\\and\\네트워크\\NET_{index}.jpg"
    # kakao_sendMedia(fileDir, chatroom_name)
    kakao_sendtext(chatroom_name, message)
    # f = open("t.txt", "w")
    # f.write(str(index + 1))

    time.sleep(5)
    os.system("shutdown -s -t 1")

schedule.every().day.at("06:00").do(main)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(1)