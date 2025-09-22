# Program to count the number of notes in a given amount

def counter(amount):
    notes = [2000, 1000, 500, 100, 50, 10]
    note_count = {}

    for note in notes:
        if amount >= note:
            count = amount // note 
            amount = amount % note
            note_count[note] = count

    if amount != 0:
        print("Remaining amount that can't be converted into notes:", amount)
    return note_count

amt = 560
result = counter(amt)

print(f"Breakdown for {amt}:")
for note, count in result.items():
    print(f"{note} : {count}")
