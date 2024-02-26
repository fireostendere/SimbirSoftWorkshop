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
    def convert_postcode_to_name(postcode: int) -> str:
        postcode_as_string = str(postcode)
        first_name = ''
        for i in range(0, len(postcode_as_string), 2):
            digit = int(postcode_as_string[i:i + 2])
            first_name += chr(97 + digit % 26)
        first_name = first_name.capitalize()
        allure.attach(first_name, name='First Name from Postcode', attachment_type=allure.attachment_type.TEXT)
        return first_name

    @staticmethod
    def get_closest_to_average_name(names: List[str]) -> str:
        lengths = [len(name) for name in names]
        average_length = sum(lengths) / len(lengths)
        closest_name = min(names, key=lambda name: abs(len(name) - average_length))
        return closest_name

    @staticmethod
    def get_index_of_name(names: List[str], name: str) -> int:
        index = names.index(name)
        return index
    