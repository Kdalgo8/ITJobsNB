CATEGORIES = {
    "Software Developer / Engineer": [
        "software", "developer", "engineer", "full stack",
        "backend", "frontend", "python", "java", "c#", "javascript"
    ],
    "IT Support / Helpdesk": [
        "helpdesk", "service desk", "it support",
        "technical support", "desktop support"
    ],
    "Data / Analytics": [
        "data", "analytics", "bi", "business intelligence",
        "sql", "power bi", "machine learning"
    ],
    "Networking and Infrastructure": [
        "network", "infrastructure", "systems",
        "cloud", "azure", "aws", "devops", "linux"
    ]
}

def categorize(title, summary):
    text = f"{title} {summary}".lower()
    for category, keywords in CATEGORIES.items():
        if any(k in text for k in keywords):
            return category
    return "All IT Jobs"
