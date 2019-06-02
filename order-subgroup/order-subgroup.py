import sys

###########################################
###################ARGS####################
###########################################
inputNumber = int(sys.argv[1])

###########################################
###########ARGS CONTROL ERROR##############
##########################################
if inputNumber <= 0:
  print("{} must be > 0".format(inputNumber))
  sys.exit(0)

###########################################
##############FUNCTIONS####################
###########################################
def getElements(n):
  return list(range(1,n,1))

def getOrdre(groupN, element):
  for n in range(1,groupN,1):
    res = (element**n) % groupN
    if res == 1:
      return n
  return 0

def getSubgroup(groupN, element):
  subGroup = []
  index = 1
  for n in range(1,groupN,1):
    res = (element**n) % groupN
    if res not in subGroup:
      subGroup.append(res)
      index += 1
    else:
      return subGroup
  return subGroup

###########################################
###################MAIN####################
###########################################
elementsGroup = getElements(inputNumber)
print("Group generated is Z_{} with multiplicative function\n".format(inputNumber))
print("Elements of the group: {}\n".format(elementsGroup))

for element in elementsGroup:
  print("{}:".format(element))
  order = getOrdre(inputNumber, element)
  print(" - Order: {}".format(order))
  subGroup = getSubgroup(inputNumber, element)
  print(" - Subgroup generated: {}".format(subGroup)) 