import requests


def url_get(url, auth=None, headers=None, id=None):
    if id and isinstance(id, int):
        get_url = '{}/{}'.format(url, id)
    else:
        get_url = '{}'.format(url)

    return get_url


def verify_credentials(credentials):

    pass
