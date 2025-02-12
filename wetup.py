from setuptools import setup
import sys

print("Detected OS:", sys.platform)  # Debugging line

setup_kwargs = {}

if sys.platform.startswith("linux"):
    print("Adding entry point...")  # Debugging line
    setup_kwargs["entry_points"] = {
        "console_scripts": [
            "my_script = my_module.cli:main"
        ]
    }

setup(**setup_kwargs)