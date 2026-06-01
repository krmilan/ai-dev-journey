# Reading files - foundational for RAG

def read_contacts(filename):
    contacts = []
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()             # Remove leading/trailing whitespace/newlines
            if line:                        # Skip empty lines
                print(f"RAW LINE: {line}")
                parts = line.split(",")     # Split by comma
                print(f"AFTER SPLIT: {parts}")
                contact = {
                    "name": parts[0].strip(),
                    "email": parts[1].strip(),
                    "city": parts[2].strip()
                }
                contacts.append(contact)
    return contacts

# Process the contacts and print them
contacts = read_contacts("sample.txt")

for contact in contacts:
    print(f"Name: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"City: {contact['city']}\n")
    print("-" * 30)                         # Separator for readability
    