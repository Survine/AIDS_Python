import time

input("Press Enter to start timing...")
start_time = time.time()

input("Press Enter to stop timing...")
end_time = time.time()

time_diff = end_time - start_time

# Print the time difference
print("Time difference:", time_diff, "seconds")
