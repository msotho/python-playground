from pathlib import Path


class JsonParser:
    @staticmethod
    def parse(file):
        print(f"Parse {file} with json_parser")


class XmlParser:
    @staticmethod
    def parse(file):
        print(f"Parse {file} with xml_parser")


PARSERS = {
    "json": JsonParser,
    "xml": XmlParser,
}


class Factory:
    def __init__(self, file_format: str):
        self.file_format = file_format

    def get_parser(self):
        parser = PARSERS[self.file_format]()

        if not parser:
            raise Exception(f"No parser for the extension {format}")

        return parser


if __name__ == "__main__":
    factory = Factory("json")
    file_parser = factory.get_parser()
    file_parser.parse("test.json")

    factory = Factory("xml")
    file_parser = factory.get_parser()
    file_parser.parse("test.xml")
