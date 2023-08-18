def login(auth: callable, username: str, password: str) -> bool:
    return auth(username, password)


def facebook_auth(username: str, password: str) -> bool:
    print(f"Authenticating {username}:{password} with Facebook")

    return True


def google_auth(username: str, password: str) -> bool:
    print(f"Authenticating {username}:{password} with Google")

    return True


if __name__ == "__main__":
    login(facebook_auth, username="user", password="pass")
    login(google_auth, username="user", password="pass")
