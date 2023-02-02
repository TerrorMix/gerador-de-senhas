import random
import string

def gerar_senha(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    senha_usuario = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        senha_usuario = senha_usuario + digit

    return senha_usuario

escolha_usuario = input("Quantos dígitos na senha?")
if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)
else:
    print("Entrada inválida!")
    quit()

response = gerar_senha(len_pass = escolha_usuario)
print(f"Senha gerada:\n{response}")


