def check_uniq(name):
    if name is not None:
        return True


def isUIused():
    """
    It's a stub function, here can be check if UI connected, so will sent True
    :return: Always False
    """
    return False


def get_authorization():
    """
    It's a stub of Authorization function
    :return: True
    """
    return True


def login_to_system(credentials):
    """
    It's a stub of Authorization function
    :param credentials:
    :return: True if credentials is valid otherwise False
    """
    return True if credentials else False


def populate_and_schedule(allocation_template):
    # TODO: populate template and schedule for upload
    return allocation_template
