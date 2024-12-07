import random

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
  """
  Gera uma senha aleatória com as opções de personalização.

  Args:
    tamanho: O tamanho desejado da senha.
    incluir_maiusculas: Se True, inclui letras maiúsculas na senha.
    incluir_minusculas: Se True, inclui letras minúsculas na senha.
    incluir_numeros: Se True, inclui números na senha.
    incluir_simbolos: Se True, inclui símbolos na senha.

  Returns:
    Uma string contendo a senha gerada.
  """

  caracteres = ""
  if incluir_maiusculas:
    caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if incluir_minusculas:
    caracteres += "abcdefghijklmnopqrstuvwxyz"
  if incluir_numeros:
    caracteres += "0123456789"
  if incluir_simbolos:
    caracteres += "!@#$%^&*()_+-={}[]|;':\",./<>?"

  senha = "".join(random.choice(caracteres) for i in range(tamanho))
  return senha

def menu():
  """
  Exibe o menu de opções para o usuário.
  """
  print("-" * 30)
  print("Gerador de Senhas")
  print("-" * 30)
  print("1. Gerar Senha")
  print("2. Sair")

while True:
  menu()
  opcao = input("Digite a opção desejada: ")

  if opcao == "1":
    tamanho = int(input("Digite o tamanho desejado da senha: "))
    maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == "s"
    minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == "s"
    numeros = input("Incluir números? (s/n): ").lower() == "s"
    simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)
    print("Senha gerada:", senha)
  elif opcao == "2":
    break
  else:
    print("Opção inválida!")