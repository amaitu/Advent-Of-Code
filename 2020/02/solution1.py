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
            == True
        ]
    )


def password_valid(policy: str, password: str):
    target_letter = policy.split(" ")[1]
    min_max = policy.split(" ")[0].split("-")

    if password.count(target_letter) < int(min_max[0]):
        return False

    if password.count(target_letter) > int(min_max[1]):
        return False

    return True


print(get_no_of_valid_passwords())
