import uuid

import sqlalchemy as sa
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import UUID

from enigine import Base


class User(Base):
    __tablename__ = "users"
    user_id = sa.Column('user_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = sa.Column('first_name', sa.String)
    last_name = sa.Column('last_name', sa.String)
    phone_number = sa.Column('phone_number', sa.String(20), unique=True)
    email = sa.Column('email', sa.String, unique=True)
    is_active = sa.Column('is_active', sa.Boolean, server_default=expression.true(), nullable=False)
    deleted = sa.Column('deleted', sa.Boolean, server_default=expression.false(), nullable=False)
    created_time = sa.Column('created_time', sa.DateTime, server_default=func.now(), nullable=False)
    updated_time = sa.Column('updated_time', sa.DateTime, server_default=func.now(), nullable=False)
    deleted_time = sa.Column('deleted_time', sa.DateTime)
    feedbacks = relationship('UserFeedback',  primaryjoin='User.user_id == UserFeedback.receiver_id', uselist=True, lazy='joined')


class UserFeedback(Base):
    __tablename__ = "user_feedbacks"
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    sender_id = sa.Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    receiver_id = sa.Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

    rating = sa.Column('rating', sa.DECIMAL, nullable=False)
    feedback = sa.Column('feedback', sa.String, nullable=False)
    date = sa.Column('date', sa.DateTime, server_default=func.now(), nullable=False)