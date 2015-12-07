import argparse
import sys

import secrets

def main(args):
    parser = argparse.ArgumentParser("Secrets command line interface")
    parser.add_argument("command", choices=["dump", "list", "store", "show"])
    options, args = parser.parse_known_args(args)

    if options.command == "dump":
        secrets.dumpSecrets()
    elif options.command == "list":
        secrets.listScopes()
    elif options.command == "store":
        secrest.storeSecret(*args)
    elif options.command == "show":
        if len(args) > 1:
            secrets.getSecret(*args)
        if len(args) == 1:
            secrets.dumpScope(*args)
    elif options.command == "clear":
        secrets.removeAllSecrets()

if __name__=="__main__":
    main(sys.argv[1:])
