def separate(names_list):
  even_names_list = list()
  odd_names_list = list()
  for i in range(len(names_list)):
      if(len(names_list[i])%2 == 0):
            even_names_list.append(names_list[i])
      else:
            odd_names_list.append(names_list[i])

      for i in range(len(even_names_list)):
        name = even_names_list[i]
        name = "b" + name[1:]
        even_names_list[i] = name

      for i in range(len(odd_names_list)):
        name = odd_names_list[i]
        name = name[:-1] + "c"
        odd_names_list[i] = name
      print("even-lettered list:",even_names_list)
      print("odd-lettered list:",odd_names_list)

      return even_names_list
names_list = ["bob","jimmy","max b","bernie","jordan","future hendrix"]

even_lettered_list = separate(names_list)
print("even-lettered list:",even_lettered_list)
