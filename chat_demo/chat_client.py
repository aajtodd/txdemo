"""
chat client example
"""

from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.threads import deferToThread
from twisted.internet import reactor

def read_from_stdin(client):
    # would use readline or something more sophisticated (or tack on a user interface)
    on_input = deferToThread(raw_input, "")
    on_input.addCallback(client.sendChatMessage)
    return on_input

class ChatClientProtocol(Protocol):

    def dataReceived(self, data):
        print(data + "\n")
        read_from_stdin(self)

    def sendChatMessage(self, msg):
        """
        Hook for messages to come in from somewhere (e.g. stdin)
        """
        self.transport.write(msg)


if __name__ == '__main__':
    server = TCP4ClientEndpoint(reactor, '127.0.0.1', 9002)
    proto = ChatClientProtocol()
    connectProtocol(server, proto)
    reactor.run()


