# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))

# 1 2 3 4 1 2 3 4 5 6
new_list = []
key = 0
while len(new_list) < length_of_circular_linked_list and key < len(circular_linked_list):
    element = circular_linked_list[key]
    if element not in new_list:
        new_list.append(element)
    key += 1
print(len(new_list))
for i in new_list:
    print(i , end = " ")
