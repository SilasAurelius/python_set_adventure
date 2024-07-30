"""
Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
"""
# I use empty strings just for spacing between the printed tasks for better readability.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Task 1 - Destinations that both airlines fly to.
s1 = our_routes.intersection(competitor_routes)
print("Common routes:", s1)

print()

# Task 2 - Destinations unique to your airline.
s2 = our_routes.difference(competitor_routes)
print("Unique routes to our airline:", s2)

print()

# Task 3 - Whether there are any destinations that neither airline shares.
s3 = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", s3)

print()