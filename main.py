import os

LINE = (
    "It's 3am. You're not hungry, you're bored, "
    "and I'm not a vending machine. Go back to bed."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
