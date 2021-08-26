---
layout: home
---
This is a survey of sequence- and structure-based methods for embedding proteins with dense vectors.

It's generated with GitHub Pages from <a href="https://github.com/cthoyt/protein-embedding-review"><
img alt="GitHub logo"
src="img/github-icon.svg" width="16" height="16" /> cthoyt/protein-embedding-review</a>. Content on
this site is available under
the [CC0 1.0 Universal](https://github.com/cthoyt/protein-embedding-review/blob/main/LICENSE)
license.

## Contributing

You can contribute to this list in one of the following ways:

1. [Add a paper](https://github.com/cthoyt/protein-embedding-review/edit/main/_data/library.yml)
   through the GitHub editor
2. [Make an issue](https://github.com/cthoyt/protein-embedding-review/issues/new) with a suggestion

## Papers

{% for entry in site.data.library %}
<strong>
{% if entry.pdf %}
<a href="{{ entry.pdf }}">{{ entry.title }}</a>
{% elsif entry.doi %}
<a href="https://bioregistry.io/doi:{{ entry.doi }}">{{ entry.title }}</a>
{% elsif entry.arxiv %}
<a href="https://bioregistry.io/arxiv:{{ entry.arxiv }}">{{ entry.title }}</a>
{% elsif entry.pubmed %}
<a href="https://bioregistry.io/pubmed:{{ entry.pubmed }}">{{ entry.title }}</a>
{% elsif entry.pmc %}
<a href="https://bioregistry.io/pmc:{{ entry.pmc }}">{{ entry.title }}</a>
{% endif %}
</strong>
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% endfor %}
