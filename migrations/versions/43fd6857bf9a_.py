"""empty message

Revision ID: 43fd6857bf9a
Revises: d318a3f9d800
Create Date: 2017-11-26 14:37:45.214887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43fd6857bf9a'
down_revision = 'd318a3f9d800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('category_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'recipe_catrgory_id_fkey', 'recipe', type_='foreignkey')
    op.create_foreign_key(None, 'recipe', 'category', ['category_id'], ['category_id'])
    op.drop_column('recipe', 'catrgory_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('catrgory_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'recipe', type_='foreignkey')
    op.create_foreign_key(u'recipe_catrgory_id_fkey', 'recipe', 'category', ['catrgory_id'], ['category_id'])
    op.drop_column('recipe', 'category_id')
    # ### end Alembic commands ###
