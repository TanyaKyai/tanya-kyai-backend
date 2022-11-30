"""empty message

Revision ID: b484abf3d1fa
Revises: 7087b80e8072
Create Date: 2022-11-30 10:54:36.606885

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b484abf3d1fa'
down_revision = '7087b80e8072'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('filename', sa.String(length=50), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('bahtsul')
    op.add_column('fatwa', sa.Column('docs_id', sa.BigInteger(), nullable=True))
    op.drop_constraint('fatwa_ibfk_1', 'fatwa', type_='foreignkey')
    op.create_foreign_key(None, 'fatwa', 'document', ['docs_id'], ['id'])
    op.drop_column('fatwa', 'gambar_id')
    op.drop_constraint('post_ibfk_1', 'post', type_='foreignkey')
    op.drop_column('post', 'gambar_id')
    op.drop_constraint('tanya_ibfk_1', 'tanya', type_='foreignkey')
    op.drop_column('tanya', 'gambar_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tanya', sa.Column('gambar_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True))
    op.create_foreign_key('tanya_ibfk_1', 'tanya', 'gambar', ['gambar_id'], ['id'])
    op.add_column('post', sa.Column('gambar_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True))
    op.create_foreign_key('post_ibfk_1', 'post', 'gambar', ['gambar_id'], ['id'])
    op.add_column('fatwa', sa.Column('gambar_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'fatwa', type_='foreignkey')
    op.create_foreign_key('fatwa_ibfk_1', 'fatwa', 'gambar', ['gambar_id'], ['id'])
    op.drop_column('fatwa', 'docs_id')
    op.create_table('bahtsul',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('judul', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('tema', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('isi', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('gambar_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['gambar_id'], ['gambar.id'], name='bahtsul_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('document')
    # ### end Alembic commands ###
