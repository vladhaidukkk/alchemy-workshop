from app.db.core import metadata, sync_engine

# isort: split
from app.tables.users import users_table  # noqa


def _reset_db():
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)


if __name__ == "__main__":
    _reset_db()
