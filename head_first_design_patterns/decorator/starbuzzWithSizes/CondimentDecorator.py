from abc import abstractmethod

from Beverage import Beverage
from Size import Size


class CondimentDecorator(Beverage): #is-a
    beverage: Beverage
    
    @abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError
        
    def getSize(self) -> Size:
        return self.beverage.getSize()