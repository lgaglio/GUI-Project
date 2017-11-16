from abc import ABC, abstractmethod

""" TODO: Add methods and common things, however this is a base class so there is nothing to add here. DO NOT PUT ANY 
 CODE HERE! """


class GameObject(ABC):
    @abstractmethod
    def update(self):
        pass
