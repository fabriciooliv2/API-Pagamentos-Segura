from flask import Flask, request, jsonify

app = Flask(__name__)

# Simula a validação de pagamentos
@app.route('/api/pagamento', methods=['POST'])
def process_payment():
    data = request.json
    if not data.get("cartao") or not data.get("valor"):
        return jsonify({"erro": "Dados incompletos"}), 400

    # Simula sucesso no pagamento
    return jsonify({"mensagem": "Pagamento aprovado!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
