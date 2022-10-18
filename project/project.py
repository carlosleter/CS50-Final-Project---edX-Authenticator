from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from csv import DictWriter, DictReader
from time import sleep
from webbrowser import open_new


def main():
    screen_login()
    screen_login()


# Function | Login
def screen_login():
    # screen
    global login
    login = Tk()
    login.title("Login | edX")
    login.geometry("490x560+700+220")
    login.resizable(width=FALSE, height=FALSE)
    try:
        # import images
        login.iconbitmap(default="icons/user.ico")
        login_background = PhotoImage(file="images/login_background.png")
        img_sign_in = PhotoImage(file="images/sign_in.png")
        img_register = PhotoImage(file="images/register.png")
        facebook = PhotoImage(file="icons/facebook.png")
        twitter = PhotoImage(file="icons/twitter.png")
        linkedin = PhotoImage(file="icons/linkedin.png")
        instagram = PhotoImage(file="icons/instagram.png")
        reddit = PhotoImage(file="icons/reddit.png")
    except TclError:
        print("File is Not Found")
        raise

    # label background
    Label(login, image=login_background).pack()

    # global variables for authenticator
    global username_verify, password_verify 
    username_verify, password_verify = StringVar(), StringVar()

    # entries
    entry_username = Entry(login, textvariable=username_verify, bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_username.place(width=392, height=37, x=49, y=311)
    entry_password = Entry(login, textvariable=password_verify, show="*", bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_password.place(width=392, height=37, x=49, y=377)

    # buttons
    bt_sign_in = Button(login, bd=1, image=img_sign_in, command=sign_in)
    bt_sign_in.place(width=85, height=40, x=259, y=442)
    bt_register = Button(login, bd=1, image=img_register, command=screen_register)
    bt_register.place(width=85, height=40, x=144, y=442)
    bt_facebook = Button(login, bd=0, image=facebook, command=link_facebook)
    bt_facebook.place(width=40, height=40, x=107, y=505)
    bt_twitter = Button(login, bd=0, image=twitter, command=link_twitter)
    bt_twitter.place(width=40, height=40, x=165, y=505)
    bt_linkedin = Button(login, bd=0, image=linkedin, command=link_linkedin)
    bt_linkedin.place(width=40, height=40, x=223, y=505)
    bt_instagram = Button(login, bd=0, image=instagram, command=link_instagram)
    bt_instagram.place(width=40, height=40, x=282, y=505)
    bt_reddit = Button(login, bd=0, image=reddit, command=link_reddit)
    bt_reddit.place(width=40, height=40, x=340, y=505)


    # show screen
    login.mainloop()


# Function | Register
def screen_register():
    login.destroy()
    sleep(0.3)
    global register
    register = Tk()
    register.title("Register | edX")
    register.geometry("490x560+700+220")
    register.resizable(width=FALSE, height=FALSE)

    try:
        # import images
        register_background = PhotoImage(file="images/register_background.png")
        img_create_an_account = PhotoImage(file="images/create_an_account.png")
    except TclError:
        raise

    # label background
    Label(register, image=register_background).pack()

    # global variables for create an account
    global name_info, username_info, email_info, password_info
    name_info, username_info, email_info, password_info = StringVar(), StringVar(), StringVar(), StringVar()

    # entries
    entry_name = Entry(register, textvariable=name_info, bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_name.place(width=392, height=37, x=49, y=216)
    entry_username = Entry(register, textvariable=username_info, bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_username.place(width=392, height=37, x=49, y=286)   
    entry_email = Entry(register, textvariable=email_info, bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_email.place(width=392, height=37, x=49, y=356)
    entry_password = Entry(register, textvariable=password_info, show="*", bd=2, font=("Canva Sans", 13), justify=LEFT)
    entry_password.place(width=392, height=37, x=49, y=426)

    # buttons
    bt_create_an_account = Button(register, bd=1, image=img_create_an_account, command=create_an_account)
    bt_create_an_account.place(width=160, height=40, x=165, y=495)

    # show screen
    register.mainloop()


# Function | create an account
def create_an_account():
    try:
        # get entries
        name, username, email, password_r = name_info.get(), username_info.get(), email_info.get(), password_info.get()

        if not name or not username or not email or not password_r:
            messagebox.showerror("Error", "Please, fill all the blank fields")
        else:
            # Writing datas in a file by DictWriter
            with open(f"users/{username}.csv", "w", newline="") as file:
                fieldnames = ["name", "username", "email", "password"]
                writer = DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({"name": name.title(), "username": username, "email": email, "password": password_r})
                messagebox.showinfo("Account", "The account was created successfully!")
                register.destroy()
    except NameError:
        raise


# Function | sign in
def sign_in():
    try:
        # get entries
        user, password = username_verify.get(), password_verify.get()
        str(user)

        # Reading datas in a file by DictReader
        with open(f"users/{user}.csv") as file:
            reader = DictReader(file)
            for row in reader:
                if user == row["username"] and password == row["password"]:
                    messagebox.showinfo("Login", "Welcome back, " + row["name"] + "!")
                    # show painel after sign in   
                    screen_painel()
                else:
                    messagebox.showerror("Error", "Invalid Password!")
    except FileNotFoundError:
        messagebox.showerror("Error", "This account is not registered!")
    except NameError:
        raise


# facebook edX
def link_facebook():
    open_new("http://www.facebook.com/EdxOnline")


# twitter edX
def link_twitter():
    open_new("https://twitter.com/edXOnline")


# linkedin edX
def link_linkedin():
    open_new("http://www.linkedin.com/company/edx")


# instagram edX
def link_instagram():
    open_new("https://www.instagram.com/edxonline/")


# reddit edX
def link_reddit():
    open_new("http://www.reddit.com/r/edx")


# Function | Painel
def screen_painel():
    login.destroy()
    sleep(0.3)
    global painel
    painel = Tk()
    painel.title("Painel")
    painel.geometry("490x560+700+220")
    painel.resizable(width=FALSE, height=FALSE)

    try:
    # import images
        cs50p = PhotoImage(file="images/cs50p.png")
        complete_course = PhotoImage(file="images/complete_course.png")
    except TclError:
        raise

    # labels
    img_label = Label(painel, image=cs50p)
    img_label.pack(ipadx=10, ipady=0)
    heading = Label(painel, text="CS50's Introduction to Programming \n with Python", font=("Canva Sans", 18, BOLD))
    heading.pack(ipadx=10, ipady=20)

    # buttons
    bt_complete_course = Button(painel, bd=2, image=complete_course, command=screen_celebration)
    bt_complete_course.place(width=300, height=50, x=95, y=440)

    #show screen
    painel.mainloop()


# Function | Congratulations
def screen_celebration():
    try:
        painel.destroy()
    except NameError:
        pass
    sleep(1)
    congrats = Tk()
    congrats.title("Congratulations! | CS50's Introduction to Programming with Python")
    congrats.geometry("490x560+700+220")
    congrats.resizable(width=FALSE, height=FALSE)

    try:
        # import gif
        congrats_img = PhotoImage(file="images/celebration.png")

        # Labels
        heading = Label(congrats, text="Congratulations!", font=("Canva Sans", 26, BOLD))
        heading.pack(ipadx=10, ipady=20)
        subheading = Label(congrats, text="You have completed your course.", font=("Canva Sans", 20))
        subheading.pack(ipadx=10, ipady=30)
        img_label = Label(congrats, image=congrats_img)
        img_label.pack(ipadx=10, ipady=40)
    except TclError:
        raise


    # show screen
    congrats.mainloop()


if __name__ == "__main__":
    main()
