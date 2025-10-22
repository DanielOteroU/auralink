import os, sys
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','auralink_new.settings')
import django
django.setup()
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()
username='testuser'
password='testpass123'
client=Client()
print('login:', client.login(username=username,password=password))
resp = client.post('/accounts/logout/')
print('logout status:', resp.status_code)
print('logout redirected to:', resp['Location'] if resp.status_code in (301,302) else '')
