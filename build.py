from docx import Document
from docx.shared import Pt, Inches
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

M, G, S, X = "Micro-task / data work", "Survey panel", "GPT / offerwall", "SMM panel"
T = "Task exchange / other"
PAY = "Head of Payments; Head of Partnerships; Product Manager Payouts"
GROW = "Head of Growth; Head of Africa / Emerging Markets; Founder"
# (segment, platform, website, why, titles, risk, email)
P = [
(M,"Microworkers","microworkers.com","VERIFIED from its FAQ: all payments in USD; withdrawals Mon-Fri only; verification via SMS, PayPal Connect, Skrill Connect or Airtm Connect; ID and selfie KYC after $1 earned; withdrawal methods vary by country and the preferred one may not be offered; 10% service fee on satisfied tasks.",PAY,"Low","C"),
(M,"Clickworker","clickworker.com","Large micro-task workforce paid in small amounts; possible limited local withdrawal options for Africa.",PAY,"Low","C"),
(M,"Toloka","toloka.ai","Data labeling crowd with small frequent payouts; African workers may face limited withdrawal methods.",PAY,"Low","C"),
(M,"Remotasks","remotasks.com","AI data task platform with a global workforce including Africa; frequent small payouts.",PAY,"Low","C"),
(M,"Appen","appen.com","Crowd data work with contributors worldwide; payout friction possible for African contributors.",PAY,"Low","C"),
(M,"Amazon Mechanical Turk","mturk.com","Long-running micro-task marketplace; payout options for workers outside the US are limited.",PAY,"Low","C"),
(M,"Hive Micro","hivemicro.com","Micro-task platform with small task payments to a global workforce.",PAY,"Low","C"),
(M,"Telus International AI","telusinternational.com","AI data community with contributors across many countries; recurring small payouts.",PAY,"Low","C"),
(M,"Prolific","prolific.com","Research participant platform paying small amounts in many countries.",PAY,"Low","C"),
(M,"DataAnnotation","dataannotation.tech","AI training task platform with contractors paid frequently.",PAY,"Low","C"),
(G,"Swagbucks","swagbucks.com","Rewards and survey site with many small cash-outs.",PAY,"Low","C"),
(G,"Toluna","toluna.com","Global survey panel with small reward redemptions.",PAY,"Low","C"),
(G,"YouGov","yougov.com","Panel with points-based rewards; international members.",PAY,"Low","C"),
(G,"Survey Junkie","surveyjunkie.com","Survey panel with small payouts; check African country coverage.",PAY,"Low","C"),
(G,"Pollfish","pollfish.com","Survey platform that rewards respondents in many markets.",PAY,"Low","C"),
(G,"Opinion Outpost","opinionoutpost.com","Survey panel with small reward thresholds.",PAY,"Low","C"),
(G,"Pinecone Research","pineconeresearch.com","Survey panel with small per-survey rewards.",PAY,"Low","C"),
(G,"Branded Surveys","brandedsurveys.com","Survey panel with frequent small redemptions.",PAY,"Low","C"),
(G,"LifePoints","lifepointspanel.com","Panel with points redemption and international members.",PAY,"Low","C"),
(G,"Cint","cint.com","Survey exchange and infrastructure; a partner could reach many panels' payouts.",PAY+"; Head of Product","Low","A"),
(S,"Freecash","freecash.com","Offerwall and GPT site with large user base and frequent small cash-outs.",PAY,"Medium","C"),
(S,"Rewarded Play","rewardedplay.com","Play-to-earn rewards app with small payouts.",PAY,"Low","C"),
(S,"GameHag","gamehag.com","Gaming rewards community with many young, global users.",PAY,"Medium","C"),
(S,"Mistplay","mistplay.com","Mobile game rewards app with gift card style payouts.",PAY,"Low","C"),
(S,"Cointiply","cointiply.com","Crypto rewards site with micro-earnings; crypto adds compliance review.",PAY,"Medium","C"),
(S,"Lootably","lootably.com","Offerwall publisher with small user payouts.",PAY,"Medium","C"),
(S,"AdGate Media","adgatemedia.com","Offerwall network that could offer wallet payouts to publishers.",PAY,"Low","A"),
(S,"OfferToro","offertoro.com","Offerwall network with publishers and users in many countries.",PAY,"Low","A"),
(S,"Tapjoy","tapjoy.com","Mobile rewards and ad network; publisher and user payouts.",PAY,"Low","A"),
(S,"Timebucks","timebucks.com","Micro-task and GPT site with many African users and small payouts.",PAY,"Medium","C"),
(X,"JustAnotherPanel","","SMM reseller panel; buyers in Africa often lack working cards. Collection use case.",GROW,"High","D"),
(X,"Peakerr","","SMM panel with an international buyer base. Collection use case.",GROW,"High","D"),
(X,"SMMKings","","SMM panel; card-free deposits for African buyers.",GROW,"High","D"),
(X,"SMMRaja","","SMM panel; card-free deposits for emerging market buyers.",GROW,"High","D"),
(X,"SMMHeaven","","SMM panel; collection use case.",GROW,"High","D"),
(X,"BulkFollows","","SMM panel; collection use case.",GROW,"High","D"),
(X,"SMMStone","","SMM panel; collection use case.",GROW,"Medium","D"),
(X,"Followiz","","SMM panel; collection use case.",GROW,"High","D"),
(X,"TheYTLab","","YouTube-focused growth service; collection use case.",GROW,"High","D"),
(X,"SocialGreg","","Social growth service; collection use case.",GROW,"High","D"),
(T,"Like4Like","like4like.org","Social task exchange with premium purchases and cash-style rewards.",GROW,"Medium","D"),
(T,"Sub4Sub","sub4sub.net","Subscriber exchange community; premium purchases.",GROW,"Medium","D"),
(T,"Followeran","","Follower exchange service.",GROW,"High","D"),
(T,"Subpals","subpals.com","Subscriber exchange community.",GROW,"Medium","D"),
(T,"Fiverr","fiverr.com","Freelance marketplace; African sellers withdraw earnings.",PAY+"; Head of Africa","Low","A"),
(T,"Upwork","upwork.com","Freelance marketplace; African freelancers withdraw earnings.",PAY+"; Head of Africa","Low","A"),
(T,"Freelancer.com","freelancer.com","Freelance marketplace with many African users.",PAY+"; Head of Africa","Low","A"),
(T,"CPAlead","cpalead.com","Affiliate and offerwall network paying publishers, including in Africa.",PAY,"Medium","A"),
(T,"PTCShare","","Paid-to-click style site; review compliance first.",PAY,"Medium","C"),
(T,"ySense","ysense.com","Survey and task rewards site with small payouts.",PAY,"Low","C"),
]
assert len(P)==50

