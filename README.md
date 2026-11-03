# Renew+ Training & Knowledge Portal

**Live site (after setup):** https://renewsankar.github.io/renew-plus-training-portal/

A web page that brings together every Renew+ Hair & Skin Care training document and video. Each item can be opened, watched or downloaded, and every PDF has a page index with thumbnails.

- **Brands:** Renew+ Hair & Skin Care · Renew Group of Companies
- **Technology partner:** Zelora Infotech

## What's included

| Item | PDF | Video |
|---|---|---|
| Employee Orientation Guide | 11 pages | – |
| Telecaller Training | – | 7:09 |
| Service Training Manual | 17 pages | 8:40 |
| Clinic SOP Handbook | 19 pages | 7:29 |
| Before & After Case Handbook | 37 pages | 3:45 |
| Hair Treatment Aftercare | 5 pages | 2:44 |
| Skin Treatment Aftercare | 6 pages | 3:11 |

## Document register

Each item has a unique document number. PDFs end in **-D** and videos end in **-V**. The numbers are shown on the website and also written into each file's properties (PDF Title/Subject/Keywords and MP4 title/comment).

| Doc No | Title | PDF | Video |
|---|---|---|---|
| RP-TRN-001 | Employee Orientation Guide | RP-TRN-001-D | – |
| RP-TRN-002 | Telecaller Training | – | RP-TRN-002-V |
| RP-TRN-003 | Service Training Manual | RP-TRN-003-D | RP-TRN-003-V |
| RP-OPS-001 | Clinic SOP Handbook | RP-OPS-001-D | RP-OPS-001-V |
| RP-CLN-001 | Before & After Case Handbook | RP-CLN-001-D | RP-CLN-001-V |
| RP-PAT-001 | Hair Treatment Aftercare | RP-PAT-001-D | RP-PAT-001-V |
| RP-PAT-002 | Skin Treatment Aftercare | RP-PAT-002-D | RP-PAT-002-V |

The prefixes stand for category: **TRN** = staff training, **OPS** = clinic operations, **CLN** = clinical documentation, **PAT** = patient care. The next new item in a category takes the next number, for example RP-PAT-003.

You can open any card directly with its number, for example `…/renew-plus-training-portal/#RP-OPS-001`.

## Website features

- **Video index:** each video card has a strip of chapter thumbnails with start times. Click one to play the video from that point.


- **Library cards:** each item has a cover thumbnail, a video thumbnail with its length, and buttons for **Open PDF**, **Watch video**, **Download PDF** and **Download video**.
- **Page index:** each PDF card has a "Page index" strip of page thumbnails. Click one to open the PDF at that page.
- **All downloads table:** lists every file with its type, length and size.
- **Find things fast:** filter by category, or use the search box.
- **Google indexing:** `sitemap.xml`, `robots.txt` and a canonical address are included.
- **Share preview:** links shared on WhatsApp, LinkedIn or Facebook show `assets/share-thumbnail.jpg`.

## Folder structure

```
index.html                 the web page (generated)
template.html, build_site.py   used to regenerate index.html
docs/                      PDFs
videos/                    MP4 videos
assets/logos/              Renew+, Renew Group and Zelora Infotech logos
assets/posters/            cover and video thumbnails
assets/pages/<pdf>/N.jpg   page-index thumbnails
assets/chapters/<video>/N.jpg  video chapter thumbnails
chapters.json              video chapter start times
assets/share-thumbnail.jpg social share image
sitemap.xml, robots.txt    search engine indexing
```

## Upload to GitHub (account: renewsankar)

1. Go to https://github.com/new while signed in as **renewsankar**.
2. Set the repository name to exactly `renew-plus-training-portal` (the page address depends on this name). Choose **Public**, leave "Add a README" unticked, and click **Create repository**.
3. On the empty repository page, click **"uploading an existing file"**.
4. Upload the files in two batches, because GitHub's web upload takes up to 100 files at a time:
   - **Batch 1:** drag in `index.html`, `template.html`, `build_site.py`, `README.md`, `sitemap.xml`, `robots.txt`, `.nojekyll`, and the `docs` and `videos` folders. Click **Commit changes**.
   - **Batch 2:** click **Add file → Upload files**, drag in the `assets` folder, and click **Commit changes**.
5. Go to **Settings → Pages**. Under *Build and deployment*, set Source to **Deploy from a branch**, Branch to **main**, and folder to **/ (root)**, then click **Save**.
6. After 1–3 minutes, open https://renewsankar.github.io/renew-plus-training-portal/

## Get it listed on Google (page indexing)

1. Open https://search.google.com/search-console and click **Add property → URL prefix**.
2. Enter `https://renewsankar.github.io/renew-plus-training-portal/`.
3. Choose the **HTML tag** verification method and copy the `<meta name="google-site-verification" …>` tag. On GitHub, open `index.html`, click the ✏️ pencil, paste the tag just under `<head>`, and commit. Then click **Verify** in Search Console.
4. In Search Console, open **Sitemaps** and submit `sitemap.xml`.
5. Optionally, use **URL inspection** on the home page and click **Request indexing**. Google usually lists the site within a few days.

## Adding or updating a file later

- **Replacing a file:** upload a new file with exactly the same name into `docs/` or `videos/`. The site updates within a minute.
- **Adding a new item:** add its entry to `ITEMS` in `build_site.py`, add a cover image to `assets/posters/` and page thumbnails to `assets/pages/`, then run `python3 build_site.py https://renewsankar.github.io/renew-plus-training-portal/` to regenerate `index.html`. Or ask Claude to do it.

## Privacy

GitHub Pages sites are public, and with indexing switched on they can appear in Google search. The Clinic SOP Handbook and the Before & After Case Handbook are internal drafts. Remove them, or skip the Google indexing steps, if they should not be public.
