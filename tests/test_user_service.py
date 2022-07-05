import unittest
from main import create_app, db
from main.models import User
from main.services.user_service import UserService
import pymysql
pymysql.install_as_MySQLdb()


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.userService = UserService()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_user(self):
        user_model = User(user_name='Yoan', email='yojuan2008@yahoo.com', key='NUEVE')
        self.userService.create(user_model)
        self.assertGreater(user_model.id, 0)
        user1 = self.userService.find_by_id(1)
        self.assertIsNotNone(user1)

    def test_create_user(self):
        user = self.__create_user()
        self.assertEqual(user.user_name, 'juan')
        self.assertGreater(user.id, 0)
        self.assertEqual(user.email, 'juan@gmail.com')
        self.assertEqual(user.key, 'NWRmMTv3ZWUdY2RjNjA3NWY4NjQ2NmQyOGRkYlolMmM=')

    def test_db_find_by_user(self):
        user = self.__create_user()
        user = self.userService.find_by_username(user.user_name)
        self.assertEqual(user.user_name, 'juan')
        self.assertGreater(user.id, 0)

    def __create_user(self):
        username = 'juan'
        email = 'juan@gmail.com'
        key_encrypt = 'NWRmMTv3ZWUdY2RjNjA3NWY4NjQ2NmQyOGRkYlolMmM='
        user = User(user_name=username, email=email, key=key_encrypt)
        return self.userService.create(user)
