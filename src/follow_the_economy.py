import sys
import logging

from utils import TwitchChat


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('event.log', encoding='utf-8')])

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

def print_and_log(event, text):
    logging.info(f"A user {event}: {text}")
    print(f"A user {event}: {text}")


def match_text_to_event_handler(text):
    print(f"parsing economic event: {text}")
    if 'thank you' in text:
        if 'proposal' in text:
            # A user proposed something, representing activism
            print_and_log("proposed something", text)
        elif 'vote' in text:
            # A user voted, representing activism
            print_and_log("voted on something", text)
        elif 'request' in text:
            # An early adopter attempted to use a not yet approved soundeffect 
            print_and_log("requested something", text)
        elif 'feedback' in text:
            # A user submitted issue/bug/feature feedback, representing labor
            print_and_log("submitted feedback", text)
        elif 'bet' in text:
            print_and_log("bet at the casino", text)
    elif 'stole from' in text:
        print_and_log("stole", text)
    elif 'was caught stealing' in text:
        print_and_log("was caught stealing", text)
    elif 'shared' in text:
        # PRO-SOCIAL BEHAVIOR
        print_and_log("shared", text)
    elif 'bought' in text:
        # A user purchased a product; represents commerce/a transaction
        print_and_log("purchased something", text)
    elif 'gave' in text:
        print_and_log("donated something", text)
    elif 'custom css' in text:
        # A user submitted custom CSS, representing labor
        print_and_log("submitted custom css", text)
    elif 'NO BETS WHILE BEGINBOT IS SOLVING'.lower() in text:
        # A user attempted to cheat, representing anti-social behavior
        print_and_log("attempted to cheat at the casino", text)

def main():
    print(f"Using args {sys.argv}")
    channel = sys.argv[1]
    print(f"Following economic news on {channel}")
    follow_the_stream(channel)

if __name__ == '__main__':
    main()
