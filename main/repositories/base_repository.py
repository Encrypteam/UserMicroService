from abc import ABC, abstractmethod
from main import db


class Create(ABC):
    @abstractmethod
    def create(self, model):
        pass


class Read(ABC):
    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self):
        pass


class Update(ABC):
    @abstractmethod
    def update(self, entity: db.Model):
        pass


class Delete(ABC):
    @abstractmethod
    def delete(self, entity: db.Model):
        pass



