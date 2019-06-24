import json


def read_entry(entry, *path):
    """
        entry: Gesuchten Eintrag; path optional bei Unterverzeichnissen - jeden Schritt in richtiger Reihenfolge angeben
    """
    with open('../config.json', encoding='utf-8') as file:
        d = json.load(file)
        if path:
            try:
                for p in path:
                    d = d[p]
                return d[entry]
            except KeyError:
                return '__KEY_ERROR__1'
        else:
            try:
                return d[entry]
            except KeyError:
                return '__KEY_ERROR__2'


if __name__ == '__main__':
    print(read_entry('clublist'))
