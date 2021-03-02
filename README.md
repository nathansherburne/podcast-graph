### Setup
#### Install NLP library for finding people names
`python -m spacy download en_core_web_sm`

#### Setup Obsidian for Graph visualization
1. Install: https://publish.obsidian.md/
2. Setup a vault in the directory of your choice

### Usage

### Examples
`OBSIDIAN_VAULT_PATH=~/Documents/Obsidian`
`python3 names.py ft.csv 1 > $OBSIDIAN_VAULT_PATH/Future\ Thinkers.md`
`python3 names.py thestoa.txt > $OBSIDIAN_VAULT_PATH/The\ Stoa.md`
