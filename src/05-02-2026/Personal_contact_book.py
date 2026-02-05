contacts = {
    "Soma": "9876543210",
    "Darshan": "9123456789",
    "Suraj": "9988776655"
}
contacts["Abhi"] = "9001122334"
contacts["Darshan"] = "9111111111"
print("Lookup Existing Contact:")
print("Soma:", contacts.get("Soma", "Contact not found"))

print("\nLookup Non-Existing Contact:")
print("Eve:", contacts.get("Eve", "Contact not found"))
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
