from app.db import ModelBase, sync_engine

# isort: split
from app.models.user import UserModel  # noqa


def _reset_db():
    ModelBase.metadata.drop_all(sync_engine)
    ModelBase.metadata.create_all(sync_engine)


if __name__ == "__main__":
    _reset_db()
