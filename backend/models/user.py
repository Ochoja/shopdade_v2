class User:
    def __init__(self, full_name: str, email: str, password: str) -> None:
        self.full_name = full_name
        self.email = email
        self.password = password

    def to_dict(self) -> None:
        return ({
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password
        })

    @staticmethod
    def from_dict(data):
        return User(
            data.get("full_name"),
            data.get("email"),
            data.get("password")
        )
