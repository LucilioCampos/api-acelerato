import requests
from requests.auth import HTTPBasicAuth

# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/chamados".format(url_base)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui inserimos o body da requisição
payload = {
    "titulo": "Abertura de chamado",
    "descricao": "Utilizando a lib requests para realizar requisições http",
    "lixeira": "false",
    "organizacao": {"organizacaoKey": 1},
    "solicitantes": [{"usuarioKey": 10}],
    "agente": {"usuarioKey": 1},
    "categoria": {"categoriaKey": 1},
    "tipoDeTicket": {"tipoDeTicketKey": 1},
    "kanbanStatus": {"kanbanStatusKey": 3},
    "equipe" : {"equipeKey": 2},
    "tipoDePrioridade": {"tipoDePrioridadeKey": 1}
}

# Necessário informar o content-type como JSON
headers = {
    "Accept": "application/JSON",
    "Content-Type": "application/JSON",
}
# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
response = requests.post(ticket_url, auth=credentials,  headers=headers, json=payload)

print(response.status_code, response.headers)

response.raise_for_status()

# Recuperamos o response como um objeto JSON
# obj = response.json()

# Print do response
# print(obj)
