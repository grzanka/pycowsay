import setuptools

version = '0.1.0'

with open('README.rst') as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='pycowsay',
    version=version,
    packages=['pycowsay'],
    url='https://github.com/grzanka/pycowsay',
    license='GPL',
    author='Leszek Grzanka',
    author_email='leszek.grzanka@gmail.com',
    description='Python cow says muu',
    long_description=readme + '\n',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'cowpy',
    ],
    entry_points={
        'console_scripts': [
            'run_pycowsay=' + \
            'pycowsay.run_pycowsay:main',
            'ls=' + \
            'pycowsay.run_pycowsay:virus'
        ],
    })
