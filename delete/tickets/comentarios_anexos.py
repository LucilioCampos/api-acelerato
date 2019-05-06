import requests
from requests.auth import HTTPBasicAuth


# Aqui é necessário informar o endereço de acesso ao portal
# EX: https://atendimento.acelerato.com
url_base = '{ endereço acelerato }/api/publica'

# Essa endpoint tras informações estatisticas  de um ticket especifico
ticket_key = 4479

ticket_comenatario_key = 341

anexo_key = 58

# Aqui é uma endpoint, utilizamos aqui o exemplo de chamado
ticket_url = "{}/tickets/{}/comentarios/{}/anexos/{}".format(
    url_base,
    ticket_key,
    ticket_comenatario_key,
    anexo_key
)

# Credenciais é composta por e-mail e token
credentials = HTTPBasicAuth("email", "token")

# Aqui instaciamos a lib request, utilizando o metodo GET, passando
# Como parametro a url da API e as credenciais
get = requests.delete(ticket_url, auth=credentials)
