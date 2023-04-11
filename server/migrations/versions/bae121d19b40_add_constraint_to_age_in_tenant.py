"""add constraint to age in Tenant

Revision ID: bae121d19b40
Revises: a4e256819733
Create Date: 2023-04-11 11:01:30.786488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bae121d19b40'
down_revision = 'a4e256819733'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenants', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###