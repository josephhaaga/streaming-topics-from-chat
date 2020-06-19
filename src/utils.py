import socket
import re

from emoji import demojize


class IRC:
    def __init__(self, server, port, nickname, token):
        self.socket = socket.socket()
        self.socket.connect((server, port))
        self.socket.send(f"PASS {token}\r\n".encode("utf-8"))
        self.socket.send(f"NICK {nickname}\r\n".encode("utf-8"))

    def join_channel(self, channel):
        if not channel.startswith('#'):
            print("Channel must begin with #")
            sys.exit(1)
        self.socket.send(f"JOIN {channel}\r\n".encode("utf-8"))

    def listen_for_messages(self, handlers):
        sock = self.socket
        try:
            while True:
                resp = sock.recv(2048).decode("utf-8")
                if resp.startswith("PING"):
                    sock.send("PONG\n".encode("utf-8"))
                elif len(resp) > 0:
                    formatted_response = demojize(resp)
                    for message in formatted_response.split('\n'): # MAY BE MORE THAN ONE MESSAGE
                        for handler in handlers:
                            handler(message)
        except KeyboardInterrupt:
            sock.close()
            exit()


class TwitchChat(IRC):
    """
    Get token here: https://twitchapps.com/tmi/
    """

    server = 'irc.chat.twitch.tv'
    port = 6667
    pattern = re.compile(r':(.+)!(?:.+)@(?:.+)\.tmi\.twitch\.tv PRIVMSG (.+) \:(.+)')

    def __init__(self, nickname, token):
        super().__init__(self.server, self.port, nickname, token)

    @classmethod
    def parse_message(cls, message):
        if "PRIVMSG" not in message:
            return
        user, channel, text = cls.pattern.findall(message)[0]
        return {'user': user, 'channel': channel, 'text': text}
