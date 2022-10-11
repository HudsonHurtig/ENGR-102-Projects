import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'Joe Biden Shaking hands with Putin',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())