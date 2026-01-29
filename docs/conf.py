# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "isadora"))
)

# -- Project information -----------------------------------------------------
project = "isadora"
author = "Kolawole Andrew"
copyright = "2026, Kolawole Andrew"
release = "1.2.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "autoapi.extension",
]

# -- Autodoc settings --------------------------------------------------------
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "show-inheritance": True,
    "inherited-members": True,
}
autodoc_inherit_docstrings = True

# -- Autosummary settings ----------------------------------------------------
autosummary_generate = True

# -- AutoAPI settings --------------------------------------------------------
autoapi_type = "python"
# AutoAPI directory
autoapi_dirs = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "isadora"))
]
autoapi_add_toctree_entry = True
autoapi_keep_files = True
autoapi_generate_api_docs = True

# -- Napoleon settings (NumPy style docstrings) ------------------------------
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_use_admonition_for_note = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Templates and exclude patterns ------------------------------------------
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output settings ----------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}
html_static_path = ["_static"]

# Add custom CSS
def setup(app):
    app.add_css_file("custom.css")

html_logo = "_static/isadora.svg"

latex_engine = "pdflatex"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "preamble": r"""
    \usepackage{amsmath}
    \usepackage{amssymb}
    \setcounter{tocdepth}{2}
    """,
}

latex_documents = [
    (
        "index",
        "isadora.tex",
        "isadora Documentation",
        "Kolawole Andrew",
        "manual",
    ),
]
