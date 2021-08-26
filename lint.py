import pathlib
from operator import itemgetter

import yaml

HERE = pathlib.Path(__file__).parent.resolve()
PATH = HERE.joinpath("_data", "library.yml")


def main():
    with PATH.open() as file:
        data = yaml.safe_load(file)
    data = sorted(data, key=itemgetter("year"), reverse=True)
    with PATH.open("w") as file:
        yaml.safe_dump(data, file, sort_keys=True, allow_unicode=True)


if __name__ == '__main__':
    main()
