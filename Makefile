# (c) 2021 Mineyuki Iwasaki

all:
	@make debug
	@make release
	
debug:
	@mkdir -p docs-local
	@cp -fr css docs-local
	@cp -fr images docs-local
	@cp -fr js docs-local
	@cp -fr press-kits docs-local
	@cp -f etc/app-ads.txt docs-local
	@cp -f etc/CNAME docs-local
	@tools/make-html.py docs-local
	@tools/make-sitemap.py docs-local
	@tools/optimize-html.py docs-local

release:
	@mkdir -p docs
	@cp -fr css docs
	@cp -fr images docs
	@cp -fr js docs
	@cp -fr press-kits docs
	@cp -f etc/app-ads.txt docs
	@cp -f etc/CNAME docs
	@tools/make-html.py docs
	@tools/make-sitemap.py docs
	@tools/optimize-html.py docs

check:
	@tools/check-link.py docs

clean:
	@rm -fr docs-local
	@rm -fr docs
