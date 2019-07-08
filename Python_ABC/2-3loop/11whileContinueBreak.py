# ---------- BREAK AND CONTINUE ----------
# Continue stops executing the code that remains in the loop and
# jumps back to the top

# Break jumps completely out of the loop

i = 1

while i <= 20:

    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue

    # If i equals 15 stop looping
    if i == 15:
        break

    # Print the odds
    print("Odd : ", i)

    # Increment i
    i += 1