import sys

from utils import TwitchChat


nickname = 'joehaaga'
token = '<YOUR_TOKEN>'

with open('.token', 'r') as f:
    token = f.read().replace('\n', '')

def log_economic_events(message):
    """Match the message to a beginbot template, and parse the event"""


def monitor_the_economy(channel, verbose=False):
    irc_server = TwitchChat(nickname, token)
    irc_server.join_channel(channel)
    irc_server.listen_for_messages([
        log_economic_events
    ])
    exit()

def main():
    print(f"Using args {sys.argv}")
    channel = sys.argv[1]
    if not channel.startswith('#'):
        print("Channel must begin with #")
        sys.exit(1)
    print(f"Monitoring the economy on {channel}")
    log_chat(channel)

if __name__ == '__main__':
    main()
