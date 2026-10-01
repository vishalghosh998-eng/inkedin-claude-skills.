---
name: icp-research-agent
description: Researches exactly who a founder or executive should be posting for on LinkedIn (their ideal customer profile), then maps what that buyer reads, what they complain about, what triggers them emotionally and which topics make them stop scrolling. Produces an ICP Brief that the newsjacking-agent and outlier-agent skills reuse. Use this skill whenever someone wants to figure out who their content is for, understand their target audience or buyer, find content ideas their customers actually care about, build a buyer persona, research customer pain points, or asks "what should I post about" for a business. Use it before running the newsjacking or outlier agents if no ICP Brief exists yet.
---

# ICP Research Agent

Most founder content fails for a simple reason: it's written for "everyone on LinkedIn" instead of the handful of people who could actually buy. This skill fixes that first. It works out who the buyer is, then goes and listens to them (in their own words, in the places they already talk) so every post after this starts from a real pain instead of a guess.

The output is an **ICP Brief**. It's the shared memory for the other two agents: the newsjacking agent uses it to decide which news matters, and the outlier agent uses it to decide whose posts to study.

This skill does research, not writing. It stops at insight and angles. The posts themselves should be written by a human, because research is where AI is strong and voice is where it's weak.

## Before you start

Check whether an ICP Brief already exists (an uploaded file, project knowledge, or `content-research/icp-brief.md` if you can read files). If one exists and is less than three months old, ask whether the user wants to refresh it or start fresh rather than silently overwriting it.

Check that web search is available. Most of the value here comes from reading what real buyers say online. If search is off, tell the user to turn it on, and in the meantime build the brief from what they give you, with every section marked as unverified.

## Step 1: Intake (ask once, keep it short)

Ask these in a single message. Tell the user that "I don't know" is a fine answer, since the research fills gaps:

1. What do you sell, and roughly what does it cost?
2. Who signs off on buying it? (title, type of company, size or stage)
3. Describe two or three of your best customers. No names needed. Why did they buy?
4. What do prospects say right before they buy? And what's the most common reason they don't?
5. Your website and LinkedIn profile (optional, but it helps).
6. Anything raw you already have: sales call notes or transcripts, customer emails, reviews, DMs, survey answers. Paste or attach whatever's handy.

Raw material from item 6 is the best source you'll get, because it's the buyer talking unprompted. Weight it above anything found online.

If the user gives very little, don't keep asking. Make a sensible first guess at the ICP from what they said and their website, state that guess, and let the research sharpen it.

## Step 2: Pin down the buyer

Write down a precise definition before researching, because vague ICPs produce vague research:

- **Role and title** (and the two or three titles that are really the same job)
- **Company type, size or stage** (and what disqualifies a company)
- **What they own and what they're measured on.** This is where the real pains live.
- **Who else is in the decision** (boss, finance, a board, a team that has to use it)

If you find the ICP is actually two different buyers (for example, a founder at a 10-person startup and a VP at a 2,000-person company), say so and ask which one to research first. One brief per buyer.

## Step 3: Research how they think and talk

Read `references/research-playbook.md` for where to look and how to search. The short version: go where the buyer talks when nobody's selling to them. Look at forums and communities, reviews of tools they already buy, job postings for their role, podcasts and interviews with people in the seat, conference agendas, and industry surveys.

Rules that keep the research trustworthy:

- **Open the page, don't trust the snippet.** Search results are summaries, and the summary is often wrong or out of date. Fetch the actual page before using anything from it.
- **One topic per search.** Narrow searches find better material than one giant query.
- **Keep quotes verbatim and linked.** A real sentence from a real buyer beats any paraphrase. Never invent or "clean up" a quote into something nobody said.
- **Prefer the last 12 to 18 months.** Pains shift. An old forum thread can still be useful, but note the date.
- **Tag every finding** so the user knows what to trust:
  - `[You told me]` came from the user or their material
  - `[Found]` came from a source you opened (include the link)
  - `[My read]` is your inference. It's useful, but it's a hypothesis to test.

Aim for breadth first (8 to 15 distinct sources), then go deeper on whatever keeps coming up. A pain that shows up in three unrelated places is real. A pain you found once is a lead.

## Step 4: Turn research into triggers

This is where the brief earns its keep. Sort what you found into:

- **Pains**, ranked by how often and how intensely they show up. For each one, say how it shows up on a normal Tuesday, not just the abstract version.
- **Fears and stakes.** What gets this person blamed, passed over or fired? What keeps them up?
- **Desires and status.** What makes them look good to their boss, board or peers? What do they want to be known for?
- **Beliefs.** What do they already believe? What are they sceptical of? Which industry "truths" are they quietly tired of hearing?
- **Language.** Phrases they actually use, and words that make them cringe.
- **Emotional triggers.** The five to seven specific things that would make this person stop scrolling. Each one should be concrete enough that you could picture the post.

Then build the **content angle bank**: 15 to 20 post angles, each tied to a specific pain or trigger above. An angle is one sentence describing the take, not a drafted post. For example: "The real reason your board keeps asking about pipeline isn't pipeline." Mix reach angles (broad pains many people share) with trust angles (specific problems only a real buyer would recognise).

## Step 5: Build the handoff for the other agents

These two sections are what make the three skills work together, so don't skip them:

- **For the newsjacking agent:** industry keywords, topics the buyer follows, publications and newsletters they read, companies and competitors worth watching, and regulators or platforms whose changes hit this buyer.
- **For the outlier agent:** a watchlist of 10 to 20 LinkedIn creators whose posts this buyer reads or would read. Include creators the buyer follows, peers of the user at a similar size, and a few bigger accounts in the space. Give profile links where you can find them, and mark any you couldn't verify.

## Step 6: Deliver the brief

Use the template in `references/brief-template.md`. Keep it scannable, since the user will come back to it every week.

Then save it:

- If you can write files, save it as `content-research/icp-brief.md` in the user's working folder.
- If you can't (for example, in a regular chat), give the full brief in one block and tell the user to save it where their next chats can see it. The easiest option is adding it to a Claude Project's knowledge, so the newsjacking and outlier agents pick it up automatically.

Finish with a short summary in chat: the buyer in one sentence, the three strongest triggers, the biggest gaps in the research, and a suggestion to run the newsjacking agent or outlier agent next.

## What this skill doesn't do

- **Write posts.** It hands over angles. The words should be the user's.
- **Invent evidence.** A gap marked as a gap is more useful than a confident guess, because the user will build a month of content on this.
- **Research a private individual.** The subject is a type of buyer, not a named person. If the user asks for a profile of a specific prospect, keep it to their public professional content and don't go looking for personal details.

## Refreshing

Suggest a refresh every three months, or sooner if the user changes their offer, pricing or target market. On a refresh, keep what's still true, mark what changed, and update the date at the top.
