import random
import string
from base.stubs import stubs


class Utils:

    @staticmethod
    def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
        """
        Generates random string with chars and digits.
        :param size: string length expected (default is 8).
        :param chars: string characters consistency.
        :return: random string.
        """
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def validate_text(text):
        """

        :param text:
        :return:
        """
        if stubs.isUIused():
            return
        if isinstance(text, str):
            if len([char for char in text]) <= 244:
                return True
        else:
            raise Exception(F"{'Text should not be longer than 255 characters'}")

    @staticmethod
    def adjust_template(template):
        template.set_id(Utils.random_string_generator(50))
        template.set_parent_org(Utils.random_string_generator(5))
        return template

    @staticmethod
    def validate_percentage(quantity_allocated, quantity_unallocated):
        try:
            return (quantity_allocated + quantity_unallocated) == 100.0
        except Exception as ex:
            print(ex.__context__)
            raise Exception(F"{'The total allocation to all selected funds has to equal 100%'}")