CLAIM = "claimed on cozzipay.com, to be validated"
VALUE = [
"Cozzipay is a card-free wallet for Africa. It currently covers Nigeria, Ghana, South Africa and Kenya, with more countries planned.",
"Users fund the wallet in local currency by bank transfer or mobile money, then pay globally in one click without a card.",
"Freelancers and earners can withdraw platform earnings (for example Fiverr, Upwork, ClickBank, PropellerAds, Popads) to a Cozzipay wallet, then cash out to a local bank.",
"Merchants integrate through a REST API, JS SDKs, plugins, or no-code payment links and invoices.",
"New: users can pay for AI subscriptions (ChatGPT, Claude, Midjourney) with auto-renewal.",
]
CLAIMS = [
"30-40%% of card payments in Africa are declined (%s)." % CLAIM,
"Support for 20+ African currencies (%s)." % CLAIM,
"Instant settlement (%s)." % CLAIM,
"Most merchants go live in under 30 minutes (%s)." % CLAIM,
]
AUD = [
("Payout platforms (micro-task, survey, GPT/offerwall, freelance, ad/affiliate networks)","Pay out small, frequent amounts to African users. Wires and card fees hurt, and withdrawal options are limited."),
("AI and SaaS selling to Africa","Collect payments from African users whose cards are declined or who have no card."),
("Digital goods and subscription sellers","Same collection problem, including recurring payments."),
("Payment infrastructure and aggregators","Could add Cozzipay as a local payment or payout rail."),
]
ICP_DEF = "Platforms with African users that either pay out small, frequent amounts, or collect payments from African users who lack working cards."
SEG = [
("1","Payout platforms (micro-task, survey, GPT/offerwall, freelance, ad/affiliate)"),
("2","AI/SaaS selling to Africa"),
("3","Digital goods and subscription sellers"),
("4","Payment infrastructure and aggregators"),
]
TITLES = ["Head of Payments","Head of Partnerships","Head of Growth / Africa / Emerging Markets","Product Manager, Payouts","Founder (at small companies)"]
SIGNALS = [
"Many users in Nigeria, Kenya, Ghana and South Africa.",
"Small payouts (under $10) where wires or card fees hurt.",
"USD-only payouts.",
"Limited country-specific withdrawal methods.",
"KYC friction.",
"Payout-related support tickets.",
]
RISK = "SMM panels that sell fake followers or views breach Instagram, YouTube and TikTok terms and are high-risk for payment partners. Cozzipay must confirm its compliance policy before contacting them. Genuine survey, task and GPT platforms are lower risk and should be contacted first."
DISC = "Disclaimer: this list was compiled from general knowledge and is not verified. Trustpilot, Reddit and LinkedIn could not be accessed. Emails and LinkedIn URLs were deliberately not guessed; they are marked 'To be enriched'. Only Microworkers has been checked (against its FAQ). No review or Africa-payment data has been collected. Websites are listed only where the domain is well known; blanks need confirming."

