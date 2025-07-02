import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

project = 'Turtles'
copyright = '2025, Luqi Xu'
author = 'Luqi Xu'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_conestack_theme'  # <<✅ this replaces RTD theme
html_static_path = ['_static']
