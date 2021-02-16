#------------------------------------------------------------------------------
# (c) 2021 Mineyuki Iwasaki
#------------------------------------------------------------------------------

.PHONY: all clean local

DEPLOY_PATH = docs

# All
all:
	@make clean
	@cp -fr css $(DEPLOY_PATH)/css/
	@cp -fr images $(DEPLOY_PATH)/images/
	@cp -fr js $(DEPLOY_PATH)/js/
	@cp -f CNAME $(DEPLOY_PATH)/
	@tools/make-html.py
	@tools/make-sitemap.py
	@tools/optimize-html.py

# Clean
clean:
	@rm -fr $(DEPLOY_PATH)/*

# Local
local:
	@make clean
	@cp -fr css $(DEPLOY_PATH)/css/
	@cp -fr images $(DEPLOY_PATH)/images/
	@cp -fr js $(DEPLOY_PATH)/js/
	@cp -f CNAME $(DEPLOY_PATH)/
	@tools/make-html.py local
	@tools/make-sitemap.py
	@tools/optimize-html.py
