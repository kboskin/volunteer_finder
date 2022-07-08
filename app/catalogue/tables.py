import uuid

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from enigine import Base


class Catalogue(Base):
    __tablename__ = "catalogue"
    id = sa.Column('id', sa.Integer, primary_key=True)
    category_name = sa.Column("category_name", sa.String)
    parent_id = sa.ForeignKey("catalogue.id")
    parent = relationship('Catalogue', remote_side=[id])


Base.metadata.create_all()