from typing import List

def read_integers() -> List[int]:
    user_input= input()
    string_list = [int(x) for x in user_input.split(",")]
    return string_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
