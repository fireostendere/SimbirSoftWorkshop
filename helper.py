import allure
from typing import List
from faker import Faker

faker = Faker()


class Helper:
    @staticmethod
    def get_random_last_name() -> str:
        last_name = faker.last_name()
        allure.attach(last_name, name="Random Last Name", attachment_type=allure.attachment_type.TEXT)
        return last_name

    @staticmethod
    def get_random_postcode() -> int:
        postcode = faker.random_number(digits=10)
        allure.attach(str(postcode), name='Random Postcode', attachment_type=allure.attachment_type.TEXT)
        return postcode

    @staticmethod
    @allure.step('convert postcode to name')
    def convert_postcode_to_name(postcode: int) -> str:
        postcode_as_string = str(postcode)
        first_name = ''
        for i in range(0, len(postcode_as_string), 2):
            digit = int(postcode_as_string[i:i + 2])
            first_name += chr(97 + digit % 26)
        first_name = first_name.capitalize()
        allure.attach(first_name, name='First Name from Postcode', attachment_type=allure.attachment_type.TEXT)
        return first_name

    @allure.step('get closest to average name')
    def get_closest_to_average_name(self, names: List[str]) -> str:
        """
        This method retrieves the name whose length is closest to the average name length.
        """
        lengths = [len(name) for name in names]
        average_length = sum(lengths) / len(lengths)
        closest_name = min(names, key=lambda name: abs(len(name) - average_length))
        return closest_name

    @allure.step('get index of name')
    def get_index_of_name(self, names: List[str], name: str) -> int:
        """
        This method retrieves the index of the given name in the list of names.
        """
        index = names.index(name)
        return index
