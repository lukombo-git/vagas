from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

#Creating the areas model
class Vagas(db.Model):
    id_vaga = db.Column(db.Integer, primary_key=True)
    titulo_vaga = db.Column(db.String(255))
    categoria_vaga = db.Column(db.String(255))
    area_candidatura  = db.Column(db.String(255))
    descricao_vaga = db.Column(db.String(255))
    tipo_vaga = db.Column(db.String(255))
    requisitos_vaga = db.Column(db.String(255))
    perfil_candidato = db.Column(db.String(255))
    habilitacoes = db.Column(db.String(255))
    provincia_vaga = db.Column(db.String(255))
    nivel_ingles_vaga = db.Column(db.String(255))
    habilidades_exigida = db.Column(db.String(255))
    experiencia_profissional = db.Column(db.String(255))
    anos_exp_exigida = db.Column(db.String(255))
    data_inicio_vaga = db.Column(db.String(255))
    data_termino_vaga = db.Column(db.String(255))

    def __repr__(self):
        return f'<vaga {self.id_vaga} {self.titulo_vaga}'
    
    def serialize(self):
        return {
            'id_vaga':self.id_vaga,
            'titulo_Vaga':self.titulo_vaga,
            'categoria_vaga':self.categoria_vaga,
            'tipo_vaga':self.tipo_vaga,
            'descricao_vaga':self.descricao_vaga,
            'requisitos_vaga':self.requisitos_vaga,
            'anos_exp_exigida':self.anos_exp_exigida,
            'experiencia_profissional':self.experiencia_profissional,
            'area_candidatura':self.area_candidatura,
            'perfil_candidato':self.perfil_candidato,
            'habilitacoes':self.habilitacoes,
            'provincia_vaga':self.provincia_vaga,
            'nivel_ingles_vaga':self.nivel_ingles_vaga,
            'habilidades_exigida':self.habilidades_exigida,
            'data_inicio_vaga':self.data_inicio_vaga,
            'data_termino_vaga':self.data_termino_vaga
        }