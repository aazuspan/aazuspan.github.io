.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

# Print the comment for each make command
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


publish: ## Build and push to Github Pages
	pelican content -o output -s pelicanconf.py
	ghp-import output
	git push origin gh-pages
