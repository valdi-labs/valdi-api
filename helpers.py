import uuid


def is_valid_uuid(s):
    try:
        uuid.UUID(s)
        return True
    except ValueError:
        return False
