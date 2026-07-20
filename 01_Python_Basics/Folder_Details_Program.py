import os

directory = "/projects"  # current directory; change to any path you want

for item in os.listdir(directory):
    print(item)