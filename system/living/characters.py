from abc import ABC, abstractmethod, abstractproperty

class Characters(ABC):
    @abstractproperty
    def name(self):
        pass
    @abstractproperty
    def info(self):
        pass
    @abstractproperty
    def state(self):
        pass
    @abstractproperty
    def characteristics(self):
        pass
    @abstractproperty
    def abilities(self):
        pass
    @abstractproperty
    def skills(self):
        pass
    @abstractproperty
    def spells(self):
        pass
    @abstractproperty
    def inventory(self):
        pass
 