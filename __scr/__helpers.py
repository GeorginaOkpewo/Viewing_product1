
class UserInfo:
    import csv
   
    #create a class with object of the header
    def __init__(self, User_id, Title, Age, Monthly_number_of_hours_watched):
        self.User_id = User_id
        self.Title = Title
        self.Age = Age
        self.Monthly_number_of_hours_watched = Monthly_number_of_hours_watched
        
    #create the string method
    def __repr__(self):
        return f"UserInfo({self.User_id!r}, {self.Title!r},{self.Age!r}, {self.Monthly_number_of_hours_watched!r})"
     #convert the UserInfo object to tuple   
    def __iter__(self):
        return iter([self.User_id, self.Title, self.Age, self.Monthly_number_of_hours_watched])
        
     #Create a list  
User = [
   UserInfo (1, "Ms", 45, 670.0),
   UserInfo(2, "Mr", 30, 550),
   UserInfo(4, "Mrs", 60, 400),
    ]
    
with open("info.csv", "w") as stream:
   writer = csv.writer(stream)
   writer.writerows(User)

