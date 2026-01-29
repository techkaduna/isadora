import os
import sys
from pathlib import Path

# --- Paths -------------------------------------------------

DOCS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = DOCS_DIR.parent
PACKAGE_DIR = PROJECT_ROOT / "isadora"

sys.path.insert(0, str(PACKAGE_DIR))

# -- Project information -----------------------------------

project = "isadora"
author = "Kolawole Andrew"
copyright = "2026, Kolawole Andrew"
release = "1.2.0"

# -- General configuration ---------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "autoapi.extension",
]

# -- Autodoc -----------------------------------------------

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "inherited-members": True,
}
autodoc_inherit_docstrings = True

autosummary_generate = True

# -- AutoAPI (CRITICAL FIX) --------------------------------

autoapi_type = "python"
autoapi_dirs = [str(PACKAGE_DIR)]   # ABSOLUTE PATH
autoapi_root = "api"
autoapi_add_toctree_entry = True
autoapi_keep_files = True
autoapi_generate_api_docs = True

# -- Napoleon ----------------------------------------------

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# -- Templates ---------------------------------------------

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML --------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}
html_static_path = ["_static"]
html_logo = "_static/isadora.svg"

def setup(app):
    app.add_css_file("custom.css")
