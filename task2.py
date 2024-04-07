#!/usr/bin/python3


import argparse
# # from typing import Tuple

# # -> Tuple[str, str, str]
def my_info():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    age = int(input("лет: "))
    # print(name)
    # print(last_name)
    # print(age)
    bio = (name, last_name, age)
    return bio

# my_info()

    # 1 variant.
    # data = (name, last_name, age)
    # return data

    # 2.
    # return name, last_name, age
# parser = argparse.ArgumentParser(description="describe what the script does", 
# formatter_class=argparse.RawDescriptionHelpFormatter)

def _parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        action="store",
        required=True,
        choices=["name", "full_name", "full_info"],
        help="Choose the mode what info to return"
    )
    return parser


def get_info(mode: str) -> str: 
    info = my_info()
    if mode == "name":
        return f"Your name: {info[0]}"
    elif mode == "full_name":
        return f"Your full name: {info[0]} {info[1]}"
    elif mode == "full_info":
        return f"Your bio: {info[0]} {info[1]}, age: {info[2]}"

if __name__ == "__main__":
    args = _parse().parse_args()
    mode = args.mode 
    print(get_info(mode))
    
        
