from repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, user_id):
        user = self.repository.get_user(user_id)

        if user:
            return {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
            }

        return None

