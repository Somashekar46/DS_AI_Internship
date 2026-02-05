raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print("Raw Login Logs:")
print(raw_logs)
unique_users = set(raw_logs)
print("\nUnique Visitors:")
print(unique_users)
is_present = "ID05" in unique_users
print("\nIs ID05 a unique visitor?")
print(is_present)
print("\nCount Comparison:")
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))
