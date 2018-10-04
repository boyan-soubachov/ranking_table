from setuptools import setup, find_packages


REQUIRES = [
    'click',
]

TEST_REQUIRES = [
    'pytest'
]

with open('README.md', 'r', encoding='utf8') as file:
    long_desc = file.read()

setup(
    name='ranking_table',
    author='Boyan Soubachov',
    author_email='boyanvs@gmail.com',
    version='0.1.0',
    license='LICENSE.txt',
    packages=find_packages(exclude=['main.py']),
    python_requires='>= 3.0.0',
    description='A simple football ranking table calculator',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires=REQUIRES,
    extras_require={
        'testing': TEST_REQUIRES,
    },
    keywords=['football', 'ranking'],
    entry_points={
        'console_scripts': ['ranking_table=ranking_table.main:main']
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),

)
