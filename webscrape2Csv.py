file = open(r"C:\Users\Thetj\CLionProjects\GuessingGame\stats\lists.txt", "w")
print("Beginning...")
for i in range(3000):
    add = str(i)
    file.write(add)
    file.write("\n")
    print("Added")
file.close()
print("Complete")
