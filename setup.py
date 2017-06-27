from setuptools import find_packages, setup

with open('ok/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip('\'"')
            break

requires = []

with open('requirements.txt', 'r') as f:
    for line in f.readlines():
        req = line.strip()
        if req:
            requires.append(req)

setup(
    name='ok',
    version=version,
    description='',
    long_description=open('README.rst', 'r').read(),
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/ok',
    download_url='https://github.com/ofek/ok',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',    ],

    install_requires=requires,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
