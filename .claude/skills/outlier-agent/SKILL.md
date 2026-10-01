---
name: outlier-agent
description: Finds LinkedIn posts in a founder's or executive's niche that massively outperformed their own creator's usual numbers, then breaks down what made them break through (hook, format, angle, emotional trigger) so the user knows what's working right now. Use this skill whenever someone wants to know what content is working on LinkedIn in their space, find viral or top-performing posts, study competitors' or creators' best posts, build a swipe file, figure out which formats or hooks to try next, or asks why some posts blow up and theirs don't. Works best with the watchlist from an ICP Brief made by the icp-research-agent skill.
---

# Outlier Agent

"Viral" on its own tells you almost nothing. A post with 5,000 reactions from someone with 400,000 followers is an average day for them. A post with 900 reactions from someone who normally gets 60 is a signal that something about that idea, hook or format hit a nerve.

So this skill judges every post against **its own creator's normal**. An outlier is a post that did at least 3x what that creator usually gets. Then it works out what that post did differently, and which of those differences show up across several creators. That pattern is what's working right now.

It hands over patterns and structures to test. It never hands over posts to copy. The structure is borrowable, but the words belong to whoever wrote them, and a copied post reads as copied.

## Before you start

**Load the ICP Brief** if one exists (an uploaded file, project knowledge, or `content-research/icp-brief.md` if you can read files). Its outlier handoff section has the watchlist, and its triggers help explain why a post landed with this particular buyer.

**If there's no ICP Brief,** ask for:

1. Who your buyer is (role, type of company)
2. 10 to 20 LinkedIn creators your buyer reads, or peers in your niche. Names or profile links are fine. If they don't know, help them build the list with web search. Aim for a mix of creators the buyer follows, peers at a similar size, and a few bigger accounts.

## Step 1: Get the posts

This skill works from a focused watchlist, not the whole platform. That's deliberate. Outliers from 15 people your buyer already reads tell you far more than the platform's top 100 posts, which are mostly celebrities and giveaways.

For each creator you need their last 15 to 25 posts, with the reactions and comments count on each (reposts too if visible) and how old each post is. Read `references/collecting-posts.md` and pick the easiest method that works in the user's setup:

- **Paste:** the user copies posts from each creator's activity page into the chat. This works everywhere, takes about two minutes per creator, and is the most reliable.
- **Spreadsheet:** a CSV or export from any LinkedIn analytics or inspiration tool the user already has.
- **Browser:** if you have access to the user's browser, read each creator's recent posts page at a normal reading pace. Keep it to the watchlist. LinkedIn restricts automated collection, so never bulk-scrape.
- **Web search only (fallback):** search for recent widely shared posts in the niche. Engagement numbers found this way are unreliable, so say the results are low confidence.

Tell the user which method you're using and roughly how long it'll take on their side. If they're short on time, start with five creators. A small, clean sample beats a big, messy one.

## Step 2: Score against each creator's baseline

Put the posts into a table with one row per post and these columns: creator, reactions, comments, reposts, age (for example 3d or 2w), format, first line, and link.

If you can run code, save the table as a CSV and run the scoring script bundled with this skill (it's in this skill's folder, under `scripts/`):

```
python <this skill's folder>/scripts/score_outliers.py posts.csv
```

It handles messy numbers like "1.2K" and "2w", leaves out posts too new to judge, and flags thin baselines. If you can't run code, apply the same method by hand:

- **Engagement score** = reactions + (2 × comments) + (3 × reposts). Comments and reposts take more effort and push a post further, so they count for more. Tell the user this is a working heuristic, not LinkedIn's formula.
- **Leave out posts less than 3 days old.** They're still collecting engagement.
- **Baseline** = the median score of that creator's remaining posts. Use the median, not the average, so one monster post doesn't hide the others.
- **Outlier** = 3x the creator's median or more. **Strong** = 2x to 3x.
- **Baseline quality:** 8 or more posts is solid. 5 to 7 is thin, so flag it. Under 5, don't score that creator.

## Step 3: Work out why each outlier broke out

Compare each outlier to **that creator's typical post**. The difference between the two is the signal. Look at:

- **Hook:** the first line or two. What type is it? Examples: specific result with a number, contrarian claim, story that opens mid-scene, direct callout of the reader, confession, or a question.
- **Format:** text only, image, carousel or document, video, or poll. Did they switch formats?
- **Structure:** list, story, breakdown or teardown, framework, before and after, or a single sharp opinion.
- **Topic and angle:** what it's about, and the specific take. Map it to a pain or trigger from the ICP Brief where it fits.
- **Emotional driver:** status, fear, relief, validation, outrage, curiosity or humour.
- **Specificity:** real numbers, names, dates and places, compared with how that creator usually writes.
- **Length and readability:** much longer or shorter than usual? White space?
- **Ending:** question, CTA, lead magnet, or no ask at all.

Then separate what's copyable from what isn't. Some outliers were driven by things the user can't reproduce: breaking news they were first on, a personal milestone or tragedy, a famous person tagged or resharing, or a giveaway. Note those under "worth ignoring" so the user doesn't chase them.

## Step 4: Find the patterns

A single outlier is an anecdote. A pattern is **the same move showing up in outliers from two or more different creators.** Only call something a pattern when that's true, and name the creators and posts that show it.

Aim for three to five patterns. For each:

- What the move is, in one line
- The evidence (which outliers, which creators, and their multiples)
- Why it likely worked for this buyer (link to the ICP Brief's triggers)
- How the user could test it this week without copying anyone

## Step 5: Deliver the report

Use `references/report-template.md`. Keep quoted hooks short (a line or two, clearly attributed), because the report is for studying structure, not collecting other people's writing.

Save it:

- If you can write files, save it as `content-research/outliers/YYYY-MM-DD-outliers.md`, plus the scored CSV next to it for next time.
- Otherwise, deliver it in one block the user can copy.

In chat, give the short version: how many outliers you found, the strongest pattern, and the one experiment you'd run first.

## How often to run it

Weekly or every two weeks is plenty. Patterns shift over a month or two, not days. Re-running on the same watchlist also shows which patterns hold up over time, and those are the ones worth building a habit around.

## What this skill doesn't do

- **Write the post, or rewrite someone else's.** It gives structures and experiments. The user supplies the idea and the words.
- **Pretend to measure the whole platform.** It measures the watchlist, and says so.
- **Invent numbers.** If engagement counts are missing or unreliable, say so in the data notes rather than estimating.
