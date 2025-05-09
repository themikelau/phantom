# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Phantom'
copyright = '2025 The Authors'
author = 'Daniel Price'

# The short X.Y version
version = '2025.0'
# The full version, including alpha/beta/rc tags
release = '2025.0.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxfortran.fortran_domain',
    'sphinxfortran.fortran_autodoc',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#
# custom css files
#
html_css_files = [
    'css/custom.css',
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Phantomdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Phantom.tex', 'Phantom Documentation',
     'Daniel Price', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'phantom', 'Phantom Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Phantom', 'Phantom Documentation',
     author, 'Phantom', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- options for sphinx-fortran
fortran_ext = [ 'f90','F90' ]

fortran_src = [
 '../src/setup/density_profiles.f90',
 '../src/setup/relax_star.f90',
 '../src/setup/set_bfield.f90',
 '../src/setup/set_binary.f90',
 '../src/setup/set_disc.f90',
 '../src/setup/set_dust.f90',
 '../src/setup/set_dust_options.f90',
 '../src/setup/set_flyby.f90',
 '../src/setup/set_planets.f90',
 '../src/setup/set_shock.f90',
 '../src/setup/set_slab.f90',
 '../src/setup/set_softened_core.f90',
 '../src/setup/set_sphere.f90',
 '../src/setup/set_stellar_core.f90',
 '../src/setup/set_vfield.f90',
 '../src/setup/stretchmap.f90',
 '../src/setup/velfield_fromcubes.f90',
 '../src/setup/phantomsetup.f90'
 '../src/tests/directsum.f90',
 '../src/tests/phantomtest.f90',
 '../src/tests/test_cooling.f90',
 '../src/tests/test_corotate.f90',
 '../src/tests/test_derivs.f90',
 '../src/tests/test_dust.f90',
 '../src/tests/test_eos.f90',
 '../src/tests/test_externf.f90',
 #'../src/tests/test_externf_gr.f90',
 '../src/tests/test_fastmath.f90',
 '../src/tests/test_geometry.f90',
 '../src/tests/test_gnewton.f90',
 '../src/tests/test_gr.f90',
 '../src/tests/test_gravity.f90',
 '../src/tests/test_growth.f90',
 '../src/tests/test_indtstep.f90',
 '../src/tests/test_kdtree.f90',
 '../src/tests/test_kernel.f90',
 '../src/tests/test_link.f90',
 '../src/tests/test_luminosity.f90',
 '../src/tests/test_nonidealmhd.f90',
 '../src/tests/test_ptmass.f90',
 '../src/tests/test_radiation.f90',
 '../src/tests/test_rwdump.f90',
 '../src/tests/test_sedov.f90',
 '../src/tests/test_setdisc.f90',
 '../src/tests/test_smol.f90',
 '../src/tests/test_step.f90',
 '../src/tests/testsuite.f90',
 '../src/tests/utils_testsuite.f90',
 '../src/main/boundary.f90',
 '../src/main/centreofmass.f90',
 '../src/main/commons.f90',
 '../src/main/cons2prim.f90',
 '../src/main/cons2primsolver.f90',
 '../src/main/damping.f90',
 '../src/main/datafiles.f90',
 '../src/main/eos_helmholtz.f90',
 '../src/main/eos_idealplusrad.f90',
 '../src/main/eos_mesa.f90',
 #'../src/main/eos_shen.f90',
 '../src/main/extern_Bfield.f90',
 '../src/main/extern_binary.f90',
 #'../src/main/extern_binary_gw.f90',
 '../src/main/extern_corotate.f90',
 '../src/main/extern_densprofile.f90',
 '../src/main/extern_gwinspiral.f90',
 '../src/main/extern_lensethirring.f90',
 '../src/main/extern_spiral.f90',
 '../src/main/extern_staticsine.f90',
 '../src/main/fastmath.f90',
 '../src/main/fs_data.f90',
 '../src/main/geometry.f90',
 '../src/main/gitinfo.f90',
 '../src/main/h2chem.f90',
 '../src/main/h2cooling.f90',
 '../src/main/inverse4x4.f90',
 '../src/main/krome.f90',
 '../src/main/mf_write.f90',
 '../src/main/mol_data.f90',
 '../src/main/options.f90',
 '../src/main/photoevap.f90',
 '../src/main/physcon.f90',
 '../src/main/quitdump.f90',
 '../src/main/random.f90',
 '../src/main/units.f90',
 '../src/main/utils_allocate.f90',
 '../src/main/utils_binary.f90',
 '../src/main/utils_cpuinfo.f90',
 '../src/main/utils_datafiles.f90',
 '../src/main/utils_deriv.f90',
 '../src/main/utils_dumpfiles.f90',
 '../src/main/utils_filenames.f90',
 '../src/main/utils_infiles.f90',
 '../src/main/utils_inject.f90',
 '../src/main/utils_mathfunc.f90',
 '../src/main/utils_sort.f90',
 '../src/main/utils_sphng.f90',
 '../src/main/utils_spline.f90',
 '../src/main/utils_tables.f90',
 '../src/main/utils_timing.f90',
 '../src/main/utils_vectors.f90',
 '../src/main/viscosity.f90',
]

sys.setrecursionlimit(10000)
