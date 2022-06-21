import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import UUID

from main import metadata, engine

UserTable = sa.Table(
    "users",
    metadata,
    sa.Column('user_id', UUID(as_uuid=True), primary_key=True),
    sa.Column('fist_name', sa.String),
    sa.Column('last_name', sa.String),
    sa.Column('phone_number', sa.String(20), unique=True),
    sa.Column('email', sa.String, unique=True),
    sa.Column('isActive', sa.Boolean, server_default=expression.true(), nullable=False),
    sa.Column('deleted', sa.Boolean, server_default=expression.false(), nullable=False),
    sa.Column('created_time', sa.DateTime, server_default=func.now(), nullable=False),
    sa.Column('updated_time', sa.DateTime, server_default=func.now(), nullable=False),
    sa.Column('deleted_time', sa.DateTime),
)

UserToCategoryTable = sa.Table(
    "user_to_category",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('user_id', UUID(as_uuid=True)),
    sa.Column('category_id', UUID(as_uuid=True)),
)

UserFeedbackTable = sa.Table(
    "user_to_category",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('id_from', UUID(as_uuid=True), nullable=False),
    sa.Column('id_to', UUID(as_uuid=True), nullable=False),
    sa.Column('rating', sa.DECIMAL, nullable=False),
    sa.Column('date', sa.DateTime, server_default=func.now(), nullable=False)
)

UserSuperpowersTable = sa.Table(
    "user_to_superpower",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('user_id', UUID(as_uuid=True), nullable=False),
    sa.Column('superpower', sa.String, nullable=False),
)

metadata.create_all(engine)