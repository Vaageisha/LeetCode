# '.' means current directory
#'..' means previous directory 
# for example: home/file, where file(.) is current directory and home(..) is the parent directory
#our output path should contain "/" ; "/" also would seprate two directories; should not end with "/"

"""Dry run:
string= "/.././///home//food" --> just traversing through string
string[i]="/" --->continue
*/../--> belongs to a directory(as it in enclosed between to forward slashes)

a= variable storing values enclosed between forward slashes
if(a==".."); and stack is not empty then POP from the stack to reach our current directory.
elif(a==".")  we can simply comntinue
elif(a=="home") we will PUSH and just continue
/+/= /
"""
class Solution:
    def simplifyPath(self, path: str) -> str:

        # Initialize a stack
        stack = []

        #Split the input string on "/" as the delimiter
        #and process each portion one by one
        
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
                
             else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str    
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str
               
