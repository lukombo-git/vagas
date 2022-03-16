"""Initial migration.

Revision ID: 1cbf27515f20
Revises: 
Create Date: 2022-03-06 06:30:31.913268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cbf27515f20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vagas',
    sa.Column('id_vaga', sa.Integer(), nullable=False),
    sa.Column('titulo_vaga', sa.String(length=255), nullable=True),
    sa.Column('categoria_vaga', sa.String(length=255), nullable=True),
    sa.Column('area_candidatura', sa.String(length=255), nullable=True),
    sa.Column('descricao_vaga', sa.String(length=255), nullable=True),
    sa.Column('tipo_vaga', sa.String(length=255), nullable=True),
    sa.Column('requisitos_vaga', sa.String(length=255), nullable=True),
    sa.Column('perfil_candidato', sa.String(length=255), nullable=True),
    sa.Column('habilitacoes', sa.String(length=255), nullable=True),
    sa.Column('provincia_vaga', sa.String(length=255), nullable=True),
    sa.Column('nivel_ingles_vaga', sa.String(length=255), nullable=True),
    sa.Column('habilidades_exigida', sa.String(length=255), nullable=True),
    sa.Column('experiencia_profissional', sa.String(length=255), nullable=True),
    sa.Column('anos_exp_exigida', sa.String(length=255), nullable=True),
    sa.Column('data_inicio_vaga', sa.String(length=255), nullable=True),
    sa.Column('data_termino_vaga', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id_vaga')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vagas')
    # ### end Alembic commands ###