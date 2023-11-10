import copy


my_list = [1, 3, 5, 2, 7, 9, 10, 12, 20]
my_list = my_list + my_list

result = []
for item in my_list:
    if item % 2 == 0:
        result.append(item)

print(result)

# list
res = [x - 2 for x in my_list if x % 2 == 0]
print(res)

# set
res = {x - 2 for x in my_list if x % 2 == 0}
print(res)

# dict
res_lst = [x - 2 for x in my_list if x % 2 == 0]
print(res_lst)
res_tup = tuple(res_lst)
print(res_tup)

res_dict = {x: chr(x) for x in my_list if x % 2 == 0}
print(res_dict)
res_dict = {x: x * 2 for x in my_list if x % 2 == 0}
print(res_dict)

# generator
res_gen = (x - 2 for x in my_list if x % 2 == 0)
print(res_gen)
# print(*res_gen)

res_gen_0 = [str(x) for x in res_gen]
print(f"string list: {res_gen_0}")
res_gen_1 = ", ".join(res_gen_0)
print(f"joined: {res_gen_1}")

res_gen = (x - 2 for x in my_list if x % 2 == 0)
res_gen_2 = ""
for i in res_gen:
    res_gen_2 += f", {i}"
print(f"for: {res_gen_2}")

print(f"range:")
print(*range(10))
