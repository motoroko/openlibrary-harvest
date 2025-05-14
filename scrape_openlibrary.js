const { chromium } = require('playwright');
const isbn = process.argv[2];
const url = `https://openlibrary.org/search?q=${isbn}`;

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'domcontentloaded' });

  try {
    const genres = await page.$$eval('.subjects .clamp a', els =>
      els.map(el => el.textContent.trim())
    );
    console.log(JSON.stringify({ isbn, genres }));
  } catch (e) {
    console.log(JSON.stringify({ isbn, genres: [], error: "Not found" }));
  }

  await browser.close();
})();
