# ---------------- append() ------------------
list =[1,2,3];
list.append(4);
print(list);

# ---------------- sort() ------------------
list2 =[2,1,3];
print(list2)
print(list2.sort());
print(list2);
print(list2.sort(reverse=True));
print(list2);


# ---------------- sort() character ------------------
fruits=['banana', 'litchi', 'apple'];
print(fruits.sort());
print(fruits);

# ---------------- reverse() ------------------
letters=['a', 'b', 'r', 'd', 'f'];
letters.reverse();
print(letters);

# ---------------- insert(index, element) ------------------
numbers=[1,2,3,4];
numbers.insert(1,5);
print(numbers);

# ---------------- remove() ------------------
shopping_list = ["asif", "eggs", "milk"]
shopping_list.remove("asif")

print(shopping_list)
# Output: ['eggs', 'milk']

# ---------------- pop() ------------------
todo = ["clean room", "call mom", "cook dinner"]

# Remove the last item and save it
finished_task = todo.pop()

print(todo)
# Output: ['clean room', 'call mom']

print(finished_task)
# Output: cook dinner


# ---------------- count() ------------------
answers = ["Yes", "No", "Yes", "Yes", "No"]
print(answers.count("Yes"));