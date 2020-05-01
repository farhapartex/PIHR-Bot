#!/usr/bin/env python
import os, sys

BASE_DIR = os.getcwd()

def main():
    try:
        from setting import settings
    except ImportError as exc:
        raise ImportError(
            "Couldn't import settings."
            "Did you forget to activate a virtual environment?"
        ) from exc
    
    settings.check_args(sys.argv)


if __name__ == "__main__":
    main()