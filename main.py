"""Collect names, then demonstrate list and string methods."""
names = []
while True:
    name = input("Enter a name (or press Enter to finish): ").strip()
    if not name:
        break
    names.append(name.title())

print("Names:", names)
print("Sorted:", sorted(names))
print("Number of names:", len(names))
if names:
    search = input("Name to search for: ").strip().casefold()
    matches = [item for item in names if item.casefold() == search]
    print("Found" if matches else "Not found")

sentence = input("Enter a sentence: ").strip()
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Words:", sentence.split())
print("Character count (without outer spaces):", len(sentence))
