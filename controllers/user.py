from models.User import User


def create_user(user_in: User) -> dict:
    user = user_in.model_dump()

    return {
        'message': 'User created successfully',
        'user': user,
    }
