# weekend-ideas

A one-page picker for weekend activities. Open `index.html` in Chrome, set today's
conditions, and tap **Give me 5 ideas**.

- `ideas.csv` is the master list. Edit it in Google Sheets or any spreadsheet and keep the same column names.
- `index.html` carries its own copy of the list, so it works on its own.
- After changing `ideas.csv`, run `python3 build.py` to copy the new list into `index.html`.
- "We did this" is remembered only in the browser where you tap it. Use **Show my done list**
  to see what you've marked, then copy it into the "Done before" column of `ideas.csv`.
