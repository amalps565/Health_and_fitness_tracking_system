from src.models.user import User
from src.models.user_profile import UserProfile
from src.utils.logger import setup_logger
from ..models import db

logger = setup_logger(__name__)
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
    def get_all_user(self):
        """
        Get all users from the database.
        """
        users=User.query.join(UserProfile).all()
        logger.info(f"Fetched all users: {users}")
        return users
    def get_user_profile(self):
        """
        Get all user profiles from the database.
        """
        user_profiles = UserProfile.query.all()
        logger.info(f"Fetched all user profiles: {user_profiles}")
        return user_profiles
    def get_userby_id(self, user_id):
        """
        Get a user by ID from the database.
        """
        user = User.query.get(user_id)
        if not user:
            return None
        return user