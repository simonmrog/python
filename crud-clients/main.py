import sys

NO_CLIENT_MESSAGE = "Client is not in the client list"
CLIENT_MESSAGE = "Client is in the client list"

clients = [
    {
        "code": 0,
        "name": "Pablo",
        "company": "Google",
        "email": "pablo@google.com",
        "position": "software engineer"
    },
    {
        "code": 1,
        "name": "Ricardo",
        "company": "Facebook",
        "email": "ricardo@facebook.com",
        "position": "data engineer"
    }
]


def create_client (client):
    global clients

    if not read_client(client["code"]):
        clients.append(client)
    else:
        print (CLIENT_MESSAGE)


def read_client (client_code):
    global clients

    flag = False
    for client in clients:
        if client["code"] == client_code:
            flag = True;
            break

    return (flag)


def update_client (client_code, updated_client):
    global clients

    if read_client(client_code):
        clients[client_code] = updated_client
    else:
        print (NO_CLIENT_MESSAGE)


def delete_client (client_code):
    global clients

    if read_client(client_code):
        clients.pop(client_code)
    else:
        print (NO_CLIENT_MESSAGE)


def list_clients ():
    global clients
    for client in clients:
        print ("{code} | {name} | {company} | {email} | {position}".format(
            code = client["code"], name = client["name"], company = client["company"],
            email = client["email"], position = client["position"]))


def search_client ():

    client_name = _get_client_field("name")
    client_code = _code_of (client_name)
    found = read_client (client_code)

    if found:
        print (CLIENT_MESSAGE)
    else:
        print (NO_CLIENT_MESSAGE)


def _code_of (client_name):
    global clients

    for client in clients:
        if client["name"] == client_name:
            return (client["code"])

    #We don't have negative client codes
    #This is in case the name is not in the list
    return (-1)

def _get_client_from_user ():

    client = {
        "code": int(_get_client_field("code")),
        "name": _get_client_field("name"),
        "company": _get_client_field("company"),
        "email": _get_client_field("email"),
        "position": _get_client_field("position")
    }

    return (client)


def _get_client_field(field):
    client_field = None

    while not client_field:
        client_field = input("What\'s the client {}?: ".format (field))

        if client_field == "exit":
            client_field = None
            break

    if not client_field:
        sys.exit()

    return (client_field)


def _print_welcome():
    print ("WELCOME")
    print ("*" * 40)
    print ("What would you like to do today?")
    print ("[C]reate client")
    print ("[S]earch client")
    print ("[U]pdate client")
    print ("[D]elete client")
    print ("[L]ist clients");


if (__name__ == "__main__"):
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "C":
        client = _get_client_from_user()
        create_client (client)
        list_clients();

    elif command == "S":
        search_client ()

    elif command == "U":
        updated_client = _get_client_from_user ()
        update_client(updated_client["code"], updated_client)
        list_clients();

    elif command == "D":
        client_code = int (_get_client_field("code"))
        delete_client (client_code)
        list_clients();

    elif command == "L":
        list_clients();

    else:
        print ("Invalid command.")
