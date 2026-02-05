friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b
print("Shared Interests:")
print(shared_interests)
print("\nAll Interests:")
print(all_interests)
print("\nInterests Unique to Friend A:")
print(unique_to_a)