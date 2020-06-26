import requests
import random
HOST = "https://mygeoangelfirespace.city"
a = requests.get(f"{HOST}/db/users.json").json()

sorted(a['users'].values(), key=lambda k: k['street_cred'])

population = len(a['users'].values())

uninsured_users = [x for x in a['users'].values() if 'insured' not in x]
# the_one_percent = sorted(a['users'].values(), key = lambda k: k['cool_points'])[-1*(population//100):]
the_one_percent = sorted(uninsured_users, key = lambda k: k['cool_points'])[-1*(population//100):]


target = random.choice([person['name'] for person in the_one_percent])

# Get a sound effect from the target
b = requests.get(f"{HOST}/{target}.html").content.split(b'ul')[1].split(b'\n')
commands = [x.replace(b'        <a href="https://mygeoangelfirespace.city/commands/', b'').replace(b'.html">', b'') for x in b if b'commands' in x]

bounty = random.choice(commands).decode('utf8')

# find a poor active player
poor_players = sorted(a['users'].values(), key = lambda k: k['cool_points'])[:20]

# print steal and give commands
print(f"!steal @{target} {bounty}")
for player in poor_players:
    print(f"{player['name']}: {player['cool_points']} cool points")
