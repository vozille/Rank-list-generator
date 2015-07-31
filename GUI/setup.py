# requires py2exe
# run as python setup.py py2exe

from distutils.core import setup
import py2exe

setup(
    windows = [{'script': "rankGenUI.py"}],
    options = {
        'py2exe':
            {
                'includes':['lxml.etree','lxml._elementpath','gzip'],
            }
    }
)
