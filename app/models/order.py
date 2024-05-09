from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.csv_loader import csv_loader
from app.db.core import ModelBase, sync_session
from app.db.types import created_at, intpk
from app.enums import OrderStatus


class OrderModel(ModelBase):
    __tablename__ = "orders"

    id: Mapped[intpk]
    # 'CASCADE' - delete all related orders after a user deletion
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    status: Mapped[OrderStatus]
    created_at: Mapped[created_at]


def _insert_mock_orders():
    # 'users' table has to be registered in the metadata to have a relationship
    import app.models.user  # noqa

    with sync_session.begin() as session:
        mock_orders = csv_loader.load("orders")
        orders = [
            OrderModel(user_id=int(order["user_id"]), status=order["status"])
            for order in mock_orders
        ]
        session.add_all(orders)


if __name__ == "__main__":
    _insert_mock_orders()
