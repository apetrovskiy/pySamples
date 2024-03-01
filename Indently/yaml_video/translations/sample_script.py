import yaml


def show_lang():
    user_input = input("Enter a language: ")

    with open(f"{user_input}.yaml", "r") as file:
        config = yaml.safe_load(file)

    print(config["greetings"]["hello"])
    print(config["messages"]["welcome"])
    print(config["messages"]["error"])


show_lang()
show_lang()
