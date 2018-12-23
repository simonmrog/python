import sys

clients = "Pablo,Ricardo,"


def add_client (client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name + ","
    else:
        print ("Client is already in the client\'s list")


def update_client (client_name, up_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, up_client_name)
    else:
        print ("Client is not in the clients list")


def delete_client (client_name):
    global clients

    if client_name in clients:
        clients = clients.replace (client_name + ",", "")

    else:
        print ("Client is not in the clients list")
    

def search_client (client_name):
    global clients    
    clients_list = clients.split(",")
    
    for client in clients_list:
        if client == client_name:
            return True;
    
    return False


def list_clients ():
    global clients
    print (clients)


def _print_welcome():
    print ("WELCOME")
    print ("*" * 40)
    print ("What would you like to do today?")
    print ("[C]reate client")
    print ("[U]pdate client")    
    print ("[D]elete client")
    print ("[S]earch client")


def _get_client_name():
    client_name = None
    
    while not client_name:
        client_name = input("What\'s the client name?")
    
        if client_name == "exit":
            client_name = None
            break
    
    if not client_name:        
        sys.exit()

    return client_name


if (__name__ == "__main__"):
    _print_welcome()
    
    command = input()
    command = command.upper()

    if command == "C":
        client_name = _get_client_name()  
        add_client (client_name)

    elif command == "D":
        client_name = _get_client_name()
        delete_client (client_name)
    
    elif command == "U":
        client_name = _get_client_name()
        update = input("What is the updated client name?")
        update_client(client_name, update)
    
    elif command == "S":
        client_name = _get_client_name()
        found = search_client (client_name)

        if found:
            print ("Client is in the clients list")
        else:
            print ("Client {} not found".format(client_name))        

    else:
        print ("Invalid command.")
    
    list_clients()

