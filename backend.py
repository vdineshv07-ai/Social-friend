class FriendsGraph:
    def __init__(self):
        self.friends = {}
    
    def add_friend(self, user, friend):
        if user not in self.friends:
            self.friends[user] = []
        if friend not in self.friends:
            self.friends[friend] = []
        
        if friend not in self.friends[user]:
            self.friends[user].append(friend)
        if user not in self.friends[friend]:
            self.friends[friend].append(user)
    
    def get_friends(self, user):
        return self.friends.get(user, [])
    
    def get_graph(self):
        return self.friends
