# devpdata-cli
CLI for development economics data integration in major data repositories.

This is the flagship command-line tool for data integration. It supports tasks like data fetching, harmonization, conversion, and more.

## Installation

Clone this repository and set up the environment:

```bash
git clone https://github.com/Melius-Imperio-LLC/devpdata-cli.git
cd devdata-cli
python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
pip install .
```

## Structure

devpdata-cli/                    # Root of the repository
├── .gitignore                   # Ignore files like venv, pycache, etc.
├── README.md                    # Project overview, installation, and usage instructions
├── setup.py                     # Setup script to make the package installable (pip install .)
├── requirements.txt             # List of required packages (e.g., click, pandas)
├── mkdocs.yml                   # MkDocs configuration file for your documentation site
├── docs/                        # Documentation folder (for MkDocs)
│   └── index.md                 # The homepage for the documentation
├── devdata/                    # The main Python package
│   ├── __init__.py              # Makes this folder a Python package
│   └── main.py                  # Contains the CLI entrypoint (e.g., click CLI with cli() function)
├── tests/                       # Folder for unit tests
│   └── test_sample.py           # A basic test file to ensure testing pipeline works
└── .github/                     # GitHub-specific configurations
    └── workflows/               # Folder for GitHub Actions workflows
         └── ci.yml              # The YAML file defining the CI pipeline (tests, build, etc.)

