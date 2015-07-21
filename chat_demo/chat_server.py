"""
chat server example
"""
from twisted.internet.protocol import ServerFactory, Protocol
from twisted.internet import reactor

class ChatServerProtocol(Protocol):
    DISCONNECTED = 0
    WAITING_FOR_USERNAME = 1
    CONNECTED = 2

    def __init__(self):
        self.state = self.DISCONNECTED
        self.username = None

    def connectionMade(self):
        print("Client connected from {0}".format(self.transport.getPeer()))
        self.transport.write("What is your name?\n")
        self.state = self.WAITING_FOR_USERNAME

    def connectionLost(self, reason):
        for client in self.factory.users:
            client.transport.write("{0} has left the chat.".format(self.username))

        self.factory.leave_chatroom(self)

    def dataReceived(self, data):
        if self.state == self.WAITING_FOR_USERNAME:
            self.username = data

            for client in self.factory.users:
                client.transport.write("{0} has joined the chatroom!".format(self.username))

            self.factory.join_chatroom(self)
            self.transport.write("Welcome {0}! You have joined the demo chatroom.".format(data))
            self.state = self.CONNECTED
        else:
            # write back out to everyone
            for client in self.factory.users.difference([self]):
                client.transport.write("{0}: {1}".format(self.username, data))

class ChatFactory(ServerFactory):
    protocol = ChatServerProtocol

    def __init__(self):
        self.users = set()

    def join_chatroom(self, client):
        self.users.add(client)

    def leave_chatroom(self, client):
        self.users.discard(client)


if __name__ == '__main__':
    reactor.listenTCP(9002, ChatFactory())
    reactor.run()


