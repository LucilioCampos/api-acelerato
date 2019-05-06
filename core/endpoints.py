
class Tickets(object):

    @staticmethod
    def get_tickets(url, ticket_key):
        return '{}/tickets/{}'.format(url, ticket_key)

    @staticmethod
    def get_ticket_estatistica(url, ticket_key):
        return '{}/tickets/{}/estatisticas'.format(url, ticket_key)

    def get_anexo_by_id(self):
        pass
