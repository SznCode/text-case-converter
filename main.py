import sys

def convert_text(text, case_type):
    if case_type == "upper":
        return text.upper()
    elif case_type == "lower":
        return text.lower()
    elif case_type == "title":
        return text.title()
    else:
        return text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <text> <case_type>")
        sys.exit(1)

    text = sys.argv[1]
    case_type = sys.argv[2]
    print(convert_text(text, case_type))
