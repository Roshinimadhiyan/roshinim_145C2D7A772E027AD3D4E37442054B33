def linearsearchproduct(productList,targetproduct):
  indices = []

  for index,product in enumerate(productList):
   if product == targetproduct:
    indices.append(index)

   return indices


# Example usage:
Products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result =   linearsearchproduct(Products,target )
print(result)