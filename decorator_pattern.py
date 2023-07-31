parsers = {}


def extension(*exts):
    def register(parser):
        for ext in exts:
            parsers[ext] = parser
        return parser

    return register


@extension('json')
def json_parser(file):
    print('json_parser')


@extension('xml')
def xml_parser(file):
    print('xml_parser')


def parse_file(file):
    ext = file.split('.')[-1]
    parser = parsers.get(ext)
    if not parser:
        raise Exception(f'No parser for the extension {ext}')
    return parser(file)


if __name__ == '__main__':
    parse_file('test.json')
    parse_file('test.xml')
