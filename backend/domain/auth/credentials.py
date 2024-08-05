from typing import Annotated

from fastapi import Depends

from backend.settings import settings


def build_public_key() -> bytes:
    with open(settings.public_key_path, "rb") as f:
        return f.read()


PublicKeyD = Annotated[bytes, Depends(build_public_key)]


def build_private_key() -> bytes:
    with open(settings.private_key_path, "rb") as f:
        return f.read()


PrivateKeyD = Annotated[bytes, Depends(build_private_key)]
