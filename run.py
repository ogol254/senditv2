from models import User


class UserView(User):
    """docstring for UserView"""

    def __init__(self):
        self.user = User()

    def post(self, name, email):
        result = self.user.save(name, email)
        return result


ab = UserView()
result = ab.post('Abraham', 'abram@gmail.com')

print(resultsaMNxbZMxbZx)
