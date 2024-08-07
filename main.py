#list sorting by using while https://github.com/Gemechu-7/Python-project-1.git
numbers=[30, 4, 6, 77, 0, 9, 22, 11]
count = 0
numbers_list =[]
max_number =numbers[0]
while count < len(numbers):
    numbers_list = numbers[count]
    count+=1
    if numbers_list > max_number:
        max_number = numbers_list
print(max_number)