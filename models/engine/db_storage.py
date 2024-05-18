from sqlalchemy.orm import sessionmaker

class DBStorage:
    # Existing code ...

    def close(self):
        """Close the storage."""
        self.__session.close()
