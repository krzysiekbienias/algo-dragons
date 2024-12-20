def one_name_check(username):
    username_list=list(username)
    for i in range(len(username_list)):
        for j in range(i+1,len(username_list)):
            username_list[i],username_list[j]=username_list[j],username_list[i]
            if ''.join(username_list)<username:
                return 'YES'
            username_list[i],username_list[j]=username_list[j],username_list[i]
    return 'NO'




if __name__=='__main__':

    print('fuck')
    print(min('a','k'))
    #print(possibleChanges(usernames='foo'))