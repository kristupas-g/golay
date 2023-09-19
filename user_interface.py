import sys

def p(string):
    print(string)
    print('\n')

arg = None
if len(sys.argv) > 1:
    arg = sys.argv[1]

if arg == None:
    options = [
        "No argument passed! Available options:",
        "  - Comma separated binary values if length < 12, zero padding will be added",
        "  - A string of text, must surrounded in """,
        "  - A path to an image (.jpg, .jpeg, .png)"
    ]
    p("\n".join(options))
    exit()

def identify_argument(argument):
    if all(char in "01," for char in argument):
        return "binary"

    if argument.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        return "image"

    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return "string"
    
    p("Unsupported argument")
    exit()
