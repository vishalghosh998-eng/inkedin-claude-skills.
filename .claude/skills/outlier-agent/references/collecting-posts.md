# Collecting posts for the outlier agent

Pick the first method that works. Walk the user through it in plain language, since most people have never looked at a creator's activity page closely.

## Method 1: Paste (works everywhere, recommended)

Tell the user:

1. Open the creator's LinkedIn profile.
2. Click **Show all posts** (in the Activity section), or go to `linkedin.com/in/<their-handle>/recent-activity/all/`.
3. Scroll until about 15 to 25 posts have loaded.
4. Select everything on the page (Ctrl+A or Cmd+A), copy, and paste it into the chat. Messy is fine.
5. Repeat for each creator. Doing a few at a time is fine too.

What you do with the paste:

- Split it into individual posts. Each post usually has the creator's name, a relative age like `3d`, `2w` or `1mo`, the post text, and the counts near the bottom: a reactions number, "N comments" and "N reposts".
- Skip reposts of other people's content (lines like "X reposted this") unless the user wants them, since they don't reflect the creator's own writing.
- If a count is missing for a post, leave it blank. Don't guess.
- Capture the first line or two as the hook, and note the format (text, image, carousel or document, video, or poll) if the paste makes it clear.

Tell the user what you parsed ("Got 22 posts from Jane, 18 from Sam") so they can spot anything that went wrong.

## Method 2: Spreadsheet or export

If the user already uses a LinkedIn analytics, scheduling or inspiration tool that exports posts with engagement, ask for the export as CSV or a pasted table. Map its columns to: creator, reactions, comments, reposts, age or date, format, first line, and link. The scoring script matches common column names on its own.

## Method 3: Browser (only if you have access to the user's browser)

- Visit each creator's recent activity page on the watchlist, one at a time, at a normal reading pace.
- Read what's on the page. Don't run scripts against LinkedIn, and don't collect from anyone outside the watchlist.
- Keep a session to the watchlist (about 20 creators at most). LinkedIn's terms restrict automated collection, and heavy use can get the user's account restricted. If LinkedIn shows a security check or a warning, stop and switch to Method 1.

## Method 4: Web search only (fallback)

Use this when none of the above is possible. Search for recent posts in the niche that got attention (for example, `site:linkedin.com/posts "[topic]"`, or articles rounding up top posts in the industry). Treat the output as inspiration, not measurement:

- Engagement counts from search results are often missing or stale.
- There's no creator baseline, so you can't calculate true outliers.
- Label the whole report **low confidence: no baseline data**, and focus on describing structures rather than ranking them.

## How much data is enough

- 10 to 20 creators × 15 to 25 posts each is the sweet spot.
- Fewer than 8 settled posts per creator makes their baseline thin. Include them, but flag it.
- Five creators with clean data is a perfectly good first run. The user can add more next week.

## Saving for next time

If you can write files, keep the combined table as `content-research/outliers/posts-YYYY-MM-DD.csv`. Next run, the user only needs to add new posts, and you can see which patterns held up.
