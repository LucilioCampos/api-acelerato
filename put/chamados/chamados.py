import requests
from requests.auth import HTTPBasicAuth


# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

ticket_key = 4479

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/chamados/{}".format(url_base, ticket_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui inserimos o body da requisição
payload = {

    "titulo": "Metodo PUT chamados",
    "descricao": "<p>Editando um chamado via <span>PUT</span></p>",
    "lixeira": "false",
}

# Necessário informar o content-type como JSON
headers = {
    "Accept": "application/JSON",
    "Content-Type": "application/JSON",
}
# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais os headers e o data
response = requests.put(ticket_url, auth=credentials,  headers=headers, json=payload)

print(response.status_code, response.headers, requests.Response)

response.raise_for_status()

# Recuperamos o response como um objeto JSON
# obj = response.json()

# Print do response
# print(obj)
