END_OPTION = "!done"
HELP_OPTION = "!help"
SUPPORTED_COMMANDS = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line')
# 'ordered-list', 'unordered-list',
user_text = ""


def take_text(formatter):
    return input("Text: ")


def display_help():
    print("""Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done""")


def link_formatter():
    label = input("Label: ")
    url = input("URL: ")
    return "[" + label + "]" + "(" + url + ")"


def header_formatter():
    level = 0
    while level < 1 or level > 6:
        level = int(input("Level: "))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")

    text = input("Text: ")
    return "#" * level + " " + text + "\n"


def formatter_solver(formatter, text):
    if formatter == 'plain':
        text += take_text(formatter)
    if formatter == 'bold':
        text += "**" + take_text(formatter) + "**"
    if formatter == 'italic':
        text += "*" + take_text(formatter) + "*"
    if formatter == 'header':
        text += header_formatter()
    if formatter == 'link':
        text += link_formatter()
    if formatter == 'inline-code':
        text += "`" + take_text(formatter) + "`"
    if formatter == 'new-line':
        text += "\n"
    return text


def main():
    global user_text
    user_input = ""

    # main loop
    while user_input != END_OPTION:
        user_input = input("Choose a formatter: ")
        if user_input == HELP_OPTION:
            display_help()
        elif user_input in SUPPORTED_COMMANDS:
            user_text = formatter_solver(user_input, user_text)
            print(user_text)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
