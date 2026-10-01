---
name: newsjacking-agent
description: Finds breaking news from the last few days in a founder's or executive's industry that their buyers care about, verifies it against real sources, and ranks it by how worth posting about it is, with angles the user can take in their own voice. Use this skill whenever someone wants to newsjack, react to industry news on LinkedIn, find something timely to post about, see what's happening in their space this week, get fresh content ideas from the news, or be first to comment on a story. Works best with an ICP Brief from the icp-research-agent skill, but can run from a quick intake without one.
---

# Newsjacking Agent

Newsjacking works because timing does half the work. A sharp take on something that broke yesterday gets read. The same take next week sounds like everyone else's. This skill's job is to find what's genuinely new in the user's world, check that it's real, and hand over the few stories worth reacting to, while there's still time to be early.

It finds the news and the angles. The take itself has to be the user's, because a take is only worth reading if it comes from someone with standing to have it.

## Before you start

**Web search has to be on.** If it isn't, stop and tell the user to turn it on. Don't fall back to news you remember. It will be out of date, and a stale or wrong "newsjack" is worse than none: it gets corrected in the comments, and the post has nothing new to say.

**Load the ICP Brief** if one exists (an uploaded file, project knowledge, or `content-research/icp-brief.md` if you can read files). Use its newsjacking handoff section (keywords, publications, companies to watch) and its pains and triggers, which decide what counts as relevant.

**If there's no ICP Brief,** ask these in one message, then continue:

1. What's your industry, and what do you sell?
2. Who's your buyer? (role, type of company)
3. Three to five topics you can credibly comment on.
4. Any competitors, companies or publications you already watch?

Mention once that running the icp-research-agent skill first would make this sharper, but don't make it a blocker.

## Step 1: Set the window

Today's date anchors everything. Say it explicitly in your searches and check it against each article's publish date.

- **Primary window: the last 72 hours.** This is newsjacking territory.
- **If that comes up thin, widen to 7 days** and say you did.
- **Past 7 days, it's no longer newsjacking.** Something older can still be a good post, but it's commentary, not a reaction. Put it in a separate "not news anymore, still useful" line rather than presenting it as fresh.

## Step 2: Search in buckets

Build 8 to 15 narrow searches across these buckets. Use the ICP Brief's keywords, and add the current month and year to queries:

1. **Industry news.** Launches, funding, acquisitions, shutdowns, big hires and departures in the user's space.
2. **The buyer's world.** Anything that changes the buyer's job: regulation, platform or algorithm changes, pricing changes from tools they rely on, new data about their role.
3. **Competitors and adjacent companies.** Product launches, funding rounds, exec moves, pivots.
4. **Big tech and AI news with a real line to the buyer.** Only if you can explain in one sentence why this buyer would care. Most AI news fails this test for most audiences.
5. **The argument of the week.** What people in the niche are debating right now: a viral post, a controversial report, a public spat about an idea.

One entity or topic per search. A search about seven companies at once returns shallow results about all of them. Loop instead.

Plain topic searches mostly return evergreen blog posts ("The CFO's guide to 2026"), not news. To find what's actually new:

- **Put dates in the query:** the exact dates of the last few days ("September 26, 2026"), or "this week" plus the month and year.
- **Search the publications in the ICP Brief directly:** [publication name] [topic], or `site:[publication domain] [topic]`.
- **Use weekly roundups and industry newsletters as a map.** Columns like "exec moves this week" or "funding roundup" cover a lot of ground fast. Then go to the primary source for each item worth keeping.
- **Search for the event, not the theme.** "[competitor] raises", "[company] launches", "[regulator] announces" find news. "Trends in [industry]" finds think pieces.

## Step 3: Verify before you rank

Everything that makes the final list has to pass this, because the user is going to put their name on a reaction to it:

- **Open the actual article.** Don't rely on the search snippet. Check the publish date on the page itself, since old stories get resurfaced and re-dated all the time.
- **Prefer primary sources.** Use the company's own announcement, the filing, the regulator's page, or the original report. Otherwise use a reputable outlet that did its own reporting.
- **Label confidence:**
  - **Confirmed:** two or more independent sources, or the primary source itself
  - **Single source:** one credible report, not yet picked up elsewhere
  - **Developing:** facts still moving, so say what's unclear
- **Watch for press releases dressed as news,** vendor surveys dressed as research, and numbers that appear in only one place.
- **Never fill a gap with a guess.** If you can't confirm a detail, leave it out or mark it unconfirmed. A shorter, true list beats a longer, shaky one.

## Step 4: Rank by post opportunity

Score each verified story on four things:

- **Fresh:** how recent it is (24 hours is best, 72 hours is good, 7 days is the limit)
- **Relevant:** whether it touches a specific pain or trigger from the ICP Brief
- **Standing:** whether the user can credibly have an opinion here, given what they do. Their experience should make the take worth more than a random person's.
- **Angle:** whether there's something to say beyond "this happened." That could be a contrarian read, a practical "here's what this means for you," a prediction, or a first-hand story it connects to.

Then sort each story:

- **Post today (high):** all four are strong
- **Worth a post this week (medium):** relevant and credible, but the angle or timing is weaker
- **Logged (low):** worth knowing, not worth a post. One line each.

**Leave these out entirely,** even if they're big news: tragedies, layoffs framed as content opportunities, anything that means mocking a person or company's failure, and political fights outside the user's lane. Take on ideas, not people. A post that looks like it's profiting from someone's bad day costs more trust than it earns.

## Step 5: Build the brief

Use the template in `references/brief-template.md`. For each high or medium story, include:

- **What happened,** in two or three plain sentences, with the date and source link
- **Why the buyer cares,** tied to a named pain or trigger from the ICP Brief
- **Two or three angles.** Each one is a single sentence describing a position, not a drafted post. Label the type: contrarian, what this means for you, prediction, or first-hand.
- **Your take:** two or three questions for the user to answer before writing, such as "Has this happened to one of your clients?", "Do you agree with the company's reasoning?", or "What would you tell a buyer who's worried about this?". Their answers are the post. This is how the take stays in their own voice.
- **Where the conversation is:** if you found people already posting about it, name the most visible one or two. Commenting early and well on the biggest post about a story is often worth as much as posting your own.
- **Window:** roughly how long before this goes stale (hours or days)

Close the brief with a short "what I searched" section: the buckets covered, how many stories were checked, and which searches came up empty. An honest "nothing worth posting this week in X" is a valid result.

## Step 6: Save and summarise

- If you can write files, save the brief as `content-research/news/YYYY-MM-DD-newsjacking.md`.
- Otherwise, deliver it in one block the user can copy.

In chat, keep the summary to a few lines: how many stories are worth posting today, the single best one and why, and anything time-sensitive.

## How often to run it

Two or three times a week works for most people, for example Monday, Wednesday and Friday mornings. News moves fast enough that a weekly run misses most of the good windows. If the user's setup supports scheduled or recurring tasks, offer to set one up.

## What this skill doesn't do

- **Write the post.** It gives angles and questions. The user's answers become the post.
- **Report news from memory.** Every item comes from a live search and an opened source.
- **Pad the list.** Three strong stories beat ten weak ones.
