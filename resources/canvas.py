import abc


class Canvas(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass
