from passlib.handlers.argon2 import argon2


async def hash_data(pwd: str):
    return argon2.hash(pwd.encode())


async def verify_data_hash(data: str, target_hash: str) -> bool:
    return argon2.verify(data, target_hash)
