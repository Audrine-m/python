<<<<<<< HEAD

names=input("James, John, Joan")
# convert the input string into a list of names
names_list=[name.strip()for name in names.split(",")]
# remove duplicates
unique_names_list=list(set(names_list))
# sort in alphabetic order
sorted_names_list=sorted(unique_names_list)
#count
total_names=len(names_list)
print("Total number of names entered:", total_names)
print("Sorted list of unique names:",sorted_names_list)
=======

names=input("James, John, Joan")
# convert the input string into a list of names
names_list=[name.strip()for name in names.split(",")]
# remove duplicates
unique_names_list=list(set(names_list))
# sort in alphabetic order
sorted_names_list=sorted(unique_names_list)
#count
total_names=len(names_list)
print("Total number of names entered:", total_names)
print("Sorted list of unique names:",sorted_names_list)
>>>>>>> a838971ed257ecd7c0284abc69d99cd3f52561fa
