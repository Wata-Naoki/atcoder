
s=list(input())
t=list(input())
st=set()
for i in range(len(s)):
    k=(ord(t[i])-ord(s[i]) + 26) % 26
    st.add(k)

if len(st) == 1:
    print('Yes')
else:   
    print('No')