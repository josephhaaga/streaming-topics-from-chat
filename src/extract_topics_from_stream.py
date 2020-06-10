import irc # module containing IRC convenience methods (e.g. connect, listen, log to file etc.)
import nlp # module containing NLP convenience methods (e.g. extract_entities, analyze_sentiment etc.)


def main():
    irc = connect_to_IRC()
    irc.when_message_is_received([
        irc.extract_text_from_message,
        nlp.get_entities_by_type
    ])

if __name__ == '__main__':
    main()
