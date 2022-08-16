# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ELEC380-NEUR383 Intro To Neuroengineering'
copyright = '2022, Caleb Kemere'
author = 'Caleb Kemere'
version = '2022'
# release = '2022'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxdoc'
# html_theme = 'alabaster'
# html_theme = 'nature'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_sidebars = {'**':['globaltoc.html','searchbox.html']}
