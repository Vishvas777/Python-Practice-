for i in range (100):
    if (i==43):
        break
        print(i)

# The loop will iterate over the range object created by range(100), which generates numbers starting from 0 up to (but not including) 100
# When the loop variable i reaches 43, the break statement will be executed, causing the
for i in range (100):
    if (i==43):
        continue
    print(i) #loop to terminate immediately when i is 43, and the continue statement will skip the rest of the loop body for that iteration and move on to the next iteration of the loop.