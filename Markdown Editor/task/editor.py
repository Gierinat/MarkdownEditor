END_OPTION = "!done"
HELP_OPTION = "!help"
SUPPORTED_COMMANDS = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                      'ordered-list', 'unordered-list', END_OPTION)
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


def list_formatter(formatter):
    rows = 0
    while rows < 1:
        rows = int(input("Number of rows: "))
        if rows < 1:
            print("The number of rows should be greater than zero")
    list_temp = ""
    for row in range(1, rows + 1):
        text = input(f"Row #{row}: ") + "\n"
        text = (lambda t, f: "* " + t if f == 'unordered-list' else f"{row}. " + t)(text, formatter)
        list_temp += text

    return list_temp


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
    if formatter == 'ordered-list':
        text += list_formatter(formatter)
    if formatter == 'unordered-list':
        text += list_formatter(formatter)
    return text


def file_saver(text):
    file = open("output.md", 'w')
    file.write(text)
    file.close()


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

    file_saver(user_text)


if __name__ == "__main__":
    main()
