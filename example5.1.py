data_lst = ['From abhinavbansal349@gmail.com Sat Jan  5 09:14:16 2020', 'From f20191293@hyderabad.bits-pilani.ac.in Fri March  5 09:20:43 2019', 'From abhinav@gmail.com']

for item in data_lst:
    pos1 = item.find(' ')
    # print(pos1)

    pos2 = item.find('@')
    # print(pos2)

    user_name = item[pos1+1:pos2]
    print(user_name)




