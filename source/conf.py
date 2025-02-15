# -*- coding: utf-8 -*-
#
# Tango Controls Documentation documentation build configuration file, created by
# sphinx-quickstart on Sat Aug  6 21:40:12 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# import breathe
import IPython.sphinxext

sys.path.append(os.path.abspath('.'))
# sys.path.append( "/home/tango/workspace/breathe")

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'breathe',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.intersphinx',
    'tangocontrib.metalabels',
#    'sphinx.ext.autosectionlabel',
]

# breathe_projects = { "cppTango": "cpp-api/xml" }

# breathe_default_project = "cppTango"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'Tango Controls'
copyright = u'2017-2019, Tango Community, Creative Commons Attribution 4.0 International (CC BY 4.0)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '9.3'
# The full version, including alpha/beta/rc tags.
release = '9.3.3'

# rst_epilog is added at the end of each rst file. Here it will contain typical substitutions
rst_epilog = """

.. _`OMG home page`: http://www.omg.org

.. _`TANGO home page`: http://www.tango-controls.org

.. _`TANGO web site`: `Tango home page`_

.. _`Tango web`: `Tango home page`_

.. _`Tango webpage`: `Tango home page`_

.. _`Tango Controls web page`: `Tango home page`_

.. _`ALBA home page`: http://www.cells.es

.. _`Soleil home page`: http://www.synchrotron-soleil.fr

.. _`Elettra home page`: http://www.elettra.trieste.it

.. _`MySQL home page`: http://www.mysql.com

.. _`Tango classes on-line documentation`: http://www.tango-controls.org/developers/dsc

.. _`omniORB home page`: http://omniorb.sourceforge.net

.. _`CVS WEB page`: http://www.cyclic.com

.. _`POGO home page`: http://www.esrf.eu/computing/cs/tango/tango_doc/tools_doc/pogo_doc/index.html

.. _`JacORB home page`: http://www.jacorb.org

.. _`Tango ATK reference on-line documentation`: http://www.esrf.eu/computing/cs/tango/tango_doc/atk_doc/index.html

.. _`ASTOR home page`: http://www.esrf.eu/computing/cs/tango/tango_doc/tools_doc/astor_doc/index.html

.. _`JIVE home page`: http://www.esrf.eu/computing/cs/tango/tango_doc/tools_doc/jive_doc/index.html

.. _`Tango ATK Tutorial`: http://www.esrf.eu/computing/cs/tango/tango_doc/atk_tutorial/Tutorials.pdf

.. _`ATK Tutorial`: `Tango ATK Tutorial`_

.. _`ZMQ home page`: http://zeromq.org/

.. _`Tango class development reference documentation`:
    http://www.esrf.eu/computing/cs/tango/tango_doc/kernel_doc/cpp_doc/index.html

.. _`Sphinx`: http://www.sphinx-doc.org

.. _`Sphinx webpage`: `Sphinx`_

.. _`Docutils`: http://docutils.sourceforge.net/index.html

.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html

"""

# rst_prolog = """
# .. role:: audition
#
# .. role:: lang
#
# """


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
			'_build',
			'_templates',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "sticky_navigation": True,
    "collapse_navigation": False
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_theme']

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if True:  #
    # Override default css to get a larger width for ReadTheDoc build
    html_context = {
        'extra_css_files': [
           # 'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
           # 'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/tango_cs_theme.css',
            '_static/css/meta_label_tango.css'
        ],
    }



# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'img/logo_tangocontrols_white.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'img/favicon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TangoControlsDocumentationdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('contents', 'TangoControlsDocumentation.tex', u'Tango Controls Documentation',
   u'Tango Community (CC BY 4.0)', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'tangocontrolsdocumentation', u'Tango Controls Documentation Documentation',
     [u'Tango Community, 3Controls, Piotr Goryl'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'TangoControlsDocumentation', u'Tango Controls Documentation',
   u'Tango Community (CC BY 4.0)', 'TangoControlsDocumentation', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Tango Controls Documentation'
epub_author = u'Tango Community'
epub_publisher = u'Tango Community'
epub_copyright = u'2017-2019, Tango Community, CC BY 4.0'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'Tango Controls Documentation'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}


# link checking options

linkcheck_ignore = [
                        r'http://localhost:\d+/*', r'https://localhost:\d+/*',
                        r'http://localhost/*', r'https://localhost/*',
                    ]

# metalabels
meta_labels = {
    'audience': {
        'allowed_values': ['administrators', 'developers', 'users', 'beginners', 'all'],
        'visible': True,
        'label': 'Intended audience: ',
        'post_label': '',
    },
    'lang': {
        'allowed_values': ['c++', 'java', 'python', 'all'],
        'visible': True,
        'label': 'Programming language: ',
        'post_label': '',
    },
}


