import requests
from requests.auth import HTTPBasicAuth


# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

# Essa endpoint recebe um id, neste caso o ticketKey
equipe_key = 1

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/users-current-task?equipeKey={}".format(url_base, equipe_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("emailr", "token")

# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
get = requests.get(ticket_url, auth=credentials)

# Recuperamos o response como um objeto JSON
obj = get.json()

# Print do response
print(obj)
