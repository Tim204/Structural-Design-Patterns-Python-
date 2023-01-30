from abc import ABC, abstractmethod
# Imaginary Universal remote control concept using bridge pattern


# Part of the Feature hierarchy
class RemoteControl:
    """
        The Abstraction defines the interface for the "control" part of the two
        class hierarchies. It maintains a reference to an object of the
        Implementation hierarchy and delegates all the real work to this object.
    """

    def __init__(self, device):  # Reference to Device object
        self._device = device

    def turn_on(self):
        self._device.turn_on()

    def turn_off(self):
        self._device.turn_off()


class AdvancedRemoteControl(RemoteControl):

    def __init__(self, device):
        super().__init__(device)

    def set_channel(self, number):
        self._device.set_channel(number)


# Part of the implementation Hierarchy
class Device(ABC):
    """
        The Implementation defines the interface for all implementation classes. It
        doesn't have to match the Abstraction's interface. In fact, the two
        interfaces can be entirely different. Typically, the Implementation interface
        provides only primitive operations, while the Abstraction defines higher-level
        operations based on those primitives.
    """
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_channel(self, number):
        pass


class SonyTV(Device):
    """Concrete Implementation of the Device class"""

    def turn_on(self):
        print("Sony: turn on")

    def turn_off(self):
        print("Sony: turn off")

    def set_channel(self, number):
        print(f"Sony: set channel to {number}")


class SamsungTv(Device):
    """Concrete Implementation of the Device class"""
    def turn_on(self):
        print("Samsung: turn on")

    def turn_off(self):
        print("Samsung: turn off")

    def set_channel(self, number):
        print(f"Samsung: sett channel to {number}")


def remote_control():
    remote = AdvancedRemoteControl(SamsungTv())
    remote.turn_on()
    remote.set_channel(30)
    remote.turn_off()


remote_control()
