#RegEx-regular expression

import re
x="vineeth123" 
if re.search("[a-z]",x):
    print("verified")
else:
    print("not verified")
print(re.search("[a-z]",x))
print(re.findall("[a-z]",x)) 

# email id format checking 

a="abc123@gmail.com"
if re.search("[a-z]",a):
    if re.search("[1-9]",a):
       if re.search("^[a-z]",a):
            if re.search("@gmail.com$",a):
               print("verified")
            else:
                print("not verified")
       else:
           print("not verified")     
    else:
        print("not verified")             
else:
    print("not verified") 