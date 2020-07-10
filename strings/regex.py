import re


padrao = "[0-9]{4,5}-?[0-9]{4}"
texto = "Meu numero para contato é 2633-5723"
retorno = re.search(padrao, texto)
print(retorno.group())