EMAILS = [
("A: Payout platforms","Faster payouts to your African users",
"Hi {{FirstName}},\n\nMany of {{Company}}'s users in Nigeria, Ghana, Kenya and South Africa lose time and money on payouts. Cards fail, wires are slow, and fees add up.\n\nCozzipay is a wallet built for this problem. Users withdraw their earnings to Cozzipay in one click and cash out to a local bank in minutes.\n\nFor you, that means fewer payout-related support tickets, better retention of African earners, and a single integration through our API (most teams go live in under 30 minutes).\n\nCould we do a 15-minute call next week? I can send a short integration overview first if you prefer.\n\nBest,\n{{Name}}\nCozzipay | cozzipay.com",
"Freelance marketplaces, ad/affiliate networks, offerwall networks, survey infrastructure"),
("B: Collecting payments (AI, SaaS, digital goods)","Recover the African checkouts your cards are declining",
"Hi {{FirstName}},\n\nCard decline rates in Africa reach 30-40%. Every declined card is a customer who wanted to pay you.\n\nCozzipay adds a card-free checkout option. Customers fund a wallet in local currency and pay in one click, with auto-renewal support for subscriptions.\n\nYou get a simple API, SDK or payment link, and settlement in local currency.\n\nWould it be useful to run a pilot on {{Company}}'s African traffic? I can share the integration docs today.\n\nBest,\n{{Name}}",
"AI/SaaS and digital goods or subscription sellers"),
("C: Micro-task, survey and GPT platforms","Give your African workers a simpler way to get paid",
"Hi {{FirstName}},\n\nMany {{Company}} members in Africa earn small amounts often. When payouts are USD-only or the withdrawal options in their country are limited, small balances get stuck or lose value to fees.\n\nCozzipay is a wallet built for African users. Members withdraw to Cozzipay in one click and cash out to a local bank, so even small payouts stay useful.\n\nWe can start with a pilot in one country, for example Nigeria or Kenya, and measure payout completion and support tickets before going further.\n\nCould we do a 15-minute call next week? I can send a short integration overview first.\n\nBest,\n{{Name}}\nCozzipay | cozzipay.com",
"Micro-task, survey, GPT/offerwall and paid-to-click platforms"),
("D: SMM panels and task exchanges","Card-free deposits for your African buyers",
"Hi {{FirstName}},\n\nBuyers in Africa often cannot top up their {{Company}} balance because their cards are declined or they do not have one.\n\nCozzipay offers a card-free option. Customers fund a wallet in local currency by bank transfer or mobile money, then pay in one click. You integrate through an API or payment link.\n\nOne note: Cozzipay reviews every merchant's compliance before onboarding, so we would ask for details about your services and platform terms first. If that is acceptable, I can share the integration docs.\n\nWould a short call make sense?\n\nBest,\n{{Name}}\nCozzipay | cozzipay.com",
"SMM panels and social task exchanges, only after Cozzipay's compliance check"),
]
LI = "Hi {{FirstName}}, I work on Cozzipay, a card-free wallet that helps platforms pay out to and collect from African users. I'd value your view on how {{Company}} handles Africa payments. Happy to connect."
FU = "Hi {{FirstName}}, following up in case my note got buried. A pilot would take less than a day of engineering, and we'd start with one country. Is it worth a quick call?"
NOTE = "Replace the numeric claims with Cozzipay's own data. Confirm Cozzipay is actually live as a payout option on any platform named before citing it."

