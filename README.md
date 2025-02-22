# JSON Corrector

Takes data, that is almost in json format, and converts it to json data. <br>
Thus prepare the data for a json parser.

# Requirements

* Python 3.x >= 3.8

# Install (Windows & Linux)

```bash
pip install json-corrector
```

# Use (Windows & Linux)
Using entry point script
```bash
echo "{'key1':'val1',key2: val2, 'key3': val3,key4: 'val4', key5: {  'key6': val6  },key7: 'val7: val7,val7'}" | jc
jc "{'key1':'val1',key2: val2, 'key3': val3,key4: 'val4', key5: {  'key6': val6  },key7: 'val7: val7,val7'}"
```
Using runpy
```bash
echo "{'key1':'val1',key2: val2, 'key3': val3,key4: 'val4', key5: {  'key6': val6  },key7: 'val7: val7,val7'}" | py -m json_corrector.jc
py -m json_corrector.jc "{'key1':'val1',key2: val2, 'key3': val3,key4: 'val4', key5: {  'key6': val6  },key7: 'val7: val7,val7'}"
```

# Build
**Firstly increase the version in `pyproject.toml`.**
## Windows
Checkout repo
```pwsh
git clone https://github.com/tschenkelz/json_corrector.git
cd json_corrector
```

*Optional Cleanup*
```pwsh
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .\dist\*
```

*Optional Specify CA certs*
```pwsh
$Env:REQUESTS_CA_BUNDLE  = "path\to\ca.pem"
```

Build & upload
```pwsh
py -m pip install --upgrade pip
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade twine
twine upload dist/*
```