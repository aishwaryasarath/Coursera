import requests
response = requests.get("https://www.google.com")
print(response.text[:300])


response2 = requests.get('https://www.google.com', stream=True)
print(response2.raw.read()[:100])

print(response.request.headers['Accept-Encoding'])
print(response.headers['Content-Encoding'])

print(response.ok)
print(response.status_code)

if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

# the above can also be done by
print(response.raise_for_status())
