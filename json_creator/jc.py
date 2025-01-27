"""
Fixes data that is almost json but not enterily. This issues are fixed:
  - single quotes are changed to double quotes
  - booleans gets quoted

Compliant json gets printed.
"""

import re


import json
import argparse

class MultipleArgumentError(Exception):
    """Raise when multiple Arguments detected but only one is expected
    This could be due to powershell version 5 or prior. Use PowerShell Core instead.
    """
    pass


def transform_json(almost_json: str) -> str:
    #regex = r'([^\w"]+(?:"[^"]*"[^\w"]*)*)([^"\W]+)'
    regex = r'([^\w"]+(?:"[^"]*"[^\w"]*)*)(?:True|true|False|false)?([^"\W]+)?'
    repl = r'\1"\2"'

    return re.sub(regex,repl,almost_json)

def main():
    parser = argparse.ArgumentParser(description=("Fixes data that is almost json"
                                                  " but not enterily."),
                                                  epilog="Compliant json gets printed.")
     # nargs = '*': powershell5 and prior cannot pass data like
     # '{"hello": "my-friend", "hello2": "my friend"}'
     # as one argument. This will be split into two arguments
     # 1. 'hello: my-friend, hello2: my'
     # 2. 'friend'}
     # To avoid program crash with missleading error, I will catch it this way.
    parser.add_argument('almost_json', help=("Data thats almost in json format,"
                                            " but not enterily."
                                            " E.g. double quotes instead of single quotes"),
                                            nargs='*')
    args = parser.parse_args()
    almost_json = args.almost_json

    # fail if on powershell 5 and prior
    if len(almost_json) > 1:
        raise MultipleArgumentError(("Multiple Arguments detected. This could be due to"
                                     " PowerShell version 5 or prior."
                                     " Use PowerShell core instead."))

    
    compliant_json = transform_json(almost_json[0])

    loaded = json.loads(compliant_json)
    print(json.dumps(loaded))

main()