from setuptools import setup, find_packages

setup(
    #name='openlibrary_harvest',
    name='openlibrary-harvest',
    version='0.1.0',
    #packages=find_packages(where="openlibrary_harvest"),  # Menggunakan find_packages() untuk mencari modul
    packages=find_packages(include=['genre-harvest', 'genre-harvest.*']),
    install_requires=[
        'tqdm',
    ],
    include_package_data=True,
    package_data={'': ['scrape_openlibrary.js']},  # Pastikan file js dimasukkan jika diperlukan
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
)
