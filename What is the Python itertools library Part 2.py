# https://www.youtube.com/watch?v=gopeM1_aAM4
# What is the Python itertools library? 
# Part 2 in a series.
# import the liberay.
import itertools
# Create some easy data to use.  
# It's 'flat' data, not nested.
data = ["fish",
        "cow",
        "dog",
        "elk",
        "zebra",
        "gnu",
        "cat"]
# Batch it into
#  sets of two elements...
# The batched function steps
#  through our data, 
#  creating tuples.
batches = itertools.batched(data, 2)
print("Our batches:")
print(f"batches is of type {type(batches)}")
# Convert it to a list
# so we can see the contents.
# It's a list of tuples!
batches = list(batches)
print(batches)
print(f"batches is of type {type(batches)}")
print(f"batches[0] is of type {type(batches[0])}")
# A use case for 
#  batching is
#  dispersing data to multiple
#  processes. Each process
#  can work on a batch of data.
print("Processing our batches:")
for batch in batches:
    # This is our processing step. 
    # In this example, 
    #  we just print the batch.
    print(f"batch: {batch}")
