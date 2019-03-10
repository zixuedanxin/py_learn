#!D:\django_demo\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cubes==1.0.1','console_scripts','slicer'
__requires__ = 'cubes==1.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cubes==1.0.1', 'console_scripts', 'slicer')()
    )
