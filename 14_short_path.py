from requests import get
from pprint import PrettyPrinter
import urllib3

# Disable SSL warning when we bypass verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    try:
        data = get(BASE_URL + ALL_JSON, verify=False, timeout=10).json()
        links = data['links']
        return links
    except Exception as e:
        print(f"Error getting links: {e}")
        return {}

def get_scoreboard():
    try:
        links = get_links()
        if not links or 'currentScoreboard' not in links:
            print("Scoreboard link not found")
            return

        scoreboard = links['currentScoreboard']
        games = get(BASE_URL + scoreboard, verify=False, timeout=10).json()['games']

        if not games:
            print("No games today")
            return

        for game in games:
            home_team = game['hTeam']
            away_team = game['vTeam']
            clock = game['clock']
            period = game['period']

            print("------------------------------------------")
            print(f"{home_team['triCode']} vs {away_team['triCode']}")
            print(f"{home_team['score']} - {away_team['score']}")
            print(f"{clock} - {period['current']}")

    except Exception as e:
        print(f"Error getting scoreboard: {e}")

def get_stats():
    try:
        links = get_links()
        if not links or 'leagueTeamStatsLeaders' not in links:
            print("Stats link not found")
            return

        stats = links['leagueTeamStatsLeaders']
        response = get(BASE_URL + stats, verify=False, timeout=10).json()
        teams = response['league']['standard']['regularSeason']['teams']

        teams = list(filter(lambda x: x['name'] != "Team", teams))
        teams.sort(key=lambda x: int(x['ppg']['rank']))

        for i, team in enumerate(teams):
            name = team['name']
            nickname = team['nickname']
            ppg = team['ppg']['avg']
            print(f"{i + 1}. {name} - {nickname} - {ppg}")

    except Exception as e:
        print(f"Error getting stats: {e}")

# Run it
get_stats()
# get_scoreboard()  # uncomment if you want scoreboard