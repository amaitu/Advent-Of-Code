import json


def import_json(path: str):
    with open(path) as file:
        return json.load(file)


def get_no_of_valid_passwords():
    password_sets = import_json("input.json")
    return sum(
        [
            1
            for password_set in password_sets
            if password_valid(next(iter(password_set)), list(password_set.values())[0])
        ]
    )


def password_valid(policy: str, password: str):
    target_letter = policy.split(" ")[1]
    available_indexes = [int(x) - 1 for x in policy.split(" ")[0].split("-")]

    occurances = 0
    for index in available_indexes:
        if password[index] == target_letter:
            occurances += 1

    return True if occurances == 1 else False


print(get_no_of_valid_passwords())
