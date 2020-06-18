import sys
import logging

from utils import TwitchChat


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

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
    if a:
        print(f"{a['user']} said {a['text']}")


def main():
    print(f"Using args {sys.argv}")
    channel = sys.argv[1]
    print(f"Following economic news on {channel}")
    follow_the_stream(channel)

if __name__ == '__main__':
    main()
