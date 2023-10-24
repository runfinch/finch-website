import io
import zipfile

import requests

# Temporarily use main to generate docs, switch to latest release after next release
api_url = "https://github.com/runfinch/finch/archive/refs/heads/main.zip"
# api_url = "https://api.github.com/repos/runfinch/finch/releases/latest"

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

for file_name in namelist:
    doc_file_prefix = namelist[0] + "docs/cmd/"
    if file_name.startswith(doc_file_prefix) and file_name[-1] != '/':
        rest = file_name.split(doc_file_prefix)[1]
        with open(f"../docs/docs/cli-reference/{rest}", "wb") as f:
            f.write(z.read(file_name))
            f.close()
