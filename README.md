# Bahtera

Bahtera is a Jekyll site for institution-level Bitcoin consultancy in Indonesia, Malaysia, Singapore, India, and the Philippines. The site uses a cream-and-navy visual system and a ship mark (PNG, in `images/logo/`).

## Work locally

```sh
bundle install
bundle exec jekyll serve
```

`bundle exec jekyll build` writes the generated site to `_site/`. The deployment workflow rebuilds it on pushes to `main`.

## Site content

- `index.md` and `_layouts/home.html` contain the landing page.
- `about.md`, `services.md`, `team.md`, `contact.md`, `blog.md` (the News page), define the main pages.
- `_services/`, `_team/`, `_myths/`, and `_posts/` contain detail pages and articles.
- `_data/menus.yml` controls navigation.
- `_config.yml` contains the site name, tagline, and logo paths.

Contact details in `_data/contact.yml` must be verified before enabling email enquiries. With no address configured, the contact page offers a local conversation brief without submitting information.

## Brand assets

The logo lockups and icon are in `images/logo/`; the favicon is `images/favicon-64x64.png`. Site colours and regional-section styles are in `_sass/_cream-theme.scss`.

Content pillars: `_myths/` (answer-first myth pages) and `_guides/` (practical guides), each with `author`, `reviewer`, `related_guide` and `example: true` front matter. Set `example_content: false` in `_config.yml` to hide the "Example draft" banner once real content is in.

`images/regions-map.svg` highlights Indonesia, Malaysia, Singapore, India, and the Philippines. Its country outlines are derived from [Natural Earth 1:50m Admin 0 countries](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/), a public-domain map dataset. The Singapore marker is enlarged for readability.

The project retains the original Jekyll Serif theme licence in `LICENSE`.

## SEO and AI discoverability

`_includes/seo.html` renders the title, meta description, canonical link, Open Graph/Twitter tags and schema.org JSON-LD (organization, services, team members, breadcrumbs, blog posts, FAQ) for every page. Optional front matter per page:

- `seo_title`: the full `<title>` text (defaults to `Page title | Bahtera`)
- `meta_description`: the snippet text (defaults to `description`, then `summary`, then the excerpt)
- `image`: a PNG/JPG share image (defaults to `images/og-image.png`)
- `noindex: true`: keeps a page out of search results and the sitemap
- `last_modified_at`: the date the content was last reviewed

`sitemap.xml`, `robots.txt`, `feed.xml` and `llms.txt` are generated from site content. `url` in `_config.yml` sets the canonical host; update it if the site moves to a custom domain. Add Search Console / Bing verification codes in `_data/seo.yml`.
