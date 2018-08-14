import os


def get_full_path(db_filename: str) -> str:
    this_folder = os.path.dirname(__file__)
    return os.path.join(this_folder, db_filename)
