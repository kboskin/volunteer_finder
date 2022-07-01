import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression

from enigine import metadata

Categories = sa.Table(
    "categories",
    metadata,
    sa.Column('category_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sa.Column('category_name', sa.String),
    sa.Column('category_description', sa.String),
    sa.Column('parent_id', sa.ForeignKey("categories.category_id")),
    sa.Column('is_active', sa.Boolean, server_default=expression.true(), nullable=False),
    sa.Column('deleted', sa.Boolean, server_default=expression.false(), nullable=False),
)