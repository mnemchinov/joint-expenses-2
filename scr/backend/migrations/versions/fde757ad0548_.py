"""empty message

Revision ID: fde757ad0548
Revises: 
Create Date: 2023-05-03 15:20:07.919285

"""
import sqlalchemy as sa
import sqlmodel  # NEW
from alembic import op

# revision identifiers, used by Alembic.
revision = 'fde757ad0548'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
                    sa.Column('date', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.Column('created_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('status',
                              sa.Enum('NEW', 'READY', 'DELIVERED', 'CANCELED',
                                      name='orderstatuses'), nullable=True),
                    sa.Column('amount', sa.Numeric(precision=10, scale=2),
                              nullable=True),
                    sa.Column('debit', sa.Numeric(precision=10, scale=2),
                              nullable=True),
                    sa.Column('opening_balance',
                              sa.Numeric(precision=10, scale=2), nullable=True),
                    sa.Column('final_balance',
                              sa.Numeric(precision=10, scale=2), nullable=True),
                    sa.Column('content', sa.JSON(), nullable=True),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False),
                    sa.Column('previous_order_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['previous_order_id'],
                                            ['orders.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('partners',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('order_partners',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('order_id', sa.Integer(), nullable=False),
                    sa.Column('partner_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
                    sa.ForeignKeyConstraint(['partner_id'], ['partners.id'], ),
                    sa.PrimaryKeyConstraint('id', 'order_id', 'partner_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_partners')
    op.drop_table('partners')
    op.drop_table('orders')
    # ### end Alembic commands ###
