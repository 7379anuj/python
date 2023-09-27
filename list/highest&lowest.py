l=[24,34,90,45,56,78]
highest=0
lowest=l[0]
for item in l:
    print(item)
    if item>highest:
        highest=item
    if item<lowest:
        lowest=item
print("highest is:",highest)
print("lowest is:",lowest)