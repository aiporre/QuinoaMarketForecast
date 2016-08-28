notes = []
for i in range(0,11):
    for j in range(0,11):
        notes.append(30 * (0.5*(i+j)/10))
print sorted(notes)