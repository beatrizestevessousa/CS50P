import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"((?:\W|^)um(?:\W|$))"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
