class ServiceError(Exception):
    """Exception raised for business logic errors"""

    pass


class DatabaseError(Exception):
    """Exception raised for database operation errors"""

    pass


class ResourceNotFoundError(Exception):
    """Exception raised for entity not found errors"""

    pass
