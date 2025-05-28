from setuptools import setup, find_packages

setup(
    name='devdata-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'devdata=devdata.main:cli',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Flagship CLI for data integration",
    url="https://github.com/Melius-Imperio-LLC/devpdata-cli",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
