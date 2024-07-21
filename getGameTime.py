import requests
from datetime import datetime, timezone, timedelta

def get_minsu_last_LOL():
    API_KEY = "RGAPI-0bffafe4-7695-4335-a7ec-a599524cb20b"
    headers = {
        "X-Riot-Token": API_KEY
    }
    PUUID = 'mSQzszCtIk_zI0U8TctYhZ_Mfb5559dB0iASct6V3EdSSJzas7uoadkC-FEXQLHFMv4_RXkoTyrDZw'
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=1"

    res = requests.get(url, headers=headers)
    last_match = res.text[2:-2]

    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/KR_7166154286"
    res = requests.get(url, headers=headers)
    match_info = res.json()
    unix_timestamp = int(match_info['info'].get('gameEndTimestamp'))
    utc_datetime = datetime.utcfromtimestamp(unix_timestamp // 1000)

    kr_timezone = timezone(timedelta(hours=9))
  
    kr_datetime = utc_datetime.replace(tzinfo=timezone.utc).astimezone(kr_timezone)

    kr_time_str = kr_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return kr_time_str