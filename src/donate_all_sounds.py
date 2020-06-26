import requests
import random
HOST = "https://mygeoangelfirespace.city"

a = requests.get(f"{HOST}/db/users.json").json()

sorted(a['users'].values(), key=lambda k: k['street_cred'])

population = len(a['users'].values())

uninsured_users = [x for x in a['users'].values() if 'insured' not in x]
poor_people = sorted(uninsured_users, key = lambda k: k['cool_points'])[:20]

poor_players = [x['name'] for x in poor_people]

target = 'joehaaga'

# Get a sound effect from the target
b = requests.get(f"{HOST}/{target}.html").content.split(b'ul')[1].split(b'\n')
commands = [x.replace(b'        <a href="https://mygeoangelfirespace.city/commands/', b'').replace(b'.html">', b'').decode('utf8') for x in b if b'commands' in x]

# print steal and give commands
for command in commands:
    player = random.choice(poor_players)
    print(f"!give @{player} {command}")
    commands.remove(command)
