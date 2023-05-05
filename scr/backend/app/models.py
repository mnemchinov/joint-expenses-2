import enum
from datetime import datetime
from typing import Optional, List

from sqlalchemy import Column, func, Enum, Numeric, JSON
from sqlalchemy import DateTime
from sqlmodel import SQLModel, Field, Relationship


class OrderStatuses(enum.IntEnum):
    NEW = 0
    READY = 1
    DELIVERED = 2
    CANCELED = 3


class OrderPartners(SQLModel, table=True):
    __tablename__ = 'order_partners'

    order_id: Optional[int] = Field(
        default=None,
        foreign_key='orders.id',
        primary_key=True
    )
    partner_id: Optional[int] = Field(
        default=None,
        foreign_key='partners.id',
        primary_key=True
    )


class Partner(SQLModel, table=True):
    __tablename__ = 'partners'

    id: Optional[int] = Field(primary_key=True)
    name: str = Field()
    email: Optional[str] = Field()
    orders: Optional[List['Order']] = Relationship(
        back_populates='partners',
        link_model=OrderPartners
    )


class Order(SQLModel, table=True):
    __tablename__ = 'orders'

    id: Optional[int] = Field(primary_key=True)
    date: Optional[datetime] = Field(
        sa_column=Column(DateTime,
                         server_default=func.now())
    )
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime,
                         server_default=func.now())
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime,
                         server_onupdate=func.now())
    )
    is_deleted: Optional[bool] = Field()
    status: Optional[OrderStatuses] = Field(
        sa_column=Column(
            Enum(OrderStatuses), default=OrderStatuses.NEW)
    )
    amount: Optional[float] = Field(
        sa_column=Column(Numeric(10, 2), default=0)
    )
    debit: Optional[float] = Field(
        sa_column=Column(Numeric(10, 2), default=0)
    )
    opening_balance: Optional[float] = Field(
        sa_column=Column(Numeric(10, 2), default=0)
    )
    final_balance: Optional[float] = Field(
        sa_column=Column(Numeric(10, 2), default=0)
    )
    previous_order_id: Optional[int] = Field(
        default=None,
        foreign_key='orders.id'
    )
    content: Optional[dict] = Field(
        sa_column=Column(JSON),
        default={}
    )
    partners: List[Partner] = Relationship(
        back_populates='orders',
        link_model=OrderPartners
    )

    class Config:
        arbitrary_types_allowed = True
