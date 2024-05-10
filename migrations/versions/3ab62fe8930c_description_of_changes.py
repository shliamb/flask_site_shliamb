"""Description of changes

Revision ID: 3ab62fe8930c
Revises: 
Create Date: 2024-05-10 12:15:47.496245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ab62fe8930c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page_1',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('seo_title', sa.String(length=1000), nullable=True),
    sa.Column('seo_description', sa.String(length=1000), nullable=True),
    sa.Column('seo_keyword', sa.String(length=500), nullable=True),
    sa.Column('text_body', sa.String(length=5000), nullable=True),
    sa.Column('id_who_changed', sa.BigInteger(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_update', sa.DateTime(), nullable=True),
    sa.Column('changefreq', sa.String(length=500), nullable=False),
    sa.Column('priority', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_page_1_changefreq'), 'page_1', ['changefreq'], unique=False)
    op.create_index(op.f('ix_page_1_id'), 'page_1', ['id'], unique=True)
    op.create_index(op.f('ix_page_1_publish'), 'page_1', ['publish'], unique=False)
    op.create_index(op.f('ix_page_1_seo_description'), 'page_1', ['seo_description'], unique=False)
    op.create_index(op.f('ix_page_1_seo_keyword'), 'page_1', ['seo_keyword'], unique=False)
    op.create_index(op.f('ix_page_1_seo_title'), 'page_1', ['seo_title'], unique=False)
    op.create_index(op.f('ix_page_1_text_body'), 'page_1', ['text_body'], unique=False)
    op.create_index(op.f('ix_page_1_title'), 'page_1', ['title'], unique=False)
    op.create_table('page_main',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_site', sa.String(length=100), nullable=False),
    sa.Column('responsive', sa.Boolean(), nullable=False),
    sa.Column('lang', sa.String(length=100), nullable=False),
    sa.Column('return_code', sa.Integer(), nullable=False),
    sa.Column('comments', sa.Boolean(), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('seo_title', sa.String(length=1000), nullable=True),
    sa.Column('seo_description', sa.String(length=1000), nullable=True),
    sa.Column('seo_keyword', sa.String(length=500), nullable=True),
    sa.Column('text_body', sa.String(length=5000), nullable=True),
    sa.Column('id_who_changed', sa.BigInteger(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_update', sa.DateTime(), nullable=True),
    sa.Column('changefreq', sa.String(length=500), nullable=False),
    sa.Column('priority', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_page_main_changefreq'), 'page_main', ['changefreq'], unique=False)
    op.create_index(op.f('ix_page_main_comments'), 'page_main', ['comments'], unique=False)
    op.create_index(op.f('ix_page_main_id'), 'page_main', ['id'], unique=False)
    op.create_index(op.f('ix_page_main_lang'), 'page_main', ['lang'], unique=False)
    op.create_index(op.f('ix_page_main_publish'), 'page_main', ['publish'], unique=False)
    op.create_index(op.f('ix_page_main_responsive'), 'page_main', ['responsive'], unique=False)
    op.create_index(op.f('ix_page_main_return_code'), 'page_main', ['return_code'], unique=False)
    op.create_index(op.f('ix_page_main_seo_description'), 'page_main', ['seo_description'], unique=False)
    op.create_index(op.f('ix_page_main_seo_keyword'), 'page_main', ['seo_keyword'], unique=False)
    op.create_index(op.f('ix_page_main_seo_title'), 'page_main', ['seo_title'], unique=False)
    op.create_index(op.f('ix_page_main_text_body'), 'page_main', ['text_body'], unique=False)
    op.create_index(op.f('ix_page_main_title'), 'page_main', ['title'], unique=False)
    op.create_index(op.f('ix_page_main_url_site'), 'page_main', ['url_site'], unique=False)
    op.create_table('sitemap',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_main_id', sa.String(length=100), nullable=True),
    sa.Column('date_main', sa.DateTime(), nullable=True),
    sa.Column('page_1_id', sa.String(length=100), nullable=True),
    sa.Column('date_page_1', sa.DateTime(), nullable=True),
    sa.Column('page_2_id', sa.String(length=100), nullable=True),
    sa.Column('date_page_2', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sitemap_page_2_id'), 'sitemap', ['page_2_id'], unique=True)
    op.create_table('page_2',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=1000), nullable=True),
    sa.Column('seo_title', sa.String(length=1000), nullable=True),
    sa.Column('seo_description', sa.String(length=1000), nullable=True),
    sa.Column('seo_keyword', sa.String(length=500), nullable=True),
    sa.Column('text_body', sa.String(length=5000), nullable=True),
    sa.Column('id_who_changed', sa.BigInteger(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_update', sa.DateTime(), nullable=True),
    sa.Column('changefreq', sa.String(length=500), nullable=False),
    sa.Column('priority', sa.Float(), nullable=False),
    sa.Column('page_1_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['page_1_id'], ['page_1.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_page_2_changefreq'), 'page_2', ['changefreq'], unique=False)
    op.create_index(op.f('ix_page_2_id'), 'page_2', ['id'], unique=True)
    op.create_index(op.f('ix_page_2_publish'), 'page_2', ['publish'], unique=False)
    op.create_index(op.f('ix_page_2_seo_description'), 'page_2', ['seo_description'], unique=False)
    op.create_index(op.f('ix_page_2_seo_keyword'), 'page_2', ['seo_keyword'], unique=False)
    op.create_index(op.f('ix_page_2_seo_title'), 'page_2', ['seo_title'], unique=False)
    op.create_index(op.f('ix_page_2_text_body'), 'page_2', ['text_body'], unique=False)
    op.create_index(op.f('ix_page_2_title'), 'page_2', ['title'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('answer_to_id', sa.BigInteger(), nullable=True),
    sa.Column('id_autor', sa.BigInteger(), nullable=True),
    sa.Column('hidden_id', sa.UUID(), nullable=False),
    sa.Column('text_comment', sa.String(length=5000), nullable=True),
    sa.Column('img_comment', sa.String(length=1000), nullable=True),
    sa.Column('likes', sa.BigInteger(), nullable=True),
    sa.Column('who_liked', sa.String(length=5000), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.Column('is_block', sa.Boolean(), nullable=False),
    sa.Column('is_spam', sa.Boolean(), nullable=False),
    sa.Column('is_bot', sa.Boolean(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_update', sa.DateTime(), nullable=True),
    sa.Column('page_2_id', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['page_2_id'], ['page_2.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hidden_id')
    )
    op.create_index(op.f('ix_comments_img_comment'), 'comments', ['img_comment'], unique=False)
    op.create_index(op.f('ix_comments_is_block'), 'comments', ['is_block'], unique=False)
    op.create_index(op.f('ix_comments_is_bot'), 'comments', ['is_bot'], unique=False)
    op.create_index(op.f('ix_comments_is_spam'), 'comments', ['is_spam'], unique=False)
    op.create_index(op.f('ix_comments_publish'), 'comments', ['publish'], unique=False)
    op.create_index(op.f('ix_comments_text_comment'), 'comments', ['text_comment'], unique=False)
    op.create_index(op.f('ix_comments_who_liked'), 'comments', ['who_liked'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_who_liked'), table_name='comments')
    op.drop_index(op.f('ix_comments_text_comment'), table_name='comments')
    op.drop_index(op.f('ix_comments_publish'), table_name='comments')
    op.drop_index(op.f('ix_comments_is_spam'), table_name='comments')
    op.drop_index(op.f('ix_comments_is_bot'), table_name='comments')
    op.drop_index(op.f('ix_comments_is_block'), table_name='comments')
    op.drop_index(op.f('ix_comments_img_comment'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_page_2_title'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_text_body'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_seo_title'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_seo_keyword'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_seo_description'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_publish'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_id'), table_name='page_2')
    op.drop_index(op.f('ix_page_2_changefreq'), table_name='page_2')
    op.drop_table('page_2')
    op.drop_index(op.f('ix_sitemap_page_2_id'), table_name='sitemap')
    op.drop_table('sitemap')
    op.drop_index(op.f('ix_page_main_url_site'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_title'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_text_body'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_seo_title'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_seo_keyword'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_seo_description'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_return_code'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_responsive'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_publish'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_lang'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_id'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_comments'), table_name='page_main')
    op.drop_index(op.f('ix_page_main_changefreq'), table_name='page_main')
    op.drop_table('page_main')
    op.drop_index(op.f('ix_page_1_title'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_text_body'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_seo_title'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_seo_keyword'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_seo_description'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_publish'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_id'), table_name='page_1')
    op.drop_index(op.f('ix_page_1_changefreq'), table_name='page_1')
    op.drop_table('page_1')
    # ### end Alembic commands ###