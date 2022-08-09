from flask import Flask,request,jsonify
app = Flask(__name__)

cancoes = [
    {
        'Musica':'Por do sol',
        'cantor':'Ludmila'
    },
    {
        'Musica':'Birds',
        'cantor':'Imagine Dragons'
    },
    {
        'Musica':'Amante não tem lar',
        'cantor':'Marilia Mendonça'
    },
    {
        'Musica':'Divisa de Fogo',
        'cantor':'Grupo Fogo no Pé'
    },
    {
        'Musica':'Proibida',
        'cantor':'Charlie Brown jr'
    }
]
#get
@app.route('/')
def obter_cancoes():
    return jsonify(cancoes)
#get id
@app.route('/cancoes/<int:indice>',methods=['GET'])
def obter_cancao_por_id(indice):
    return jsonify(cancoes[indice])
#POST
@app.route('/cancoes',methods=['POST'])
def criando_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)

    return jsonify(f'Sua canção foi adicionada com sucesso.',cancao,200)
#PUT
@app.route('/cancoes/<int:indice>',methods=['PUT'])
def alterando_cancao(indice):
    try:
        if cancoes[indice] is not None:
            cancao_alterada = request.get_json()
            cancoes[indice].update(cancao_alterada)

            return jsonify(f'Sua canção foi alterada.',cancao_alterada,200)
    except:
        return jsonify('Não foi possivel encontrar a canção que deseja altar',404)
#DELETE
@app.route('/cancoes/<int:indice>',methods=['DELETE'])
def excluido_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify('Sua canção foi excluida.',200)
    except:
        return jsonify('Não foi possivel encontrar a canção que deseja excluir',404)
    
app.run(port=5000,host='localhost',debug=True)