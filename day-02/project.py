def read_contacts(filename):
    contacts = []
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                contacts.append({
                    "name": parts[0].strip(),
                    "email": parts[1].strip(),
                    "city": parts[2].strip()
                })
    return contacts

def generate_summary(contacts):
    cities =[]
    for contact in contacts:
        cities.append(contact["city"])
        
    summary ={
        "total_contacts": len(contacts),
        "cities": cities,
        "names": [c["name"] for c in contacts] # List comprehension to extract names
    }
    return summary

def display_report(contacts, summary):
    print("=" * 40)
    print("     CONTACT REPORT")
    print("=" * 40)
    print(f"Total Contacts: {summary['total_contacts']}")
    print(f"Cities: {', '.join(summary['cities'])}")
    print()
    
    for contact in contacts:
        print(f" {contact['name']} | {contact['email']} | {contact['city']}")
    
    print("=" * 40)
    
# Main execution
contacts = read_contacts("sample.txt")
print(contacts,"\n")  # Debugging: Print the contacts list to verify it's read correctly
summary = generate_summary(contacts)
print(summary,"\n")  # Debugging: Print the summary to verify it's generated correctly
display_report(contacts, summary)
