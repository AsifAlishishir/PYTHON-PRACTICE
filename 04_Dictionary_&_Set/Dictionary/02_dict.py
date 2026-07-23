marks={
    "Harry":100,
    "Shubham":56,
    "Rohan":26,
    0:"Asif"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99,"Sadia":98})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])