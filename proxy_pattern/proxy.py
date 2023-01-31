from abc import ABC, abstractmethod


class Ebook(ABC):
    """
        The Subject(Ebook) interface declares common operations for both RealSubject and
        the Proxy. As long as the client works with RealSubject using this
        interface, you'll be able to pass it a proxy instead of a real subject.
    """
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass


class RealEbook(Ebook):
    """
        The RealSubject(RealEbook) contains some core business logic. Usually, RealSubjects are
        capable of doing some useful work which may also be very slow or sensitive -
        e.g. correcting input data. A Proxy can solve these issues without any
        changes to the RealSubject's code.
    """
    def __init__(self, filename):
        self._filename = filename
        self.load()

    def load(self):
        print(f"Loading the ebook {self._filename}")

    def show(self):
        print(f"Showing the ebook {self._filename}")

    def get_filename(self):
        return self._filename


class EbookProxy(Ebook):
    """
        The Proxies have an interface identical to the RealSubject.
    """

    def __init__(self, filename):
        self._filename = filename
        self._real_ebook = None

    def show(self):
        if self._real_ebook is None:
            self._real_ebook = RealEbook(self._filename)
        self._real_ebook.show()

    def get_filename(self):
        return self._filename


class LoggingEbookProxy(Ebook):
    def __init__(self, filename):
        self._filename = filename
        self._real_ebook = None

    def show(self):
        if self._real_ebook is None:
            self._real_ebook = RealEbook(self._filename)

        print("Logging...")
        self._real_ebook.show()

    def get_filename(self):
        return self._filename


class Library:
    _ebooks = {}

    def add(self, ebook):
        self._ebooks[ebook.get_filename()] = ebook

    def open_ebook(self, filename):
        self._ebooks.get(filename).show()


def book_store():
    library = Library()
    filenames = ["a", "b", "c"]
    for filename in filenames:
        library.add(LoggingEbookProxy(filename))

    library.open_ebook("a")
    library.open_ebook("c")


book_store()
