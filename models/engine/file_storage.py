class FileStorage:
    # Existing code ...

    def close(self):
        """Close the storage."""
        self.reload()
