.. -*- mode: rst -*-

|Python35|_

.. |Python35| image:: https://img.shields.io/badge/python-3.5-blue.svg
.. _Python35: https://badge.fury.io/py/scikit-learn


Blog
====

Nicolas Thiebaut's data science blog.

Hosted on github pages.

Built following `this blog post <https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/>`_, with the `Flex theme <https://github.com/alexandrevicenzi/Flex>`_.

For local testing:

* Run ``pelican content`` to generate the HTML.
* Switch to the output directory.
* Run ``python -m pelican.server``.
* Visit localhost:8000 in your browser to preview the blog.

To create master branch follow the procedure explained `here <http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/>`_. From the source branch:

* Add modified files (git add -u) and commit
* Remove .ipynb_checpoints if they exist
* pelican content -s publishconf.py (you may have to delete existing .ipynb_checkpoints in the content folder if you get an error)
* if branch gh-pages does not exist: git branch gh-pages
* ghp-import output
* commit gh-pages branch
* git checkout master
* git merge gh-pages
* git push --all
