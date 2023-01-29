

class Message:
    """Subsystem working with the facade class"""
    def __init__(self, message):
        self._message = message


class NotificationServer:
    """Subsystem working with the facade class"""

    def connect(self, ip_address):
        return Connection()

    def authenticate(self, app_id, key):
        return AuthToken()

    def send(self, auth_token, message, target_device):
        print("Sending a message")


class Connection:
    """Subsystem working with the facade class"""
    def disconnect(self):
        print("Disconnected")


class AuthToken:
    """Subsystem working with the facade class"""
    pass


class NotificationService:  # The Facade class!
    """
        The Facade class provides a simple interface to the complex logic of one or
        several subsystems. The Facade delegates the client requests to the
        appropriate objects within the subsystem. The Facade is also responsible for
        managing their lifecycle. All of this shields the client from the undesired
        complexity of the subsystem.
    """
    def send(self, message, target):
        server = NotificationServer()
        connection = server.connect("ip")
        auth_token = server.authenticate("appID", "key")
        server.send(auth_token, Message(message), target)
        connection.disconnect()


def client():
    service = NotificationService()
    service.send("Hello World!", "target")


client()
