import io
import zipfile

import requests

api_url = "https://api.github.com/repos/runfinch/finch/releases/latest"

response = requests.get(api_url)
data = response.json()

zip_file_url = data['zipball_url']

r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
namelist = z.namelist()

directory = namelist[0]

with open("../docs/docs/changelog.md", "wb") as f:
    f.write(z.read(directory + "CHANGELOG.md"))
    f.close()
