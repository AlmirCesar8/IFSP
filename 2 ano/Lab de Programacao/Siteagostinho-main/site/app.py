from flask import Flask, render_template, jsonify

app = Flask(__name__)
noticias = [
    {
        "id": 1,
        "titulo": "Novas descobertas sobre os benefícios da meditação",
        "resumo": "Estudos recentes indicam que a prática regular de meditação pode reduzir significativamente os níveis de estresse, melhorar a concentração e promover um equilíbrio emocional mais estável. Pesquisadores destacam que a meditação também pode ajudar na prevenção de doenças cardiovasculares e no fortalecimento do sistema imunológico.",
        "categoria": "Saúde"
    },
    {
        "id": 2,
        "titulo": "Alimentação saudável: dicas para uma vida mais equilibrada",
        "resumo": "Especialistas em nutrição recomendam a adoção de uma dieta rica em frutas, verduras, grãos integrais e proteínas magras para melhorar a qualidade de vida. Além disso, a redução do consumo de alimentos processados e açúcares refinados pode prevenir doenças crônicas como diabetes e hipertensão, promovendo maior longevidade e bem-estar geral.",
        "categoria": "Saúde"
    },
    {
        "id": 3,
        "titulo": "Importância do sono para a saúde mental e física",
        "resumo": "Dormir bem é fundamental para o funcionamento adequado do organismo. Pesquisas mostram que a privação de sono está associada a problemas como ansiedade, depressão, obesidade e comprometimento do sistema imunológico. Técnicas para melhorar a qualidade do sono incluem manter uma rotina regular, evitar o uso de eletrônicos antes de dormir e criar um ambiente tranquilo no quarto.",
        "categoria": "Bem-Estar"
    },
    {
        "id": 4,
        "titulo": "Exercícios físicos e seus impactos positivos no corpo e mente",
        "resumo": "A prática regular de atividades físicas contribui para a melhora da saúde cardiovascular, fortalecimento muscular e controle do peso corporal. Além dos benefícios físicos, o exercício libera endorfinas, que promovem sensação de bem-estar e ajudam no combate à ansiedade e depressão. Profissionais recomendam pelo menos 150 minutos de atividade moderada por semana.",
        "categoria": "Bem-Estar"
    },
    {
        "id": 5,
        "titulo": "Terapias alternativas ganham espaço no cuidado com a saúde",
        "resumo": "Cada vez mais pessoas buscam terapias como acupuntura, aromaterapia e yoga para complementar tratamentos tradicionais. Essas práticas auxiliam no alívio de dores crônicas, redução do estresse e melhora da qualidade de vida. Especialistas ressaltam a importância de integrar essas terapias com acompanhamento médico para resultados mais eficazes.",
        "categoria": "Saúde"
    }
]

@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/contato')
def contatos():
    return render_template('contato.html')
@app.route('/noticias')
def noticiar():
    return render_template('noticia.html', noticias=noticias)
@app.route('/api/noticias')
def retornar():
    return jsonify(noticias)
if __name__ == '__main__':
    app.run(debug=True)
