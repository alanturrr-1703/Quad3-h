# image_store.py

import os


class ImageStore:
    def __init__(self, directory: str):
        """
        Initialize the image store by specifying a directory for storing images.
        :param directory: Path to the directory where images will be stored.
        """
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save_image(self, image_name: str, image_data: bytes) -> str:
        """
        Save image data to the specified directory.
        :param image_name: Name of the image file.
        :param image_data: Image file data (bytes).
        :return: Path to the saved image file.
        """
        file_path = os.path.join(self.directory, image_name)
        with open(file_path, 'wb') as image_file:
            image_file.write(image_data)
        return file_path

    def load_image(self, image_name: str) -> bytes:
        """
        Load image data from a file.
        :param image_name: Name of the image file.
        :return: Image file data (bytes).
        """
        file_path = os.path.join(self.directory, image_name)
        with open(file_path, 'rb') as image_file:
            return image_file.read()

    def delete_image(self, image_name: str) -> bool:
        """
        Delete an image from the store.
        :param image_name: Name of the image file.
        :return: True if the file was successfully deleted, False otherwise.
        """
        file_path = os.path.join(self.directory, image_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
