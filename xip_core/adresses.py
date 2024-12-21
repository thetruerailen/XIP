import random
import struct

class XIPAddress:
    def __init__(self, address_string: str = None):
        if address_string:
            self.zone, self.cluster, self.network, self.host = map(int, address_string.split('.'))
        else:
            self.zone = random.getrandbits(64)
            self.cluster = random.getrandbits(64)
            self.network = random.getrandbits(64)
            self.host = random.getrandbits(64)

    def __str__(self):
        return f"{self.zone}.{self.cluster}.{self.network}.{self.host}"

    def to_bytes(self) -> bytes:
        return struct.pack('!QQQQ', self.zone, self.cluster, self.network, self.host)

    @classmethod
    def from_bytes(cls, data: bytes) -> 'XIPAddress':
        addr = cls()
        addr.zone, addr.cluster, addr.network, addr.host = struct.unpack('!QQQQ', data)
        return addr
