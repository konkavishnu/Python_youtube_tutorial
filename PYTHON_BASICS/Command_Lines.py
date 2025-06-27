# NOTE : Command line functions cannot be executed with run button just like normal python file .
# we need to go to the command line (Terminal) and type - py Command_Lines.py -n "Vishnu" -l "English"
# to get the configured output.


def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides personal greeting"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Your name"
    )
    parser.add_argument(
        "-l", "--lang", metavar="langauge",
        required=True, choices=["English", "Spanish", "German"],
        help="Your language"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
