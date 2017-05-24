# Talk

Usa [markdown-to-slides](https://github.com/partageit/markdown-to-slides) per generare
le pagine HTML a partire da Markdown: nel mio caso ho usato nodejs installato
dentro un virtualenv

```
$ virtualenv .env && . .env/bin/activate
$ pip install nodeenv
$ nodeenv -p
$ npm install markdown-to-slides
$ markdown-to-slides --watch talk.md -o index.html
```
