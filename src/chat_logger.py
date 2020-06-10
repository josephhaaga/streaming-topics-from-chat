# Borrowed from LearnDataSci

import sys
import socket
import logging
from emoji import demojize


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'joehaaga'
token = '<YOUR_TOKEN>'

with open('.token', 'r') as f:
    token = f.read().replace('\n', '')

class IRC:
    def __init__(self, server, port, token, nickname):
        self.socket = socket.socket()
        self.socket.connect((server, port))
        self.socket.send(f"PASS {token}\r\n".encode('utf-8'))
        self.socket.send(f"NICK {nickname}\r\n".encode('utf-8'))

    def join_channel(self, channel):
        self.socket.send(f"JOIN {channel}\r\n".encode('utf-8'))

    def listen_for_messages(self, handler):
        handler(*args, **kwargs)
        try:
            while True:
                resp = sock.recv(2048).decode('utf-8')
                if resp.startswith('PING'):
                    sock.send("PONG\n".encode('utf-8'))
                elif len(resp) > 0:
                    formatted_response = demojize(resp)
                    logging.info(formatted_response)
                    handler(formatted_response)
        except KeyboardInterrupt:
            sock.close()
            exit()


def log_chat(channel, verbose=False):
    irc_server = IRC(server, port, token, nickname)
    irc_server.join_channel(channel)
    irc_server.listen_for_messages(print)
    exit()

if __name__ == '__main__':
    channel = sys.argv[1]
    if not channel.startswith('#'):
        print("Channel must begin with #")
        sys.exit(1)
    print(f"Logging chat from {channel}")
    log_chat(channel)
