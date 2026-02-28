from flask import Flask, request, render_template
from backend.operators import add, subtract, multiply, divide

# Application Flask principale pour la calculatrice

app = Flask(__name__)

# Dictionnaire des opérateurs disponibles
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule le résultat d'une expression simple avec un seul opérateur.
    Args:
        expr (str): Expression à calculer (ex: "2+3")
    Returns:
        float: Résultat du calcul
    Raises:
        ValueError: Si l'expression est vide, mal formée ou contient plusieurs opérateurs.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")  # Supprime les espaces

    # Permettre les parenthèses autour de l'expression entière
    if s.startswith('(') and s.endswith(')'):
        s = s[1:-1]

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur en commençant à l'indice 1 pour ignorer le signe
    # éventuel du premier opérande, et en ignorant les signes qui suivent un opérateur
    # (signe du second opérande, ex: 5*-2)
    for i in range(1, len(s)):
        ch = s[i]
        if ch in OPS:
            if s[i - 1] in OPS and ch == '-':
                continue  # Signe négatif du second opérande, pas un opérateur
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L'opérateur ne doit pas être au début ou à la fin
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Appel de la fonction correspondant à l'opérateur
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.
    Affiche la page de la calculatrice et traite les requêtes POST pour effectuer le calcul.
    Returns:
        Template HTML rendu avec le résultat.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Démarre le serveur Flask en mode debug
    app.run(debug=True)