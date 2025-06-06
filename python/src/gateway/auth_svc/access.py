import os
import requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("Missing Credentials", 401)

    basic_auth = (auth.username, auth.password)

    try:
        response = requests.post(
            f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login",
            auth=basic_auth
        )
    except requests.exceptions.RequestException as e:
        return None, ("Auth service unavailable", 503)

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
