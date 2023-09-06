import json
import datetime

import pytz
import requests


current_datetime = datetime.datetime.now(pytz.timezone('Asia/Almaty')).isoformat('T')

url = 'http://loki:3100/api/prom/push'
payload = {
    'streams': [
        {
            'labels': '{source=\"Name-of-your-source\",job=\"name-of-your-job\", host=\"host_name\"}',
            'entries': [
                {
                    'ts': current_datetime,
                    'line': f'[WARN] On server host_name detected error',
                }
            ]
        }
    ]
}

payload = json.dumps(payload)
response = requests.post(
    url,
    data=payload,
    headers={
        'Content-type': 'application/json',
    }
)

print(response)
