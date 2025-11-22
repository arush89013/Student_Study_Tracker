class Session:
    def __init__(self, subject, date, duration, breakminutes):
        self.subject=subject
        self.date=date
        self.duration_minutes=duration
        self.break_minutes=breakminutes

    def effectivestudy(self):
        return max(0,self.duration_minutes-self.break_minutes)

class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.sessions=[]

    def add_session(self,session):
        self.sessions.append(session)

    def tst(self):                                            #Total study time function
        return sum(s.effectivestudy() for s in self.sessions)

    def stbs(self):                                           #study time by subject function
        subj_time={}
        for s in self.sessions:
            subj_time[s.subject]=subj_time.get(s.subject,0)+s.effectivestudy()
        return subj_time

class Tracker:
    def __init__(self):
        self.users={}
        self.cu=None                                         #Current user

    def register(self,username,password):
        if username in self.users:
            print("Username already taken.")
            return False
        self.users[username]=User(username, password)
        print(f"User '{username}' registered.")
        return True

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password==password:
            self.cu=user
            print(f"Logged in as {username}.")
            return True
        print("Invalid login details.")
        return False

    def logout(self):
        if self.cu:
            print(f"Logged out {self.cu.username}.")
            self.cu=None

    def add_study_session(self):
        if not self.cu:
            print("Log in first.")
            return
        subject=input("Subject: ")
        date=input("Date (YYYY-MM-DD): ")
        try:
            duration=int(input("Duration (minutes): "))
            break_time=int(input("Break minutes: "))
        except ValueError:
            print("Please enter valid numbers.")
            return
        session = Session(subject, date, duration, break_time)
        self.cu.add_session(session)
        print("Session added.")

    def view_report(self):
        if not self.cu:
            print("Log in first.")
            return
        total=self.cu.tst()                                           #Calling tst function
        print(f"Total study time: {total} minutes")
        subj_times=self.cu.stbs()                                     #Calling stbs function
        print("Time by subject:")
        for subj, time in subj_times.items():
            print(f" {subj}: {time} minutes")

def main():
    t = Tracker()
    while True:
        if not t.cu:
            choice=input("\nChoose:\n1. Register\n2. Login\n3. Exit\n> ")
            if choice=='1':
                username=input("Username: ")
                password=input("Password: ")
                t.register(username, password)
            elif choice=='2':
                username=input("Username: ")
                password=input("Password: ")
                if t.login(username, password):
                    while True:
                        action=input("\nChoose:\n1. Add Study Session\n2. View Report\n3. Logout\n> ")
                        if action=='1':
                            t.add_study_session()
                        elif action=='2':
                            t.view_report()
                        elif action=='3':
                            t.logout()
                            break
                        else:
                            print("Invalid option.")
            elif choice=='3':
                print("Bye.")
                break
            else:
                print("Invalid choice.")
        else:
            # Should not reach here, user actions handled in inner loop
            pass

if __name__ == "__main__":
    main()
