# (c) 2021 Mineyuki Iwasaki

DEPLOY_PATH = docs

all:
	@make clean
	@mkdir -p $(DEPLOY_PATH)
	@cp -fr css $(DEPLOY_PATH)
	@cp -fr images $(DEPLOY_PATH)
	@cp -fr js $(DEPLOY_PATH)
	@cp -fr press-kits $(DEPLOY_PATH)
	@cp -f etc/app-ads.txt $(DEPLOY_PATH)
	@cp -f etc/CNAME $(DEPLOY_PATH)
	@tools/make-html.py
	@tools/make-sitemap.py
	@tools/optimize-html.py

local:
	@make clean
	@mkdir -p $(DEPLOY_PATH)
	@cp -fr css $(DEPLOY_PATH)
	@cp -fr images $(DEPLOY_PATH)
	@cp -fr js $(DEPLOY_PATH)
	@cp -fr press-kits $(DEPLOY_PATH)
	@cp -f etc/app-ads.txt $(DEPLOY_PATH)
	@cp -f etc/CNAME $(DEPLOY_PATH)
	@tools/make-html.py local
	@tools/make-sitemap.py
	@tools/optimize-html.py

clean:
	@rm -fr $(DEPLOY_PATH)
