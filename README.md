# lead-scoring-tool
Python script that auto-scores and prioritizes sales leads

# Lead Scoring Tool

Automates lead triage for sales teams — scores and ranks incoming leads by 
priority in place of manual spreadsheet review.

## The Problem

When new leads land — from a web form, a trade show list, or an outbound 
campaign , [Lead Scoring Tool.py](https://github.com/user-attachments/files/29952453/Lead.Scoring.Tool.py)
someone on the sales or ops team has to manually review each one 
and decide who to call first. For a small batch this is manageable; for 
50-200 leads, it can eat 30-45 minutes of someone's day, and the prioritization 
is inconsistent from person to person and day to day. This kind of manual 
triage is exactly the type of GTM bottleneck automation is built to remove.

## The System

A Python script that:
1. Scores every lead as **Hot**, **Warm**, or **Cold** using fixed business 
   rules based on company size and budget
2. Automatically ranks the full list so the highest-priority leads surface 
   first, with ties broken by budget size
3. Applies the exact same logic to every lead, every time — removing the 
   inconsistency of manual judgment calls

### Core logic

python
def score_lead(employee_count, budget):
    if budget >= 50000 and employee_count >= 200:
        return "Hot"
    elif budget >= 10000:
        return "Warm"
    else:
        return "Cold"

tier_rank = {"Hot": 0, "Warm": 1, "Cold": 2}
sorted_leads = sorted(leads, key=lambda lead: (tier_rank[lead["tier"]], -lead["budget"]))

## The Outcome

Manually sorting 10 leads into priority order took me 4-5 minutes — roughly 
24-30 seconds per lead. The script does the same job in under a second. 
Scaled to a realistic batch of 100 leads, that's 40-50 minutes of manual 
triage work eliminated per batch, with zero inconsistency between runs.

## Tech Stack

- **Python** — core scoring and ranking logic
- Built-in `sorted()` with a custom `lambda` key function for multi-tier, 
  multi-field ranking

## Example Output

=== Prioritized Lead List ===
Initech              Hot    budget: $150,000
Stark Industries     Hot    budget: $90,000
Wayne Ent.           Hot    budget: $60,000
Globex Inc           Warm   budget: $25,000
Hooli                Warm   budget: $12,000
Umbrella Co          Cold   budget: $8,000
Soylent Corp         Cold   budget: $4,000
Acme Corp            Cold   budget: $500
Pied Piper           Cold   budget: $200
Cyberdyne Systems    Cold   budget: $100

## About This Project

Built as part of a hands-on GTM engineering curriculum. Drawing on my prior 
experience as a Customer Operations Engineer at HighRadius — where I 
configured automated rules for enterprise finance workflows — this project 
applies the same "define the rule once, apply it consistently at scale" 
principle to a sales/GTM use case.

## What's Next

- Read leads from a live CSV export instead of a hardcoded list
- Connect directly to a CRM (HubSpot) so scoring runs automatically on new 
  lead creation
- Add additional scoring dimensions (industry fit, engagement signals)
