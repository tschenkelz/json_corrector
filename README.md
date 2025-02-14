# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

# Install

## Windows
```pwsh
py -m pip install json-corrector
```

# Use
```pwsh
echo "{'key1':'val1',key2: val2, 'key3': val3,key4: 'val4', key5: {  'key6': val6  },key7: 'val7: val7,val7'}" | jc
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