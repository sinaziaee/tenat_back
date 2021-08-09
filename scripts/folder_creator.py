import os


def apply(path):
    if not os.path.exists(path):
        os.makedirs(path)
