import requests
from requests.auth import HTTPBasicAuth


# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

# Essa endpoint recebe um id, neste caso o ticketKey
ticket_key = 4479

anexo_key = 63

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/tickets/{}/anexos/{}".format(url_base, ticket_key, anexo_key)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
get = requests.get(ticket_url, auth=credentials, allow_redirects=True)

# Recuperamos o response como um objeto JSON
obj = get.request

anexo = '../../anexos/image.png'

open(anexo, 'wb').write(get.content)

