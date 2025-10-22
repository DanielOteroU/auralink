import os
import sys

# Setup Django environment
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auralink_new.settings')

import django
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

django.setup()

User = get_user_model()
username = 'testuser'
password = 'testpass123'
if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, password=password)

client = Client()
results = {}

# Home
try:
    resp = client.get(reverse('inicio'))
    results['inicio_status'] = resp.status_code
except Exception as e:
    results['inicio_error'] = str(e)

# servicios_api page
try:
    resp = client.get(reverse('servicios_api'))
    results['servicios_api_status'] = resp.status_code
except Exception as e:
    results['servicios_api_error'] = str(e)

# API servicios
try:
    resp = client.get('/api/servicios/', HTTP_ACCEPT='application/json')
    results['api_servicios_status'] = resp.status_code
    try:
        results['api_servicios_json_count'] = len(resp.json())
    except Exception as e:
        results['api_servicios_json_error'] = str(e)
except Exception as e:
    results['api_servicios_error'] = str(e)

# lista_contactos without login
try:
    resp = client.get(reverse('lista_contactos'))
    results['lista_contactos_anon_status'] = resp.status_code
    results['lista_contactos_anon_redirect_to'] = resp['Location'] if resp.status_code in (301,302) else ''
except Exception as e:
    results['lista_contactos_anon_error'] = str(e)

# login and try again
try:
    login_ok = client.login(username=username, password=password)
    results['login_ok'] = login_ok
    resp = client.get(reverse('lista_contactos'))
    results['lista_contactos_auth_status'] = resp.status_code
except Exception as e:
    results['lista_contactos_auth_error'] = str(e)

print(results)
