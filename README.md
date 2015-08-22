# Definition Expander
Generalizes definitions using DBpedia ontology and WordNet

## Scripts
###`WikiExtractor.py`
Parses a downloaded wikipedia dump and converts each article into an xml tag.

**Run**: `$ bzip2 -dc /path/to/pages-articles.xml.bz2 | python /path/to/WikiExtractor.py -l -o extracted`

Where `pages-articles.xml.bz2` is the latest pages bz2 dump file (e.g. http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)

This will write many files in the directory `extracted`. Make sure that this directory is under `/scratch`. See `navassa:/scratch/varot/defexpand/extracted` for sample output.

This script can also produce a JSON summary for informational purposes, and for calculating an `infobox_counts.tsv` file. See source file for more detailed usage.
