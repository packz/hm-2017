# Talk

Usa [markdown-to-slides](https://github.com/partageit/markdown-to-slides) per generare
le pagine HTML a partire da Markdown: nel mio caso ho usato nodejs installato
dentro un virtualenv

```
$ virtualenv .env && . .env/bin/activate
(env) $ pip install nodeenv
(env) $ nodeenv -p
(env) $ npm install markdown-to-slides
(env) $ make
```

La presentazione sarà in ``staging_dir/index.html``.
