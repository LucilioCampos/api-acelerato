import requests
from requests.auth import HTTPBasicAuth

# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

release_key = 41


# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/releases{}".format(url_base, release_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui inserimos o body da requisição
payload = {
    "dataFinal": "24/12/2019",
    "dataInicial": "24/05/2019",
    "nome": "API Releses Create",
    "projetos": [
        2
    ],
    "releaseNotes": True
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
