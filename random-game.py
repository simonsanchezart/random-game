import argparse
import random
import argparse
import requests
import webbrowser
from time import sleep

RAWG_TOKEN = "YOUR_TOKEN_HERE"
STEAM_TOKEN = "YOUR_TOKEN_HERE"

parser = argparse.ArgumentParser(description="Random game chooser")
parser.add_argument("-steamuser", metavar="steamuser",
                    default="fackingtroll", type=str, help="Enter your Steam username")
parser.add_argument("-amount", metavar="amount", default=10,
                    type=int, help="Enter amount of games to choose")
parser.add_argument("-open", metavar="open", default="y",
                    type=str, help="Enter 'y' if you want to open links")
args = parser.parse_args()

def get_steam_id():
    steam_api_get_id = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAM_TOKEN}&vanityurl={steam_username}"
    request = requests.get(steam_api_get_id)
    id = request.json()['response']['steamid']
    return id


all_steam_games = {}


def get_steam_game_list():
    steam_api_call = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_TOKEN}&steamid={steam_id}&include_appinfo=true&format=json"
    request = requests.get(steam_api_call)
    full_json = request.json()
    all_games = full_json["response"]["games"]
    for game in all_games:
        game_id = game["appid"]
        all_steam_games[game["name"]
                        ] = f"https://store.steampowered.com/app/{game_id}/"


steam_username = args.steamuser
steam_id = get_steam_id()
steam_games = get_steam_game_list()

links_to_open = []


def open_all_links():
    for link in links_to_open:
        webbrowser.open_new_tab(link)
        sleep(0.05)


def main():
    platforms = ["steam", "itch.io", "other"]
    games_amount = args.amount
    for _ in range(games_amount):
        platform = random.choice(platforms)

        if platform == "steam":
            random_game = random.choice(list(all_steam_games))
            game_url = all_steam_games[random_game]
            links_to_open.append(game_url)
            print(f"{random_game} (Steam)\n")
        elif platform == "itch.io":
            print("Random itch.io game\n")
            links_to_open.append("https://itch.io/randomizer")
        elif platform == "other":
            page = random.randint(1, 851096)
            rawg_api_call = f"https://api.rawg.io/api/games?key={RAWG_TOKEN}&page={page}&page_size=1"
            request = requests.get(rawg_api_call)
            req_json = request.json()

            game = req_json["results"][0]["name"]
            links_to_open.append(f"https://www.google.com/search?q={game}")
            print(f"{game}\n")

    open_links = args.open
    if open_links == "y":
        open_all_links()


main()
