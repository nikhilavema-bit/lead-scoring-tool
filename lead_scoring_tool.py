#Lead Scoring Tool

#Automatically scores and ranks incoming sales leads by priority (Hot/Warm/Cold)
#based on company size and stated budget, removing the need for manual triage.


# --- Step 1: Define the scoring rule ---
def score_lead(employee_count, budget):
    """Returns a priority tier for a lead based on company size and budget."""
    if budget >= 50000 and employee_count >= 200:
        return "Hot"
    elif budget >= 10000:
        return "Warm"
    else:
        return "Cold"


# --- Step 2: Sample lead data (in production, this would come from a CRM export or API) ---
leads = [
    {"company": "Acme Corp", "employee_count": 5, "budget": 500},
    {"company": "Globex Inc", "employee_count": 200, "budget": 25000},
    {"company": "Initech", "employee_count": 3000, "budget": 150000},
    {"company": "Umbrella Co", "employee_count": 50, "budget": 8000},
    {"company": "Wayne Ent.", "employee_count": 400, "budget": 60000},
    {"company": "Stark Industries", "employee_count": 1000, "budget": 90000},
    {"company": "Hooli", "employee_count": 30, "budget": 12000},
    {"company": "Pied Piper", "employee_count": 10, "budget": 200},
    {"company": "Soylent Corp", "employee_count": 150, "budget": 4000},
    {"company": "Cyberdyne Systems", "employee_count": 2, "budget": 100},
]


# --- Step 3: Score every lead ---
for lead in leads:
    lead["tier"] = score_lead(lead["employee_count"], lead["budget"])


# --- Step 4: Rank leads — Hot first, then Warm, then Cold; ties broken by budget (highest first) ---
tier_rank = {"Hot": 0, "Warm": 1, "Cold": 2}
sorted_leads = sorted(
    leads,
    key=lambda lead: (tier_rank[lead["tier"]], -lead["budget"])
)


# --- Step 5: Output the prioritized call list ---
print("=== Prioritized Lead List ===")
for lead in sorted_leads:
    print(f'{lead["company"]:<20} {lead["tier"]:<6} budget: ${lead["budget"]:,}')
