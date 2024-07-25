import requests
from datetime import datetime, timezone, timedelta

LAST_MATCH_URL_BY_GAME_NAME = {
    "tft": "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/mSQzszCtIk_zI0U8TctYhZ_Mfb5559dB0iASct6V3EdSSJzas7uoadkC-FEXQLHFMv4_RXkoTyrDZw/ids?start=0&count=1",
    "lol": "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/mSQzszCtIk_zI0U8TctYhZ_Mfb5559dB0iASct6V3EdSSJzas7uoadkC-FEXQLHFMv4_RXkoTyrDZw/ids?start=0&count=1"
}

MATCH_TIME_URL_BY_GAME_NAME = {
    "tft": "https://asia.api.riotgames.com/tft/match/v1/matches/",
    "lol": "https://asia.api.riotgames.com/lol/match/v5/matches/",
}

TIMESTAMP_KEY_BY_GAME_NAME = {
    'tft': "game_datetime",
    'lol': "gameEndTimestamp"
}

def get_minsu_last_game(gameName):
    API_KEY = "RGAPI-aed09009-eb61-4105-99ab-21b0f75e0a19"
    headers = {
        "X-Riot-Token": API_KEY
    }
    url = LAST_MATCH_URL_BY_GAME_NAME[gameName]

    res = requests.get(url, headers=headers)
    last_match = res.text[2:-2]
    url = MATCH_TIME_URL_BY_GAME_NAME[gameName] + last_match
    res = requests.get(url, headers=headers)
    match_info = res.json()
    unix_timestamp = int(match_info['info'].get(TIMESTAMP_KEY_BY_GAME_NAME[gameName]))
    utc_datetime = datetime.utcfromtimestamp(unix_timestamp // 1000)

    kr_timezone = timezone(timedelta(hours=9))
  
    kr_datetime = utc_datetime.replace(tzinfo=timezone.utc).astimezone(kr_timezone)

    kr_time_str = kr_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return kr_time_str