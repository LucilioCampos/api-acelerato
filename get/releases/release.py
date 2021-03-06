import requests
from requests.auth import HTTPBasicAuth

# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

release_key = 41

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/releases/{}".format(url_base, release_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
get = requests.get(ticket_url, auth=credentials)

# Recuperamos o response como um objeto JSON
obj = get.json()

# Print do response
print(obj)
