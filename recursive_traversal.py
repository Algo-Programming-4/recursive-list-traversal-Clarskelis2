nested_list = [1, [2, 3], [[4], [5, [6, 7]]], 8]

def Recursion_of_lists(List, Total, Items, Recursions, MaxDepth):
  Recursions += 1
  Depth = 0
  for i in range(len(List)):
    Items += 1
    if type(List[i]) == list:
        Total,Items,Recursions,Depth,MaxDepth = Recursion_of_lists(List[i], Total, Items, Recursions, MaxDepth)
        Depth += 1
    else:
      Total += List[i]
    if Depth < MaxDepth:
            Depth = MaxDepth
  return Total, Items, Recursions, Depth, Depth

print("Total:", Recursion_of_lists(nested_list, 0, 0, 0, 0)[0], "\nTotal Items:", Recursion_of_lists(nested_list, 0, 0, 0, 0)[1], "\nRecursions:", Recursion_of_lists(nested_list, 0, 0, 0, 0)[2], "\nMax Depth:", Recursion_of_lists(nested_list, 0, 0, 0, 0)[3])