from dataclasses import dataclass


@dataclass
class AuthState:
    username: str = None
    password: str = None
    state: bool = False


class Auth:
    auth_state = AuthState()

    def login(self, username: str, password: str) -> None:
        self.auth_state.username = username
        self.auth_state.password = password
        self.auth_state.state = True

    def logout(self) -> None:
        self.auth_state.username = None
        self.auth_state.password = None
        self.auth_state.state = False

    def is_logged_in(self) -> bool:
        return self.auth_state.state

    def get_logged_in_user(self) -> AuthState:
        return self.auth_state


if __name__ == "__main__":
    auth = Auth()
    auth.login(username="user", password="pass")
    print(auth.is_logged_in())
    print(auth.get_logged_in_user())

    auth.logout()
    print(auth.is_logged_in())
