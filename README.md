# Finch Website

This repository is the source to the runfinch project website.

The documentation is written in markdown files, and is hosted by
[mkdocs](https://www.mkdocs.org/) with the [Material
theme](https://squidfunk.github.io/mkdocs-material/).

## Development

The Finch website can be built and ran locally in containers with Finch, using
the included Compose file:

```bash
git clone https://github.com/runfinch/website.git
finch compose up
```

To run the Finch website locally (not within a container) you can also use
python [virtual
environments](https://docs.python.org/3/library/venv.html#module-venv) and pip
to install mkdocs.

```bash
# Create a python virtual environment
python3 -m venv .env

# Source the virtual environment
source ./.env/bin/activate

# Install mkdocs
pip install -r requirements.txt

# Run mkdocs
mkdocs serve
```

You should now be able to browse to mkdocs on http://localhost:8000. To
customize the IP address and port, you can pass the flag `--dev-addr` into the
`mkdocs serve` command.

## License Summary

Site templates, source code, and stylesheets are made available under the Apache
2.0 license. See the LICENSE file.

The content and documentation is made available under the Creative Commons
Attribution-ShareAlike 4.0 International License. See the LICENSE-CONTENT file.
The sample code within this documentation is made available under a modified
MIT-0 license. See the LICENSE-SAMPLECODE file.