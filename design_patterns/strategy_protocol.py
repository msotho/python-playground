from typing import Protocol


class Auth(Protocol):
    def login(self, username: str, password: str) -> bool:
        ...


class Facebook(Auth):
    def login(self, username: str, password: str) -> bool:
        print(f"Authenticating {username}:{password} with Facebook")

        return True


class Google(Auth):
    def login(self, username: str, password: str) -> bool:
        print(f"Authenticating {username}:{password} with Google")

        return True


def login(auth: Auth, username: str, password: str) -> bool:
    return auth.login(username, password)


if __name__ == "__main__":
    facebook = Facebook()
    google = Google()

    login(facebook, username="user", password="pass")
    login(google, username="user", password="pass")
