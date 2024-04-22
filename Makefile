# (c) 2021 Mineyuki Iwasaki

all:
	@mkdir -p docs
	@cp -fr css docs
	@cp -fr js docs
	@cp -fr press-kits docs
	@cp -f etc/app-ads.txt docs
	@cp -f etc/CNAME docs
	@tools/make-html.py
	@tools/make-image.py
	@tools/make-sitemap.py
	@tools/optimize-html.py
	@cp -fr docs docs-local
	@tools/make-local.py

check:
	@tools/check-link.py

clean:
	@rm -fr docs
	@rm -fr docs-local
