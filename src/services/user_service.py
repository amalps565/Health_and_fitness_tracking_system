from datetime import datetime

from src.models.user_profile import UserProfile
from src.utils.logger import setup_logger
from ..models import db
from ..models.user import User
from ..schemas.user import UserSchema
from ..contracts.user_dto import UserDTO, UserResponseDTO
from ..repositories.user_repository import UserRepository
from src.repositories import user_repository

logger=setup_logger(__name__)

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    def create_users(self,user_data_list):
       logger.info("Creating user")
       user_DTO= UserDTO(**user_data_list)
       user=self._create_user_object(user_DTO)
       user_profile=self._create_userprofile_object(user_DTO)
       saved_user=self.user_repository.add(user,user_profile)
       return UserResponseDTO(
            user_id=saved_user[0].id,
            username=saved_user[0].username,
            email=saved_user[0].email,
            registration_date=saved_user[0].registration_date,
            height=saved_user[1].height_cm,
            fitness_level=saved_user[1].fitness_level,
            goals=saved_user[1].goals,
            weight=saved_user[1].weight_kg,
            age=saved_user[1].age,
            health_conditions=saved_user[1].health_conditions

        )


    def _create_user_object(self, user_dto):
        return User(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password,
            registration_date=datetime.now(),
        )
    def _create_userprofile_object(self, user_dto):
        return UserProfile(
            height_cm=user_dto.height,
            weight_kg=user_dto.weight,
            age=user_dto.age,
            fitness_level=user_dto.fitness_level,
            goals=user_dto.goals,
            health_conditions=user_dto.health_conditions
        )
    
    def get_all_users(self):
        users=self.user_repository.get_all_user()
        # user_profile=self.user_repository.get_user_profile()
        user_dtos=[]
        
        for user in users:
            user_profile= UserProfile.query.filter_by(user_id=user.id).first()
            user_dtos.append(
                UserResponseDTO(
                    user_id=user.id,
                    username=user.username,
                    email=user.email,
                    registration_date=user.registration_date,
                    height=user_profile.height_cm,
                    fitness_level=user_profile.fitness_level,
                    goals=user_profile.goals,
                    weight=user_profile.weight_kg,
                    age=user_profile.age,
                    health_conditions=user_profile.health_conditions

                
                )
                # for user in users

            )
        return user_dtos
    def get_user_by_id(self, user_id):
        """
        Get a user by ID from the database.
        """ 
        user=self.user_repository.get_userby_id(user_id)
        user_profile= UserProfile.query.filter_by(user_id=user.id).first()
        if not user_profile:
            user_profile = None
        return UserResponseDTO(
            user_id=user.id,
            username=user.username,
            email=user.email,
            registration_date=user.registration_date,
            height=user_profile.height_cm,
            fitness_level=user_profile.fitness_level,
            goals=user_profile.goals,
            weight=user_profile.weight_kg,
            age=user_profile.age,
            health_conditions=user_profile.health_conditions
        )

