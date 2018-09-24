class Person(object):
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting = 0

    def greet (self,other_person):
        print("Hello {0}, I am{1}!".format(other_person.name,self.name))
        self.greeting = self.greeting + 1

    def print_contact_info(self,):
        print (self.name + "email:" + self.email + " " + self.name +"phone" + self.phone)

    def add_friend(self,other_person):
        return self.friends.append(other_person)

    def num_friends(self):
        print(f"Numbers of friends {len(self.friends)}")

    def __repr__(self):
        return ("{0} {1} {2}".format(self.name,self.email,self.phone))


sonny = Person("sonny", "sonny@yahoo.com", "483-485-4948")
jordan = Person("jordan","jordan@aol.com","495-586-3456")

sonny.greet(jordan)
sonny.print_contact_info()
sonny.add_friend(jordan)
sonny.num_friends()
