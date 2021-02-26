from argparse import ArgumentParser
import requests
from uuid import uuid4

HTTP = "http://"


def mine(url):
    try:
        print("Mining...")
        url = HTTP + url + "/mine"
        r = requests.get(url)
        if r.status_code == 200:
            print(r.status_code)
            print(r.content.decode())
        else:
            print(r.status_code)
            print("Unable to process request")
    except IOError as f:
        print(f)


def new_transaction(url, recipient, amount=int):
    try:
        print("Attempting new transaction...")
        url = HTTP + url + "/transactions/new"
        node_identifier = str(uuid4()).replace('-', '')
        json_data = {
            "sender": node_identifier,
            "recipient": recipient,
            "amount": amount
        }
        r = requests.post(url, json=json_data)
        if r.status_code == 201:
            print(r.status_code)
            print(r.content.decode())
        else:
            print(r.status_code)
            print("Unable to process request")
            print(r.content.decode())
    except IOError as f:
        print(f)


def run_client(url):
    print("------ Blockchain Menu ------")
    print("1 > Mine")
    print("2 > New Transaction")
    print("exit > Exit")
    choice = input("Enter Command > ")
    while choice != "exit":
        if choice == "":
            print("Command cannot be empty!")
        elif int(choice) == 1:
            mine(url)
        elif int(choice) == 2:
            recipient = input("Enter Recipient Address > ")
            amount = int(input("Enter amount > "))
            new_transaction(url, recipient, amount)
        else:
            print("Command not recognized!")
        choice = input("Enter Command > ")


def set_argparse():
    parser = ArgumentParser()
    parser.add_argument('-s', '--server', default="localhost")
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')
    return parser.parse_args()


if __name__ == '__main__':
    args = set_argparse()
    server = args.server
    port = str(args.port)
    url = server + ":" + port
    run_client(url)
