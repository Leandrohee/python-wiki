#Simple loop with number 1 to 5
for i in range(1,6):
   i                              # 1-2-3-4-5

#Simple loop with numbers 0 to 4
for i in range(5):
    i                            # 0-1-2-3-4

#Loop with an list
list1 = ["arroz", "banana", "feijao"]
for food in list1:
   i                              # "arroz"-"banana"-"feijao"

#Loop over a string
word = "leandro"
for letter in word:
   letter                          # l-e-a-n-d-r-o

#Loop with while
num = 1
while num <= 5:
    num
    num += 1

#Loop with a break
for num in range(10):
    # print(num)
    num                              # 0-1-2-3-4
    if num == 5:
        break

#Getting the index of an list 
list_example = [10,20,30,40,50]
for index, item in enumerate(list_example):
    # print(f"the item {index} is {item}")
    item



