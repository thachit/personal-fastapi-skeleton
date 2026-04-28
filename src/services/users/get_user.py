from src.db.db import get_session
from src.models.user import User


async def get_all_users():
    with get_session() as session:
        user_objs = session.query(User).all()

        return user_objs