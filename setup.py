from setuptools import setup

setup(
    name='southwest-headers',
    version='1.0',
    packages=['southwest_headers'],
    url='https://github.com/nicolaskenner/southwest-headers',
    license='',
    author='nicolaskenner',
    author_email='nick@picnicpeaks.com',
    description='Southwest Headers',
    install_requires=['async-generator==1.10', 'attrs==21.2.0', 'blinker==1.4', 'Brotli==1.0.9', 'certifi==2021.10.8',
                      'cffi==1.15.0', 'cryptography==36.0.0', 'h11==0.12.0', 'h2==4.1.0', 'hpack==4.0.0',
                      'hyperframe==6.0.1', 'idna==3.3', 'kaitaistruct==0.9', 'outcome==1.1.0', 'pyasn1==0.4.8',
                      'pycparser==2.21', 'pyOpenSSL==21.0.0', 'pyparsing==3.0.6', 'PySocks==1.7.1', 'selenium==4.1.0',
                      'selenium-wire==4.5.6', 'six==1.16.0', 'sniffio==1.2.0', 'sortedcontainers==2.4.0',
                      'trio==0.19.0', 'trio-websocket==0.9.2', 'urllib3==1.26.7', 'wsproto==1.0.0', 'zstandard==0.16.0']

)