PROMPT = """You are a research analyst. Find platforms that fit the profile below and build a verified list.

ICP
Platforms with African users that either (a) pay out small, frequent amounts, or (b) collect payments from African users who lack working cards. Our product is Cozzipay, a card-free wallet for Africa (Nigeria, Ghana, South Africa, Kenya) that lets platforms pay out to local banks and collect payments without cards.

SEGMENTS (priority order)
1. Payout platforms: micro-task, data labeling, survey panels, GPT/offerwalls, freelance marketplaces, ad and affiliate networks.
2. AI and SaaS products selling to Africa.
3. Digital goods and subscription sellers.
4. Payment infrastructure and aggregators.

HOW TO FIND PLATFORMS
- Search for "[platform type] Nigeria withdrawal", "[platform type] Kenya payout problem", "best paying survey sites in Africa", "GPT sites that pay in Africa".
- Check Trustpilot category pages, Reddit threads (r/beermoney, r/WorkOnline, r/Nigeria, r/Kenya, r/Ghana, r/AfricaOnline), Nairaland, and affiliate directories.
- Check each platform's help center and terms for payout methods and supported countries.
- Look for platforms whose users complain about cards declined, PayPal restrictions, USD-only payouts, KYC issues or withdrawal delays.

FOR EACH PLATFORM CAPTURE
- Website
- Segment
- Payout methods
- Countries supported
- Minimum payout
- Fees
- Trustpilot score and recurring complaints
- Reddit sentiment
- Africa-specific payment problems (declined cards, PayPal restrictions, USD-only, KYC issues, withdrawal delays)
- Compliance risk rating (Low, Medium, High) with a reason. Flag services that sell fake engagement or breach social network terms as High.
- Decision-maker titles (Head of Payments, Head of Partnerships, Head of Growth/Africa/Emerging Markets, Product Manager Payouts, founder at small companies)
- Public partnerships email
- Company LinkedIn URL
- Source URL and date for every claim

RULES
- Never invent emails, reviews, scores or quotes.
- Use only emails published on the company's own site or official pages.
- If a value cannot be confirmed, write "Not verified".
- Do not include platforms with no evidence of African users.
- Return a table, ranked by fit (many African users, small payouts, visible payout complaints, low compliance risk first), followed by a list of sources.
"""

# ---------- Markdown ----------
def esc(s): return s.replace("|","\\|").replace("\n","<br>")
def md_table(h, rows):
    out = ["| "+" | ".join(h)+" |", "|"+"|".join("---" for _ in h)+"|"]
    out += ["| "+" | ".join(esc(c) for c in r)+" |" for r in rows]
    return "\n".join(out)

HDR = ["#","Segment","Platform","Website","Why it fits","Target titles","Contact email","LinkedIn","Compliance risk","Recommended email","Status"]
def rows():
    for i,(s,n,w,y,t,r,e) in enumerate(P,1):
        yield [str(i),s,n,w,y,t,"To be enriched","To be enriched",r,e,"VERIFIED (FAQ)" if i==1 else "Unverified"]

