import pickle
import os

def front_semi_truck():
    # definition path for current catalog of script
    catalog_path = os.path.dirname(os.path.abspath(__file__))

    # definition path for data in same catalog
    data_path = os.path.join(catalog_path, 'dictionary.pkl')

    command = "start"
    while command != "2":

        command = input("1.start or overwrite last values\n2.exit and calculate\n3.print "
                        "dictionary of values\n>")
        if command == "1":
            # set up conditional
            dmc = ["dmc", 0, "dmc - total mass of semitrailer?"]
            Rd_max = ["Rd_max", 0, "Rd_max - what is total load of axes semitrailer [kg]?"]
            Rb_max = ["Rb_max", 0, "Rb_max - what is  maximium  load of motion axes [kg]?"]
            Rb_min = ["Rb_min", 0, "Rb_min - what is  minium procentage of total mass on motion axes [%]?"]
            Xc = ["Xc", 0, "Xc - distance between motion axes and king pin[mm]?"]
            Qs = ["Qs", 0, "Qs - load of body [kg]?"]
            Xs = ["Xs", 0, "Xs position load of body [mm]?"]
            Qr = ["Qr", 0, "Qr - load of fame (without axes) [kg]?"]
            Xr = ["Xr", 0, "Xr - position load of fame (without axes) [mm]?"]
            Qz = ["Qz", 0, "Qz - load of suspension [kg]?"]
            Xz = ["Xz", 0, "Xz - position load of suspension [mm]?"]
            Qa = ["Qa", 0, "Qa - load of first axe truck unit without load[kg]?"]
            Xa = ["Xa", 0, "Xa - position of first axe truck unit [mm]?"]
            Qb = ["Qb", 0, "Qb - load of motion axes truck unit without load [kg]?"]
            # list of questions
            questions = [dmc, Rd_max, Rb_max, Rb_min, Xc, Qs, Xs, Qr, Xr, Qz, Xz, Qa, Xa, Qb]
            # list of answers
            dictionary = {}
            # defult cmmand
            command = "start"
            # for by row in questions (matrix 2d)
            for row in questions:
                # for by cell in questions of row (matrix 1d)
                for element in row[2:3]:
                    # set condition and reset after loop condition to false
                    condition = False
                    # when user input value as int, loop will be pass
                    while condition == False:
                        # try becouse if user input str it will be error
                        try:
                            # show question in cmd
                            print(element)
                            # ask about value
                            command = input("write command \n>")
                            # if user input exit, loop break
                            if command == "exit":
                                break
                            # if user input int, int will be add to list, and loop will be pass
                            elif type(int(command)) == int:
                                dictionary[row[0]] = command
                                condition = True
                                # if user input difrent value then int
                        except ValueError:
                            print("value must be intiger!")
                # similar like above
                if command == "exit":
                    break
            # save data
            with open(data_path, 'wb') as plik:
                pickle.dump(dictionary, plik)
        elif command == "3":
            #except error
            try:
                # Load dictionary from file
                with open(data_path, 'rb') as plik:
                    dictionary = pickle.load(plik)
                print(dictionary)
            #if couldun t find data
            except FileNotFoundError:
                print("data 'dictionary.pkl' doesn't exist.")