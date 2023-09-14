import json
import requests

BASE_URL = 'https://api.bws.xyz'


def account_login(email, password):
    url = f'{BASE_URL}/account/login'
    payload = json.dumps({
        'email': email,
        'password': password
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(
            url,
            headers=headers,
            data=payload
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise RuntimeError(f'Login request failed: {e}')


def stop_vm(access_token, vm_id):
    url = f'{BASE_URL}/vm/stop/{vm_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    try:
        response = requests.post(
            url,
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'Stopping instance failed: {e}')


def start_vm(access_token, vm_id):
    url = f'{BASE_URL}/vm/start/{vm_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    try:
        response = requests.post(
            url,
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'Stopping instance failed: {e}')
