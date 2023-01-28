
class Stream:
    """
        The base Component interface defines operations that can be altered by
        decorators.
    """
    def write(self, data):
        pass


class CloudStream(Stream):
    """
        Concrete Components provide default implementations of the operations. There
        might be several variations of these classes.
    """
    def write(self, data):
        print(f"Storing {data}")


class CompressedCloudStream(Stream):
    """Decorator"""
    def __init__(self, stream):
        self._stream = stream

    def write(self, data):
        compressed = self.compress(data)
        self._stream.write(compressed)

    def compress(self, data):
        return data[0:5]


class EncryptedCloudStream(Stream):
    """Another decorator"""

    def __init__(self, stream):
        self._stream = stream

    def write(self, data):
        encrypted = self.encrypt(data)
        self._stream.write(encrypted)

    def encrypt(self, data):
        return "#$%&***!@^#)(*((*&^!"


class ClientCode:
    """Fictitious client """
    def execute_code(self):
        """Decorating various types of stream to obtain crazy results!"""
        self.store_credit_card(EncryptedCloudStream(CompressedCloudStream(CloudStream())))

    def store_credit_card(self, stream):
        stream.write("1234-1234-1234-1234")


client = ClientCode()
client.execute_code()