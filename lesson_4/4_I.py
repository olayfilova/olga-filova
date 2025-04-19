# INTERFACE SEGREGATION

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass


class GeneralWorker:
    def work(self):
        ...

    def rest(self):
        ...


class Robot(GeneralWorker):
    def work(self):
        ...

    def rest(self):
        raise NotImplementedError("Robot do not rest")


class WorkMixin:
    def work(self):
        return "work"


class RestableMixin:
    def rest(self):
        return "Need a rest"


class HumanWorker(WorkMixin, RestableMixin): #or from GeneralWorker
    def work(self):
        return "Work"

    def rest(self):
        return "Need a rest"


class RobotWorker(WorkMixin):
    ...

h=HumanWorker()
