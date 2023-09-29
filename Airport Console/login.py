users=[]

def user2str(user):
    return "|".join([user['username'],user['password'],user['ime'],user['prezime'],user['radnomesto']])

def str2user(line):
        username,password,ime,prezime,radnomesto=line.strip('\n').split('|')
        user={
             'username':username,
             'password':password,
             'ime':ime,
             'prezime':prezime,
             'radnomesto':radnomesto,
             
        }
        return user

def loadusers():
    for line in open('users.txt','r').readlines():
        if len(line) > 1:
            user = str2user(line)
            users.append(user)
    return users        

def login(username,password,users):
    for user in users:
        if user['password']==password and user['username']==username:
            return user
    return False

