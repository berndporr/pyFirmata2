# -- Path setup ----------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -------------------------------
project = 'pyFirmata2'
copyright = '2010, Tino de Bruijn & 2018-2020, Bernd Porr'
author = 'Bernd Porr'

# -- General configuration -----------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------
html_theme = 'alabaster'
