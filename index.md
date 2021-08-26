---
layout: home
---
This is a survey of sequence- and structure-based methods for embedding proteins with dense vectors.

It's generated with GitHub Pages from <a href="https://github.com/cthoyt/protein-embedding-review">
<img alt="GitHub logo" src="img/github-icon.svg" width="16" height="16" />
cthoyt/protein-embedding-review</a>. Content on this site is available under
the [CC0 1.0 Universal](https://github.com/cthoyt/protein-embedding-review/blob/main/LICENSE)
license.

## Contributing

You can contribute to this list in one of the following ways:

1. [Add a paper](https://github.com/cthoyt/protein-embedding-review/edit/main/_data/library.yml)
   through the GitHub editor
2. [Make an issue](https://github.com/cthoyt/protein-embedding-review/issues/new) with a suggestion

## Papers

{% for entry in site.data.library %} {% if entry.pdf %}
<strong><a href="{{ entry.pdf }}">{{ entry.title }}</a></strong>
{% elsif entry.arxiv %}
<strong><a href="https://bioregistry.io/arxiv:{{ entry.arxiv }}">{{ entry.title }}</a></strong>
{% elsif entry.pubmed %}
<strong><a href="https://bioregistry.io/pubmed:{{ entry.pubmed }}">{{ entry.title }}</a></strong>
{% elsif entry.pmc %}
<strong><a href="https://bioregistry.io/pmc:{{ entry.pmc }}">{{ entry.title }}</a></strong>
{% elsif entry.biorxiv %}
<strong><a href="https://bioregistry.io/biorxiv:{{ entry.biorxiv }}">{{ entry.title }}</a></strong>
{% elsif entry.doi %}
<strong><a href="https://bioregistry.io/doi:{{ entry.doi }}">{{ entry.title }}</a></strong>
{% endif %}
<br />{{ entry.author }} *et al.*, {{ entry.year }}
<br />
{% if entry.code %}
   This entry has code.
   {% if entry.packaged %}
      This entry is packaged.
      {% if entry.reusable %}
         This entry is trivially reusable.
      {% else %}
         This entry is not trivially reusable.
      {% endif %}
   {% else %}
      This entry is not packaged and therefore can not be trivially reused.
   {% endif %}
{% else %}
   This entry does not have code and therefore can not be reused.
{% endif %}
{% endfor %}
