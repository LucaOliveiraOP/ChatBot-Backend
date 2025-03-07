from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

options = {
    1: 'Acesso',
    2: 'Pagamento',
    3: 'Dúvidas',
    4: 'Reclamações',
    5: 'Sugestões',
    6: 'Outros'
}
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    response = ""
    if user_message:
        user_message = user_message.lower()

        if user_message.isdigit():
            option_number = int(user_message)
            if option_number in options:
                response = process_option(options[option_number])
            else:
                response = "Opção inválida. Por favor, escolha uma opção válida."
        else:
            if user_message in [option.lower() for option in options.values()]:
                response = process_option(user_message.capitalize())
            else:
                response = "Opção inválida. Por favor, escolha uma opção válida."

    else:
        response = "Mensagem não recebida corretamente."

    return jsonify({'response': response})

def process_option(option):
    if option == 'Acesso':
        return "Posso ajudar você com problemas de acesso. Qual é a sua dúvida?"
    elif option == 'Pagamento':
        return "Você está enfrentando problemas com pagamento? Como posso te ajudar?"
    elif option == 'Dúvidas':
        return "Quais são as suas dúvidas sobre a plataforma?"
    elif option == 'Reclamações':
        return "Desculpe por qualquer inconveniente. O que você gostaria de reclamar?"
    elif option == 'Sugestões':
        return "Agradecemos suas sugestões! O que você gostaria de sugerir?"
    elif option == 'Outros':
        return "Gostaria de falar com um atendente humano?"
    else:
        return "Desculpe, não entendi. Pode reformular?"

if __name__ == '__main__':
    app.run(debug=True)
