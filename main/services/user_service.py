from main.repositories import UserRepository
from main.models import User


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create(self, user: User) -> User:
        user = self.repository.create(user)
        return user

    def find_by_username(self, username: str) -> User:
        return self.repository.find_by_username(username)

    def find_by_id(self, id):
        user = self.repository.find_by_id(id)
        return user

    def find_all(self):
        users = self.repository.find_all()
        return users

    def update(self, user: User) -> User:
        user = self.repository.update(user)
        return user
