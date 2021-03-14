#------------------------------------------------------------------------------
# (c) 2021 Mineyuki Iwasaki
#------------------------------------------------------------------------------

.PHONY: all clean local

DEPLOY_PATH = docs

# All
all:
	@make clean
	@cp -fr css $(DEPLOY_PATH)/
	@cp -fr images $(DEPLOY_PATH)/
	@cp -fr js $(DEPLOY_PATH)/
	@cp -fr press-kits $(DEPLOY_PATH)/
	@cp -f app-ads.txt $(DEPLOY_PATH)/
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
	@cp -fr css $(DEPLOY_PATH)/
	@cp -fr images $(DEPLOY_PATH)/
	@cp -fr js $(DEPLOY_PATH)/
	@cp -fr press-kits $(DEPLOY_PATH)/
	@cp -f app-ads.txt $(DEPLOY_PATH)/
	@cp -f CNAME $(DEPLOY_PATH)/
	@tools/make-html.py local
	@tools/make-sitemap.py
	@tools/optimize-html.py
