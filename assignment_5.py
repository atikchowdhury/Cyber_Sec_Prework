def large(names_list):
    longest_name=''
    for name in names_list:
        if(len(name)>len(longest_name)):
            longest_name=name
        else:
            pass
    return longest_name

names_list=["bob","jimmy","max b","bernie","jordan","future hendrix"]
big_name=large(names_list)
print("largest name is ",big_name)
