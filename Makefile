pPY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make local                          (re)generate the web site          '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	
local: 
	rm -fr content/.ipynb_checkpoints
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome http://localhost:8000
	pelican --listen

publish:
	rm -fr content/.ipynb_checkpoints
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS) --ignore-cache

github: publish
	rm -fr content/.ipynb_checkpoints
	git add -u 
	git commit -m 'Publish pelican content' 
	git push --all
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git checkout master
	git merge  $(GITHUB_PAGES_BRANCH) -m "Merging gh-pages into master"
	git push --all
	git checkout source

.PHONY: publish local github
