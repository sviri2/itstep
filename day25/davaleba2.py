#Ex.2 (3 points)
# Take string as an input.this will be our word.you have to do the following steps:
# 1.Reverse the given string
# 2.change every character in the reversed string with +3 unicode in the ascii table('a' will become 'd',because chr(ord('a') +3)) is 'd' )
# 3.Reverse the result again and print it



# Ex: computer --> frpsxwhu
# cipher coding --> flskhu#frglqj
# jujutsu --> mxmxwvx

str = input()
rvs = str[::-1]
ret= ""
for ch in rvs:
    ret += chr(ord(ch)+3)
    ret = ret[::-1]
    print(ret)