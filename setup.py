from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class CustomInstallCommand(install):
    def run(self):
        # Run npm install playwright
        try:
            print("Running `npm install playwright`...")
            subprocess.check_call(['npm', 'install', 'playwright'], cwd=os.path.dirname(__file__))
        except Exception as e:
            print("Warning: npm install playwright failed:", e)
        install.run(self)

setup(
    name='openlibrary-harvest',
    version='0.1.0',
    packages=find_packages(include=['genre_harvest', 'genre_harvest.*']),
    install_requires=[
        'tqdm',
    ],
    include_package_data=True,
    package_data={'': ['scrape_openlibrary.js']},
    author='Khalifatur Rauf',
    author_email='blograuf.kr@gmail.com',
    description='Scrape genres from OpenLibrary using Playwright via Node.js',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/motoroko/openlibrary-harvest',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
