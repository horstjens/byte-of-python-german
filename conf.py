# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [#"myst_parser",           # markdown files. remove if you use myst_nb 
              "myst_nb",               # jupyter notebooks
              "sphinx_design",         
              'sphinx_togglebutton',
              'sphinxcontrib.mermaid', # mermaid diagrams
              ]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_fence_as_directive = ["mermaid"]
myst_heading_anchors = 2 

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', ".venv"]


language = 'de'
project = 'A byte of Python deutsch'
#copyright = '2026 Horst JENS. Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.de">CC-By-SA 4.0 Creative Commons Nammensnennung Share-Alike 4.0 international</a>'
author = '<a href="https://spielend-programmieren.at/">Horst JENS</a> übersetzt. Englische Originalausgabe von <a href="https://www.swaroopch.com/contact">Swaroop CH</a>.' 
release = '2026'
html_logo = "./img/byte_of_python_a_200.png"
html_favicon = "./img/snake_bitten16.png"
html_show_sphinx = True
html_search_language = "de"
html_title = "Byte of Python deutsch"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']


#html_logo = "_static/logo-wide.svg"
#html_favicon = "_static/logo-square.svg"

## see https://sphinx-book-theme.readthedocs.io
html_theme_options = {
    #"rightsidebar": False,
    #  "relbarbgcolor": "black"
    "home_page_in_toc": True,
    # "github_url": "https://github.com/executablebooks/MyST-Parser",
    "repository_url": "https://github.com/horstjens/byte-of-python-german",
    "repository_branch": "master",
    #"path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    # "announcement": "<b>v3.0.0</b> is now out! See the Changelog for details",
    "use_sidenotes": True,
    #"navbar_end": ["mybutton.html"],
    "extra_footer": 'Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.de">Creative Commons CC-By-Sa 4.0 <img src="_static/cc-by-sa25.png"></a>',

}

source_suffix = {
    #".md":"markdown",    # outcomment this line if you use myst-db
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',

}

