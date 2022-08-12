#PART 1

import regex as re #importing regex module 
import json #importing json module

#saving the variable
txt = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHPWarning #2] count(): Parameter must be an array or an object that implements Countable(153)"}]}

#saving the ids in a list
lst = txt["orders"]
#appending the error code with the above list
code = str(txt["errors"][0])
lst.append(code.split(",")[0])
# print(lst)

for i in lst:
    s = json.dumps(i) #converting each dict to string
    x= re.search(r":(.*)", s) #searching values after ":"
    print(x.group(1).strip("},\"")) #grouping the index returned by search and striping "}" and "
