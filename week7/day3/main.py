# list = [1, 2, 3]
#
#
# def our_sum(*args):
#     sum_var = 0
#     for num in args:
#         sum_var += num
#     return sum_var
#
#
# print(our_sum(*list))
#
#
# # res=sum(list)
# # print(res)
#
#
# def sum_only_numbers(*args):
#     sum_lst = 0
#     for arg in args:
#         try:
#             sum_lst += arg
#         except:
#             pass
#     return sum_lst
#
#
#
#
#
# my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
# print(sum_only_numbers(*my_list))


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# print(list(map(filter(lambda person: len(person)>=4,people),people)))


filterd=list(filter(lambda person: len(person)<5, people))
print(list(map(lambda person: f"hello {person}",filterd)))



# # ----------------------------------------------------------------
#
# people_names_less_than_5 = list(filter(lambda people: len(people) < 5, peoples))
# print(list(map(lambda people: f"hello {people}", people_names_less_than_5)))
#
# # ----------------------------------------------------------------
# print(list(map(lambda people: f"hello {people}", list(filter(lambda people: len(people) < 5, peoples)))))