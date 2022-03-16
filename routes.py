from flask import Blueprint, jsonify, request
from models import db, Vagas
from models import *

vagas_blueprint=Blueprint('vagas_api_routes',__name__,url_prefix='/api/vagas')


#createing a new candidate
@vagas_blueprint.route('/create', methods=['POST'])
def create_vagas():
    try:
        vaga = Vagas()
        vaga.titulo_vaga = request.form["titulo_vaga"]
        vaga.categoria_vaga = request.form["categoria_vaga"]
        vaga.area_candidatura  = request.form["area_candidatura"]
        vaga.descricao_vaga = request.form["descricao_vaga"]
        vaga.tipo_vaga = request.form["tipo_vaga"]
        vaga.requisitos_vaga = request.form["requisitos_vaga"]
        vaga.perfil_candidato = request.form["perfil_candidato"]
        vaga.habilitacoes = request.form["habilitacoes"]
        vaga.provincia_vaga = request.form["provincia_vaga"]
        vaga.nivel_ingles_vaga = request.form["nivel_ingles_vaga"]
        vaga.habilidades_exigida = request.form["habilidades_exigida"]
        vaga.experiencia_profissional = request.form["experiencia_profissional"]
        vaga.anos_exp_exigida = request.form["anos_exp_exigida"]
        vaga.data_inicio_vaga = request.form["data_inicio_vaga"]
        vaga.data_termino_vaga = request.form["data_termino_vaga"]
        db.session.commit()
        db.session.add(vaga)
        db.session.commit()
        response ={'message':'Vaga Criada com sucesso!','result':vaga.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message':'Erro ao criar a vaga'}
    return jsonify(response)

#updating a vaga
@vagas_blueprint.route('/update_vaga_id/<id_vaga>', methods=['GET','POST','PUT'])
def update_vaga(id_vaga):
    vaga = Vagas.query.get(id_vaga)
    try:
        vaga.titulo_vaga = request.form["titulo_Vaga"]
        vaga.categoria_vaga = request.form["categoria_vaga"]
        vaga.area_candidatura  = request.form["area_candidatura"]
        vaga.descricao_vaga = request.form["descricao_vaga"]
        vaga.tipo_vaga = request.form["tipo_vaga"]
        vaga.requisitos_vaga = request.form["requisitos_vaga"]
        vaga.perfil_candidato = request.form["perfil_candidato"]
        vaga.habilitacoes = request.form["habilitacoes"]
        vaga.provincia_vaga = request.form["provincia_vaga"]
        vaga.nivel_ingles_vaga = request.form["nivel_ingles_vaga"]
        vaga.habilidades_exigida = request.form["habilidades_exigida"]
        vaga.experiencia_profissional = request.form["experiencia_profissional"]
        vaga.anos_exp_exigida = request.form["anos_exp_exigida"]
        vaga.data_inicio_vaga = request.form["data_inicio_vaga"]
        vaga.data_termino_vaga = request.form["data_termino_vaga"] 
        db.session.commit()
        db.session.add(vaga)       
    except Exception as e:
        print(str(e))
        response = {'message':'Erro ao criar o candidato','result':vaga.id_vaga} 
    return jsonify(response)
   

#deleting a vaga
@vagas_blueprint.route('/delete/<id_vaga>', methods=['DELETE'])
def vaga_delete(id_vaga):
    try:
        vaga = Vagas.query.get(id_vaga)
        db.session.delete(vaga)
        db.session.commit()
        response ={'message':'Vaga eliminada com sucesso!','result':vaga.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message':'Vaga não existe.'}
    return jsonify(response)

#getting all vagas
@vagas_blueprint.route('/all', methods=['GET'])
def get_all_vagas():
    all_vagas = Vagas.query.all()
    result = [vaga.serialize() for vaga in all_vagas]
    response = {'message':'Returning all vagas','result': result}
    return jsonify(response)


#counting all vagas
@vagas_blueprint.route('/count_vagas', methods=['GET'])
def count_vagas():
    total_vagas = Vagas.query.count()
    response = {'message':'Returning all vagas','result': total_vagas}
    return jsonify(response)

#get an vaga by id
@vagas_blueprint.route('/<int:id_vaga>', methods=['GET'])
def vagas_id(id_vaga):
    vaga = Vagas.query.filter_by(id_vaga=id_vaga).first()
    if vaga:
        return jsonify({"result":vaga.serialize()}), 200
    return jsonify({"result":"Vaga não existe."}), 404

