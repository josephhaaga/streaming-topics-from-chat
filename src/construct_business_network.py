import sys
import logging
import re

from utils import TwitchChat

nickname = 'joehaaga'
token = '<YOUR_TOKEN>'

with open('.token', 'r') as f:
    token = f.read().replace('\n', '')

def follow_the_stream(channel, verbose=False):
    irc_server = TwitchChat(nickname, token)
    irc_server.join_channel(channel)
    irc_server.listen_for_messages([
        parse_economic_event
    ])
    exit()

def parse_economic_event(message):
    a = TwitchChat.parse_message(message)
    if not a:
        return
    user, channel, text = a
    if a['user'] != 'beginbotbot':
        return
    # logging.info(f"{text}") # We can just look at chat.log
    match_text_to_event_handler(a['text'].lower())

def insert_event_into_graph(origin, action, dest):
    print(f"{origin} - [{action}] -> {dest}")

def match_text_to_event_handler(text):
    print(f"parsing economic event: {text}")
    usernames = re.compile(r'@(\S+)')
    usernames = usernames.findall(text)
    if len(usernames) < 2:
        return
    origin, dest = usernames
    if 'stole from' in text:
        # "@bopojoe_ stole from @joehaaga. Chance of Getting Caught: 51.66666666666666%"
        insert_event_into_graph(origin, "ROBBED_SUCCESSFULLY", dest)
    elif 'was caught stealing' in text:
        insert_event_into_graph(origin, "ROBBED_FAILED", dest)
    elif 'shared' in text:
        # PRO-SOCIAL BEHAVIOR
        insert_event_into_graph(origin, "SHARED_WITH", dest)
    elif 'gave' in text:
        insert_event_into_graph(origin, "DONATED_TO", dest)

def main():
    print(f"Using args {sys.argv}")
    channel = sys.argv[1]
    print(f"Following economic news on {channel}")
    follow_the_stream(channel)

if __name__ == '__main__':
    main()
