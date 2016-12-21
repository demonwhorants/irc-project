import random
import socket


def build_room(irc_server, creator, room_name):

    print creator + " made a shiny room called " + room_name
    new_room = Room(creator, room_name)
    irc_server.room_list.append(new_room)


def destroy_room(irc_server, destroy_this_room):

    irc_server.room_list = [room for room in irc_server.room_list if room.room_name != destroy_this_room]
    print destroy_this_room + " destroyed."


def kick_user(irc_server, user_name):

    pass


def ban_user(irc_server, user_name):

    pass


def list_rooms(room_list):
    for room in room_list:
        print room.room_name


class Server:

    SERVER_COMMANDS = {
        "build": build_room,
        "destroy": destroy_room,
        "kick": kick_user,
        "ban": ban_user,
        "list_rooms": list_rooms
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

        def list_empty_rooms(self):
            pass


class Room:

    ROOM_COMMANDS = {}

    def __init__(self, creator, room_name):
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
        self.username = "Guest" + str(self.guest_ID)
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

        print "listening"
        client, address = s.accept()
        print address
        client.setblocking(1)
        rxd = client.recv(1024)
        if rxd:
            try:
                print rxd
                command, creator, thing = rxd.split(" ")
                irc_server.SERVER_COMMANDS[command](irc_server, creator, thing)
            except KeyError:
                print "invalid command"
        #client.close()

    except KeyboardInterrupt:

        exit()

    except:

        print "timeout"

print rxd
