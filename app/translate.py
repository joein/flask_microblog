import json
import requests

from flask import current_app
from flask_babel import _



def translate(text, source_language, dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is  not configured.')
    r = requests.post(current_app.config['YA_TRANSLATOR_URL'].substitute(key=current_app.config['YA_TRANSLATOR_KEY'], text=text,
                                                                 lang=f"{source_language}-{dest_language}"))
    if r.status_code != requests.status_codes.codes.ok:
        return _('Error: the translation service failed.')
    return json.loads(r.text)
