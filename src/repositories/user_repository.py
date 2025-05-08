from ..models import db
class UserRepository:
    """
    UserRepository class to handle user-related database operations.
    """

    def add(self, user,user_profile):
        """
        Create a new user in the database.
        """
        db.session.add(user)
        db.session.commit()
        user_profile.user_id = user.id
        db.session.add(user_profile)
        db.session.commit()
        return user, user_profile