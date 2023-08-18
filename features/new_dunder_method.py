class Session:
    _session = None

    def __new__(cls, *args, **kwargs):
        if cls._session is None:
            print("Creating new session")
            cls._session = super().__new__(cls)
        return cls._session


if __name__ == "__main__":
    session1 = Session()
    session2 = Session()
    print(session1 is session2)  # True
