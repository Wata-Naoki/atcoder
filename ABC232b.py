
s=list(input())
t=list(input())
st=set()
for i in range(len(s)):
    # ordのaは97で、zは122
    # 26で足して26で割った余りをとることで、zからaに戻ることを考慮する
    k=(ord(t[i])-ord(s[i]) + 26) % 26
    st.add(k)

# 全ての距離が等しければ、Yes
if len(st) == 1:
    print('Yes')
else:   
    print('No')