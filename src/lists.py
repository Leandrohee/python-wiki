#LIST
list_example: list[any] = [44, "apple, 3.14", True]
list_example[0]                                 # return the first element: 44
list_example.append("new item")                 # add a new item


#ARRAYS
import array
array_integer = array.array("i", [1,2,3,4])
array_string = ["leandro","rafael","felipe"]
array_integer[2]                                # return the third element: 3
array_string[1]                                 # return the second element: "rafael"


#ARRAYS WITH NUMPY
import numpy as np
array_integer_np = np.array([10,20,30,40])
array_integer_np[2]

#OBJECTS (dict)
person_dict: dict[str, any] = {
    "name": "leandro",
    "age": 30,
    "profession": "firefighter"
}
person_dict["name"]                             # return "leandro"
person_dict["age"]                             # return 25


#DICT INSIDE A LIST
list_dict: list[dict[str, any]] = [
    {
        "name": "leandro",
        "age": 30,
        "profession": "firefighter"
    },
    {
        "name": "rafael",
        "age": 27,
        "profession": "engennier"
    },
    {
        "name": "felipe",
        "age": 19,
        "profession": "student"
    },
]
print(list_dict[0]["name"])