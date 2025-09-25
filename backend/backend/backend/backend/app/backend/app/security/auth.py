import os, time, jwt
from fastapi import Header, HTTPException

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
ALGO = "HS256"

def issue_token(*, sub: str, role: str = "owner", ttl: int = 3600) -> str:
    now = int(time.time())
    payload = {"sub": sub, "role": role, "iat": now, "exp": now + ttl}
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGO)

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGO])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
