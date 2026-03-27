import unittest
import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.obj = user.User()

    def tearDown(self):
        pass

    def test_init(self):
        obj1 = user.User('Obj', 25)
        assert obj1.name == 'Obj'
        self.assertEquals(obj1.age, 25)

        obj2 = user.User('Obj')
        self.assertEquals(obj2.name, 'Obj')
        self.assertEquals(obj2.age, 10)

        self.assertEquals(self.obj.name, 'Bob')
        self.assertEquals(self.obj.age, 10)

    def test_set_hobbies(self):
        obj = user.User()
        obj.set_hobbies('skate, football')
        assert type(obj.hobbies) is list
        assert len(obj.hobbies) == 2
        assert obj.hobbies[0] == 'skate'