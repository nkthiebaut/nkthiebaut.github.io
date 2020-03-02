.. -*- mode: rst -*-

|Python36|_

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://badge.fury.io/py/scikit-learn


Blog
====

Nicolas Thiebaut's data science blog.

Hosted on github pages.

Built following `this blog post <https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/>`_, with the `Flex theme <https://github.com/alexandrevicenzi/Flex>`_.

Setup 
-----

The blog requires `Pelican <http://docs.getpelican.com/en/stable/>`_ (``pip install pelican``) and `Ghp-import <https://github.com/davisp/ghp-import>`_ (``pip install ghp-import``)

Local testing
-------------

* Run ``pelican content`` to generate the HTML.
* Switch to the output directory.
* Run ``python -m pelican.server``.
* Visit localhost:8000 in your browser to preview the blog.


Publishing on GitHub pages
--------------------------

To create master branch follow the procedure explained `here <http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/>`_. From the source branch:

* Remove .ipynb_checkpoints from the content folder if they exist
* Run ``pelican content -s publishconf.py``
* if branch gh-pages does not exist: ``git branch gh-pages``
* Run ``ghp-import output``
* Add modified files (``git add -u``) and commit
* ``git checkout master``
* ``git merge gh-pages``
* `git push --all``
* ``git checkout source``

Automated publishing with MAKE
------------------------------

(from the repo root folder)
To test locally: ``make local`` (it will open chrome and run the pelican server)
To publish changes: ``make github``.
