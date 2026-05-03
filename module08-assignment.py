# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 95,
    "AI Solutions": 250
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "NorthStar Retail",
    "contact_person": "Emma Carter",
    "email": "emma@northstarretail.com",
    "phone": "604-555-1001"
}

customer2 = {
    "company_name": "BlueWave Finance",
    "contact_person": "Daniel Lee",
    "email": "daniel@bluewavefinance.com",
    "phone": "604-555-1002"
}

customer3 = {
    "company_name": "GreenLeaf Health",
    "contact_person": "Sophia Patel",
    "email": "sophia@greenleafhealth.com",
    "phone": "604-555-1003"
}

customer4 = {
    "company_name": "SkyBridge Logistics",
    "contact_person": "Michael Chen",
    "email": "michael@skybridgelogistics.com",
    "phone": "604-555-1004"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for customer_id, info in customers.items():
    print(f"{customer_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Info:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "604-555-9001"
customers["C002"]["industry"] = "Financial Services"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
projects = {
    "C001": [
        {"name": "E-Commerce Website", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Help Desk Setup", "service": "IT Support", "hours": 60, "budget": 5700}
    ],
    "C002": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 80, "budget": 17600},
        {"name": "Data Dashboard", "service": "Data Analysis", "hours": 90, "budget": 15750}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 100, "budget": 20000}
    ],
    "C004": [
        {"name": "AI Chatbot", "service": "AI Solutions", "hours": 70, "budget": 17500},
        {"name": "Website Upgrade", "service": "Web Development", "hours": 50, "budget": 7500}
    ]
}

print("\n\nProject Information:")
print("-" * 60)
for customer_id, project_list in projects.items():
    print(customer_id)
    for project in project_list:
        print(f"  {project}")

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)
for customer_id, project_list in projects.items():
    for project in project_list:
        cost = services[project["service"]] * project["hours"]
        print(f"{customer_id} - {project['name']}: ${cost}")

# TODO 9: Customer statistics using dictionary methods
customer_ids = list(customers.keys())
customer_companies = [info["company_name"] for info in customers.values()]
total_customers = len(customers)

print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", customer_ids)
print("Customer Companies:", customer_companies)
print("Total Customers:", total_customers)

# TODO 10: Service usage analysis
service_counts = {}
for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
all_projects = [project for project_list in projects.values() for project in project_list]
all_hours = [project["hours"] for project in all_projects]
all_budgets = [project["budget"] for project in all_projects]

total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

most_expensive_project = max(all_projects, key=lambda project: project["budget"])
least_expensive_project = min(all_projects, key=lambda project: project["budget"])

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Project Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)
print("Most Expensive Project:", most_expensive_project["name"], "-", most_expensive_project["budget"])
print("Least Expensive Project:", least_expensive_project["name"], "-", least_expensive_project["budget"])

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)
for customer_id, info in customers.items():
    customer_projects = projects.get(customer_id, [])
    customer_hours = sum(project["hours"] for project in customer_projects)
    customer_total_budget = sum(project["budget"] for project in customer_projects)
    print(f"{customer_id} - {info['company_name']}")
    print(f"  Contact: {info['contact_person']}")
    print(f"  Projects: {len(customer_projects)}")
    print(f"  Total Hours: {customer_hours}")
    print(f"  Total Budget: ${customer_total_budget}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate}")

# TODO 14: Filter customers using dictionary comprehension
active_customers = {customer_id: info for customer_id, info in customers.items() if projects.get(customer_id)}

print("\n\nActive Customers (with projects):")
print("-" * 60)
for customer_id, info in active_customers.items():
    print(f"{customer_id}: {info['company_name']}")

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {
    customer_id: sum(project["budget"] for project in project_list)
    for customer_id, project_list in projects.items()
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
for customer_id, budget in customer_budgets.items():
    print(f"{customer_id}: ${budget}")

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or customer_dict[field] == "":
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)
for customer_id, info in customers.items():
    print(f"{customer_id}: {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
status_cycle = ["active", "completed", "pending"]
status_counts = {}

index = 0
for project_list in projects.values():
    for project in project_list:
        project["status"] = status_cycle[index % len(status_cycle)]
        status = project["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
        index += 1

print("\n\nProject Status Summary:")
print("-" * 60)
for status, count in status_counts.items():
    print(f"{status}: {count}")

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    budget_analysis = {}
    for customer_id, project_list in projects_dict.items():
        total = sum(project["budget"] for project in project_list)
        count = len(project_list)
        average = total / count if count > 0 else 0
        budget_analysis[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }
    return budget_analysis

budget_analysis = analyze_customer_budgets(projects)

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
for customer_id, stats in budget_analysis.items():
    print(f"{customer_id}: {stats}")

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    customer_projects = projects.get(customer_id, [])
    used_services = []
    for project in customer_projects:
        if project["service"] not in used_services:
            used_services.append(project["service"])

    unused_services = []
    for service in services:
        if service not in used_services:
            unused_services.append(service)

    if not customer_projects:
        return unused_services[:3]

    avg_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)
    recommendations = []

    for service in unused_services:
        estimated_cost = services[service] * 80
        if estimated_cost <= avg_budget:
            recommendations.append(service)

    if not recommendations:
        recommendations = unused_services[:2]

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)
for customer_id in customers:
    recommendations = recommend_services(customer_id, customers, projects, services)
    print(f"{customer_id}: {recommendations}")
