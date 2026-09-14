class UserRepository:

    def get_user(self, user_id):
        users = {
            1: {
                "id": 1,
                "name": "Ahmed",
                "email": "ahmed@example.com",
                "is_active": False,
            },
            2: {
                "id": 2,
                "name": "Omar",
                "email": "omar@example.com",
                "is_active": True,
            },
        }

        return users.get(user_id)
