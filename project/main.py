import PySimpleGUI as sg

user = []

sg.theme('DarkAmber')

layoutReg = [[[sg.Text("Enter the username you want to use: ")], sg.InputText(key=1)],
            [[sg.Text("Enter the password you want to use: ")], sg.InputText(key=2)],
            [[sg.Button("REGISTER"), sg.Button("EXIT")]]]

windowReg = sg.Window("Registration Panel", layoutReg)

def login_panel():

    sg.theme('DarkAmber')

    layout =    [[sg.Text('Enter your username: '), sg.InputText(key=1)],
                [[sg.Text('Enter your password: '), sg.InputText(key=2)],
                [sg.OK(), sg.Cancel()]]]

    window = sg.Window('Login Client', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if values[1] == user[0] and values[2] == user[1]:
            print("You have successfully logged in!")
            window.close()
            user_panel()
        else:
            print("You have entered wrong username or password!")
            break

def user_panel():
    sg.theme('DarkAmber')

    layouts = [[[sg.Text("Welcome, "+user[0])]], [[sg.Text("That's your user panel.")], sg.Button("End Session")]]

    windows = sg.Window("User Panel", layouts)

    while True:
        events, values2 = windows.read()
        if events in (sg.WIN_CLOSED, 'End Session'):
            break

    windows.close()

while True:
    eventReg, values3 = windowReg.read()
    if eventReg in (sg.WIN_CLOSED, 'EXIT'):
        break
    if eventReg in ('REGISTER'):
        user.append(values3[1])
        user.append(values3[2])
        print("You have successfully registered. Redirecting to login page...")
        windowReg.close()
        login_panel()