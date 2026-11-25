# Cozzipay Reusable Prompts

These are the prompts used, in order, to research and build lead lists for Cozzipay (cozzipay.com), a card-free wallet that lets people in Africa pay for online platforms and services. Each prompt is in its own code block so it copies cleanly. The prompts are verbatim, including original typos.

Prompts 8, 11 and 12 were followed by files in this repo:

- Prompt 8: `cozzipay-ai-saas-platforms.xlsx` and `cozzipay-ai-saas-platforms.md`
- Prompt 11: `cozzipay-ai-saas-platforms-batch2.xlsx` and `cozzipay-ai-saas-platforms-batch2.md`
- Prompt 12: `cozzipay-africa-expansion-startups.xlsx` and `cozzipay-africa-expansion-startups.md`

---

## 1. Research Cozzipay and build ICP and outreach copy

**Purpose / when to use:** Start of a project. Gets the AI to learn the product, define the ICP and draft outreach copy.

**Tip:** Use a tool that can browse the web so it reads cozzipay.com directly.

~~~text
Check Cozzipay.com understand the platform value proposition, I want to do online research for potential platforms that can integrate Cozzipay, you will find who our ICP are and get the platforms , their email and LinkedIn and write a great sales copy to reach out to them
~~~

## 2. Google Workspace and MCP question

**Purpose / when to use:** Check whether the AI can create Google Sheets and Docs and connect to an MCP.

**Tip:** Capabilities depend on the tool. Ask this early so you know whether to expect files or text.

~~~text
Is it possible for you to connect with my Google workspace and create spreadsheet to put all the platforms you recommend to integrate Cozzipay for me and can you create Google doc Also, can you connect with an MCP?
~~~

## 3. MCP setup question

**Purpose / when to use:** Find out where to configure extra MCP servers in your AI tool.

**Tip:** Name your tool (for example Kiro, Claude, Cursor) to get exact steps.

~~~text
Where do I do my setup to add more mcp
~~~

## 4. Clarifying the micro-task platform type

**Purpose / when to use:** Define the target merchant type: micro-task and social growth platforms.

**Tip:** Giving concrete examples of the platform type keeps the research on target.

~~~text
No, I mean platforms that offer services that are micro tasks or sell stuff like YouTube subscribers, instagram followers, surveys and give users task/activities to do
~~~

## 5. Research 50 micro-task platforms with reviews

**Purpose / when to use:** Build a vetted list of 50 platforms and check reputation and African payment problems.

**Tip:** Reddit and Trustpilot need live search. Without it, the AI may rely on stale memory.

~~~text
Yes, but first research and gather 50 of these types of of platforms for me, also check their Reddit reviews, trustpilot and what people are saying about them, check for their problems if users are having payment problems with them from Africa
~~~

## 6. Create the ICP, research prompt, and 50-platform document

**Purpose / when to use:** Produce the ICP markdown file, a reusable research prompt, and a Word document with 50 leads and email copy in a table.

**Tip:** Ask for the table columns you want (name, URL, email, LinkedIn, pain point, email copy).

~~~text
Okay I want you to write out this Target audience, the ICP and the prompt to research and find this type of merchant and platforms and make the list, put it in md file and also create the docx document for 50 list of the potential merchants/platfoms that we discussed with email copy to send to them, put it in a table for easy read
~~~

## 7. Push files to a GitHub repo

**Purpose / when to use:** Save the generated files to a GitHub repository.

**Tip:** Replace the URL with your own repo. The AI needs repo access to push.

~~~text
https://github.com/icreed/LeadsList.git

Okay here is a repo push them here
~~~

## 8. Batch 1: 100 AI and SaaS platforms

**Purpose / when to use:** Get 100 AI and SaaS products with an African audience that need to receive payment from Africa.

**Tip:** Output files for this batch: `cozzipay-ai-saas-platforms.xlsx` and `.md`.

~~~text
Okay now give me 100 more platforms that need to receive payment from Africa I need AI platforms, saas products that has African audience
~~~

## 9. Spreadsheet and md versions with email copy

**Purpose / when to use:** Request both file formats: an md list of platforms only, and a spreadsheet with the list plus per-platform email copy.

**Tip:** Say which columns belong in each file to avoid rework.

~~~text
Put them in spreadsheet file format and also an md file copy 

The Md file should just be the platform list, while the spreadsheet file should have list and email copy to send to each of the platforms to get them for us.
~~~

## 10. Fix copy quality

**Purpose / when to use:** Ask the AI to correct problems in the generated copy.

**Tip:** This prompt only works right after the AI output. Name the specific problems (generic copy, wrong names, repeated text) when reusing it standalone.

~~~text
Okay fix them,
~~~

## 11. Batch 2: 100 smaller platforms

**Purpose / when to use:** Get 100 more AI and SaaS platforms that are smaller and easier to reach than the big names.

**Tip:** Output files for this batch: `cozzipay-ai-saas-platforms-batch2.xlsx` and `.md`.

~~~text
Okay now give me another 100 more platforms that are not the big platforms that may be hard to get those need to receive payment from Africa, I need AI platforms, saas products that has African audience 

Put them in the files as before also
With Md file version too
~~~

## 12. Batch 3: 150 Africa-expansion startups

**Purpose / when to use:** Find startups not yet in Africa whose products could earn up to $1m from African users, to pitch Cozzipay as their payment method.

**Tip:** Output files for this batch: `cozzipay-africa-expansion-startups.xlsx` and `.md`. Back the $1m claim with a simple market-size estimate.

~~~text
Okay Iet look for another 150 batch of startups that are not currently in Africa market but they have products that are solving significant problems that African users can use, and subscribe for or pay for. 

This ones are the one we will market African potential to, how they can make up to $1m in revenue from across Africa by expanding to Africa and having a seamless payment method for Africans to pay on their platform which is Cozzipay

So we need the ones that will see potential to expand to Africa and make more money
~~~

## 13. Save prompts

**Purpose / when to use:** Collect all prompts into one reusable markdown file (this file).

~~~text
Okay I need you to help me put all the prompt I have send to you into an Md file so that I can reuse them
~~~

---

## Tips for better results

- Use a tool with live web search, or connect a search MCP, so research reflects current data and not memory.
- Enrich contacts with Apollo, Hunter or LinkedIn Sales Navigator. AI-suggested emails are often guesses.
- Verify every claim before sending: platform details, review summaries, and payment-problem reports.
- Replace the "30-40% decline" claim in the outreach copy with Cozzipay's own data, or remove it.
- Check Cozzipay's compliance policy before approaching SMM panels and similar services.
- Run batches in small groups (25 to 50) and spot-check each one for duplicates and dead links.
- Ask for a fixed table layout up front so batches combine cleanly.
