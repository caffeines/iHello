import bcrypt


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=12)).decode(
        "utf-8"
    )


def check_password(password: str, hash_pass: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hash_pass.encode("utf-8"))
