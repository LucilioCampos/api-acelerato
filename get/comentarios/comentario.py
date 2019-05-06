import requests
from requests.auth import HTTPBasicAuth


# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

ticket_key = 4479

ticket_comentario_key = 337

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/tickets/{}/comentarios/{}".format(url_base, ticket_key, ticket_comentario_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
get = requests.get(ticket_url, auth=credentials)

# Recuperamos o response como um objeto JSON
obj = get.json()

# Print do response
print(obj)
