Build System for our Website
############################

Getting started
===============

1. Make sure the submodules are checked out. This may take a while!

   ::

       git submodule update --init --recursive

2. Run pelican once to sort out any configuration issues there may be::

       make

3. When that works, use the following to start a devserver listening at
   `<http://localhost:8000>`_::

       make devserver

Documentation
=============

See http://docs.getpelican.com/en/stable/ for general documentation Pelican,
used to build the website.
