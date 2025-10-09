import re

def verificar_senha(senha):
    # Regras de segurança
    comprimento = len(senha) >= 8
    tem_maiuscula = re.search(r"[A-Z]", senha)
    tem_minuscula = re.search(r"[a-z]", senha)
    tem_numero = re.search(r"[0-9]", senha)
    tem_especial = re.search(r"[@$!%*?&]", senha)

    pontuacao = sum([
        bool(comprimento),
        bool(tem_maiuscula),
        bool(tem_minuscula),
        bool(tem_numero),
        bool(tem_especial)
    ])

    if pontuacao == 5:
        return "Senha forte 💪"
    elif 3 <= pontuacao < 5:
        return "Senha média ⚠️"
    else:
        return "Senha fraca ❌"

def dicas_senha():
    print("\n💡 Dicas para criar senhas seguras:")
    print("- Use pelo menos 8 caracteres")
    print("- Misture letras maiúsculas e minúsculas")
    print("- Inclua números e símbolos (@, $, %, &...)")
    print("- Evite usar datas de nascimento ou nomes pessoais\n")

if __name__ == "__main__":
    print("🔐 Verificador de Senhas Seguras 🔐")
    senha = input("Digite uma senha para verificar: ")
    resultado = verificar_senha(senha)
    print(f"\nResultado: {resultado}")
    dicas_senha()
