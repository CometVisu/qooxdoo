# -*- coding: utf-8 -*-
#
# qooxdoo documentation build configuration file, created by
# sphinx-quickstart on Thu May 20 09:23:10 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.ifconfig']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'qooxdoo'
copyright = u'2011-2012, ' + project + ' developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0'
# The current git branch (used for github links)
git_branch = "master"

# qooxdoo Source Text Macros
# use e.g. as "%{version}" anywhere in .rst files
vMajor = "2"
vMinor = "0"
vPatch = ""
qxmacros = {
    "version"  : vMajor + '.' + vMinor + (('.' + vPatch) if vPatch else '')
   ,"versionL" : vMajor + '.' + vMinor + '.x' # latest in this line
   ,"versionU" : vMajor + '_' + vMinor + (('_' + vPatch) if vPatch else '') # underscore notation for SourceForge viewvc links
   ,"JS"       : "JavaScript"
   ,"qooxdoo"  : project
   ,"Website"  : "qx.Website"
   ,"Server"   : "qx.Server"
   ,"Desktop"  : "qx.Desktop"
   ,"Mobile"   : "qx.Mobile"
   ,"Q"        : "q"
   # following are some technical values about qooxdoo that might need adaption
   # from time to time (not necessarily with every release)
   ,"sdk_unpacked" : "110"   # disk requirements for unpacked SDK, in MB
   ,"cache_average_min" : "0.5" # average lower bound for cache space on disk, in GB
   ,"cache_average_max" : "1.5" # average upper bound for cache space on disk, in GB
}

# more qxmacros
if 'QOOXDOO_RELEASE' in os.environ and os.environ['QOOXDOO_RELEASE']=='1':
    qxmacros['release_tag'] = 'release_' + qxmacros['versionU']
else:
    qxmacros['release_tag'] = git_branch

print "Github links will use:", qxmacros['release_tag']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []
exclude_patterns = ["**._skip_.rst"]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# Highlight language
highlight_language = 'javascript'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = '_theme.indigo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["."]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Manual (v" + version + ")"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'qooxdoo doc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual], toctree_only [True/False]).
latex_documents = [
  ('index', 'qooxdoo.tex', u'qooxdoo Documentation',
   u'qooxdoo developers', 'manual', True),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''
latex_elements = {
    #'preamble' : r'\setcounter{tocdepth}{3}'  # this is *with* headers in index.rst
    'preamble' : r'\setcounter{tocdepth}{2}'  # this is *without* headers in index.rst
}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# -- Custom options ------------------------------------------------------------

# config vars
qxcomponents = 'all'

# Make this file an extension
def setup(app):
    app.connect('source-read', qxmacro_resolve)
    app.add_config_value('qxcomponents', 'all', 'env')
    
##
# qooxdoo macro extension
import string
class MyTemplate(string.Template):
    delimiter = "%"

# <source> - [<filecontent>]; http://sphinx.pocoo.org/ext/appapi.html#event-source-read
def qxmacro_resolve(app, docname, source):
    templ     = MyTemplate(source[0])
    source[0] = templ.safe_substitute(qxmacros)

