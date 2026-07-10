student={
    "name": "asif ali",
    "subjects": {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

# ------------------- dict.keys() ---------------------
# print(student.keys());
# print(list(student.keys()));

# ------------------- dict.values() ---------------------
# print(list(student.values()));


# ------------------- dict.items() ---------------------
# print(list(student.items()));


# ------------------- dict.get() ---------------------
print(student.get("subjects"));

# ------------------- dict.update() ---------------------
new_dict={"city" : "dhaka", "age": 15};
student.update(new_dict);
print(student);
