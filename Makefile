docs :
	# poetry run python -m jupydocs convert
	typer jupydocs.cli  utils docs --output website/docs/api_reference_cli.md --name jupydocs
	echo '---\nid: module_cli\ntitle: cli module\n---\n' | cat - website/docs/api_reference_cli.md > temp && mv temp website/docs/api_reference_cli.md

website :
	cd website
	npm start