import json


def remove_user(user_to_delete: str, bank_path: str = "bank.json", auth_path: str = "auth.json", clients_path: str = "clients.json"):


    # here I need to change to make it efficent
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    with open(bank_path, "r") as f:
        credentials = json.loads(f.read())

    with open(bank_path, "r") as f:
        clients = json.loads(f.read())

    accounts.pop(user_to_delete, None)
    credentials.pop(user_to_delete, None)
    clients.pop(user_to_delete, None)

    with open(bank_path, "w") as f:
        f.write(json.dumps(accounts, indent=4))

    with open(bank_path, "w") as f:
        f.write(json.dumps(credentials, indent=4))

    with open(bank_path, "w") as f:
        f.write(json.dumps(clients, indent=4))





def add_user():
    pass