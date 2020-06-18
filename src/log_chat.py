# Borrowed from LearnDataSci

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

def log_chat(channel, verbose=False):
    irc_server = TwitchChat(nickname, token)
    irc_server.join_channel(channel)
    irc_server.listen_for_messages([
        logging.info,
        print
    ])
    exit()

def main():
    print(f"Using args {sys.argv}")
    channel = sys.argv[1]
    if not channel.startswith('#'):
        print("Channel must begin with #")
        sys.exit(1)
    print(f"Logging chat from {channel}")
    log_chat(channel)

if __name__ == '__main__':
    main()
