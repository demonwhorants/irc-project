import random
import socket
import server_functions as sfn


class Server:

    SERVER_COMMANDS = {
        "build": sfn.build_room,
        "destroy": sfn.destroy_room,
        "kick": sfn.kick_user,
        "ban": sfn.banned_users
    }

    def __init__(self):
        admin_name = raw_input("Enter admin username: ")
        admin_password = raw_input("Enter admin password: ")
        admin_ID = random.randint(1, 100000)

        self.room_list = []         # room objects
        self.registered_users = []  # user:pw key  pairs
        self.logged_in_users = []   # user IDs
        self.guests = []            # guest IDs
        self.logged_in_users.append(admin_ID)
        self.registered_users.append(
            {
                "user_ID": admin_ID,
                "username": admin_name,
                "password": admin_password,
                "server_admin": "yes"
            }
        )


class Room:

    ROOM_COMMANDS = {}

    def __init__(self, room_name, creator):
        self.room_name = room_name
        self.user_list = [creator]
        self.admin_list = [creator]
        self.banned_users = []
        self.MOTD = "Have a nice Day!"

    def open_room(self):
        pass

    def close_room(self):
        pass


class User:
    def __init__(self, socket, username):
        self.user_ID = random.randint(1, 100000)
        self.user_name = username
        self.room_list = []
        self.socket = socket

    def join(self):
        pass

    def leave(self):
        pass

    def speak(self):
        pass

    def whisper(self):
        pass

    def create_room(self):
        pass


class Guest:
    def __init__(self, socket):
        self.guest_ID = random.randint(1, 100000)
        self.room_list = []
        self.socket = socket

    def register(self):

        pass

    def login(self):
        pass

    def join(self):
        pass

    def leave(self):
        pass

    def speak(self):
        pass

    def whisper(self):
        pass


# create server admin account


irc_server = Server()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 5001))
s.settimeout(10)
s.listen(5)

while True:

    try:

        print "talk"
        client, address = s.accept()
        print address
        client.setblocking(1)
        rxd = client.recv(1024)
        if rxd:
            print rxd
        client.close()

    except KeyboardInterrupt:

        exit()

    except:

        print "timeout"

print rxd
