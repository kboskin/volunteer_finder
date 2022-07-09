
import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref

from enigine import Base


class Categories(Base):
    __tablename__ = "catalogue"
    id = sa.Column("id", sa.Integer, primary_key=True)
    parent_id = sa.Column("parent_id", sa.Integer, sa.ForeignKey(id))
    parent = relationship("Categories", backref='parent_category', remote_side=id)

    category_name = sa.Column("category_name", sa.String)
