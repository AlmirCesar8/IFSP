from flask import Flask, render_template, abort, request, flash, redirect, url_for

app = Flask(__name__)

#Rota principal

@app.route("/")
def index():
    return render_template("index.html")

#Erro 401 forcado

@app.route("/area-restrita")
def area_restrita():
    #Em aplicação real é feita a verificação de se o usuario esta logado
    #Como não temos sistema de login, iremos forçar o erro com abort()
    print("Tentativa de acesso à area restrita sem autenticação")
    abort(401)  

#Para demonstrar o erro 403, uma rota de admin (simulado)

@app.route("/painel-admin")
def painel_admin():
    #Aqui, voce verificaria se o usuario logado é um adm
    #Vamos simular que o usuario não é admin e forçar o erro 403

    print("Tentativa de acesso ao painel de admin sem permissão")
    abort(403)

#-------- Manipuladores de Erro (Error Handlers) --------

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    #A função recebe o objeto de erro como argumento.
    #Retornamos a renderização do nosso template e o codigo de status 404
    return render_template("404.html"), 404

@app.errorhandler(401)
def nao_autorizada(error):
    return render_template("401.html"), 401

@app.errorhandler(403)
def acesso_proibido(error):
    return render_template("403.html"), 403

app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'

@app.route('/formulario', methods = ['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        #Em uma aplicação real, aqui ocorreria a validação no back-end

        nome = request.form.get('nome')
        email = request.form.get('email')
        print(f"Dados recebidos do formulario: Nome = {nome}, Email = {email}")

        #Simula uma mensagem de sucesso

        flash(f"Obrigado por se cadastrar, {nome}!", "success")
        return redirect(url_for('formulario'))
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)