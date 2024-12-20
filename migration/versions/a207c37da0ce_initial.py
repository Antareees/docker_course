"""initial

Revision ID: a207c37da0ce
Revises: 
Create Date: 2024-11-03 19:27:49.783957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a207c37da0ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=255), nullable=False),
    sa.Column('genre_desc', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hosts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host_name', sa.String(length=255), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_name', sa.String(length=255), nullable=False),
    sa.Column('duration', sa.Time(), nullable=False),
    sa.Column('program_ratings', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(length=255), nullable=False),
    sa.Column('country_name', sa.String(length=100), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('host_program_pair',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('host_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['host_id'], ['hosts.id'], ),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('airtime', sa.Time(), nullable=False),
    sa.Column('playlist_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_name', sa.String(length=255), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('duration', sa.Time(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_name', sa.String(length=255), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('year_of_release', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlist_and_track_pair',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('request_time', sa.Time(), nullable=False),
    sa.Column('request_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song_requests')
    op.drop_table('playlist_and_track_pair')
    op.drop_table('album')
    op.drop_table('tracks')
    op.drop_table('playlists')
    op.drop_table('host_program_pair')
    op.drop_table('artists')
    op.drop_table('programs')
    op.drop_table('hosts')
    op.drop_table('genres')
    # ### end Alembic commands ###
