import glob


class File:
    def __init__(self, id, label_id, path):
        self.id = id
        self.label_id = label_id
        self.path = path


def get_files(path):
    return glob.glob(r'' + path)


if __name__ == '__main__':
    get_files('./images/*.png')
