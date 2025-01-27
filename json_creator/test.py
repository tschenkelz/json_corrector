import re

mystr = '{"hello": "my-friend", "hello2": "my friend, abc", "field asdf asdf": True, "nxt":"hello:what", "nxt2": Mystr, "test": {"na":hallo}}'
regex = r'([^\w"]+(?:"[^"]*"[^\w"]*)*)([^"\W]+)'

repl = r'\1"\2"'

#test = re.findall(regex,mystr,re.M)
#test = re.findall(regex,mystr)
# for i in test:
#     print(i)
#print(test)

sub = re.sub(regex,repl,mystr,flags=re.M)
print(f"orig:\n{mystr}\nadjusted:\n{sub}")
# for i in sub:
#     print(sub)