md = ["# Cozzipay: Target Audience, ICP, Research Prompt and Platform List\n",
"## 1. Value proposition\n"]
md += ["- "+v for v in VALUE]
md += ["\nNumeric claims (all "+CLAIM+"):\n"]+["- "+c for c in CLAIMS]
md += ["\n## 2. Target audience\n", md_table(["Audience","Pain point Cozzipay solves"],[list(a) for a in AUD])]
md += ["\n## 3. Ideal customer profile (ICP)\n", ICP_DEF, "\n**Segments in priority order**\n"]
md += [f"{n}. {s}" for n,s in SEG]
md += ["\n**Buyer titles**\n"]+["- "+t for t in TITLES]
md += ["\n**Fit signals**\n"]+["- "+t for t in SIGNALS]
md += ["\n**Risk note**\n", RISK]
md += ["\n## 4. Reusable research prompt\n","Give the text below to a research-capable AI.\n","```text",PROMPT.strip(),"```"]
md += ["\n## 5. The 50 platforms\n","> "+DISC+"\n", md_table(HDR,list(rows()))]
md += ["\n## 6. Outreach copy\n", md_table(["Segment","Subject","Body","Use for"],[[a,b,c,d] for a,b,c,d in EMAILS])]
md += ["\n**LinkedIn connection note (under 300 characters)**\n","> "+LI,"\n**Follow-up (3-4 days later)**\n","> "+FU,"\n**Note:** "+NOTE]
open("/projects/sandbox/cozzipay/cozzipay-icp-and-research-prompt.md","w").write("\n".join(md)+"\n")

# ---------- DOCX ----------
d = Document()
sec = d.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = sec.page_height, sec.page_width
for m in ("left_margin","right_margin","top_margin","bottom_margin"): setattr(sec,m,Inches(0.5))
d.styles["Normal"].font.name="Calibri"; d.styles["Normal"].font.size=Pt(10)

def shade(cell,color):
    tcPr=cell._tc.get_or_add_tcPr(); sh=OxmlElement("w:shd")
    sh.set(qn("w:val"),"clear"); sh.set(qn("w:fill"),color); tcPr.append(sh)
def repeat_header(row):
    trPr=row._tr.get_or_add_trPr(); e=OxmlElement("w:tblHeader"); e.set(qn("w:val"),"true"); trPr.append(e)
def table(h, data, widths, size=8):
    t=d.add_table(rows=1,cols=len(h)); t.style="Table Grid"; t.autofit=False
    for i,x in enumerate(h):
        c=t.rows[0].cells[i]; c.text=""; r=c.paragraphs[0].add_run(x); r.bold=True; r.font.size=Pt(size); shade(c,"D9E2F3")
    repeat_header(t.rows[0])
    for row in data:
        cells=t.add_row().cells
        for i,x in enumerate(row):
            cells[i].text=""; r=cells[i].paragraphs[0].add_run(x); r.font.size=Pt(size)
    for row in t.rows:
        for i,w in enumerate(widths): row.cells[i].width=Inches(w)
    return t

d.add_heading("Cozzipay: Target Platforms and Outreach Copy",0)
p=d.add_paragraph(); r=p.add_run(DISC); r.bold=True
d.add_heading("50 target platforms",1)
widths=[0.3,0.9,0.9,0.9,2.4,1.2,0.7,0.7,0.6,0.6,0.8]
table(HDR,list(rows()),widths,7)
d.add_paragraph()
d.add_paragraph("Compliance note: "+RISK)
d.add_page_break()
d.add_heading("Email copy",1)
table(["Segment","Subject","Body","Use for"],[list(e) for e in EMAILS],[1.5,1.7,5.0,1.8],8)
d.add_heading("LinkedIn connection note (under 300 characters)",2); d.add_paragraph(LI)
d.add_heading("Follow-up (3-4 days later)",2); d.add_paragraph(FU)
d.add_paragraph("Note: "+NOTE)
d.save("/projects/sandbox/cozzipay/cozzipay-target-platforms.docx")
print(len(LI))
