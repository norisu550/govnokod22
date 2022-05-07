import re
import os


for root, dir, files in os.walk("/НАЧАЛО ДЕРЕВА/"):
    for name in files:
        if re.search(".html",name):
            fullname = os.path.join(root,name)
            #print(fullname)
            with open(fullname, "r") as f:
                s = f.read()
                s = re.sub("ТО ЧТО НАХУЙ","1",s)
            os.remove(fullname)
            with open(f'{fullname}',"a") as f:
                f.write(s1)

