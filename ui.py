from main import EnergyData

def getting_started():
    global empty_str
    empty_str = ""
    user_input = input("Welcome to Energy Generation Tracker. Choose an action (i.e. a):\n"
    "a) Get country's electricity generation mix in TWh over time\n" 
    "b) Get generation mix percentage for one country\n"
    "c) Get generation mix percentage for multiple countries\n"
    "d) Export country's energy mix data in TWh to Excel\n"
    "e) Export country's energy mix data in TWh to PostgreSQL db\n"
    "Type 'Exit' to quit\n")

    if user_input == "a":
        return option_a()

    if user_input == "b":
        result = option_b()
        if result == None:
            return empty_str
        else:
            return result

    if user_input == "c":
        a = EnergyData('default_country')
        result = a.compare_countries()
        if result == None:
            return empty_str
        else:
            return result

    if user_input == "d":
        result = option_d()
        if result == None:
            return empty_str
        else:
            return result

    if user_input == "e":
        result = option_e()
        if result == None:
            return empty_str
        else:
            return result
        
    if user_input == "Exit":
        return empty_str

    else: 
        return "The action was not found."
        
# functions handling user options
        
def option_a():
        print("You can choose the country and the time range for the statistics.")
        user_quit = False

        while True:
            country = input("Insert country:\n")
            a = EnergyData(country)
            if a.valid_country() == False:
                print(f"No values found for '{country}'. Please try again.")
                choice = input("Type 'quit' to exit or press Enter to try again: \n")
                if choice.lower() == 'quit':
                    user_quit = True
                    break
            else:
                break
        
        if user_quit == False:
            while True:
                try:
                    start_year = int(input("Insert the first year:\n"))
                    last_year = int(input("Insert the last year:\n"))
                    if start_year < 1985 or last_year > 2022:
                        raise ValueError
                    return a.histdata(start_year, last_year)
                except ValueError:
                    print("The data is available between 1985 and 2022.")
        else:
            return empty_str

def option_b():
    user_quit = False

    while True:
        country = input("Insert country:\n")
        a = EnergyData(country)
        if not a.valid_country():
            print(f"No values found for {country}. Please try again.")
            choice = input("Type 'quit' to exit or press Enter to try again: \n")
            if choice.lower() == 'quit':
                user_quit = True
                break
        else:
            break

    if user_quit == False:
        while True:
            try:
                start_year = int(input("Insert the year:\n"))
                last_year = start_year
                if start_year < 1985 or last_year > 2022:
                    raise ValueError
                result = a.get_the_share(country, start_year)
                print(result)

                while True:
                    user_input_level3 = input("Do you want to check another year for the same country? (Yes or No)\n")
                    if user_input_level3.lower() == "yes":
                        start_year = int(input("Insert a different year.\n"))
                        result = a.get_the_share(country, start_year)
                        print(result)
                    elif user_input_level3.lower() == "no":
                        return 
            except ValueError:
                print("The data is available between 1985 and 2022.")
        else:
            return empty_str

def option_d():
    user_quit = False

    while True:
        country = input("Insert country:\n")
        a = EnergyData(country)
        if a.valid_country() == False:
            print(f"No values found for {country}. Please try again.")
            choice = input("Type 'quit' to exit or press Enter to try again: \n")
            if choice.lower() == 'quit':
                user_quit = True
                break
        else:
            break

    if user_quit == False:
        while True:
            try:
                start_year = int(input("Insert the first year:\n"))
                last_year = int(input("Insert the last year:\n"))
                if start_year < 1985 or last_year > 2022:
                    raise ValueError
                return a.export_to_excel(start_year, last_year, country)
            except ValueError:
                print("The data is available between 1985 and 2022.")
    else:
        return empty_str

def option_e():
        user_quit = False
        user_input_level2 = input("Choose an action:\n"
        "a) Create a table in PostgreSQL\n"
        "b) Fill in the data to an existing table in PostgreSQL\n"
        "c) Delete the table in PostgreSQL\n")

        if user_input_level2 == "a":
            while True:
                table_name = input("Type in the table name (without spaces):\n")
                country = input("Insert country:\n")
                a = EnergyData(country)
                if a.valid_country() == False:
                    print(f"No values found for {country}. Please try again.")
                    choice = input("Type 'quit' to exit or press Enter to try again: \n")
                    if choice.lower() == 'quit':
                        user_quit = True
                        break
                    else:
                        break

            if user_quit == False:
                while True:
                    try:
                        start_year = int(input("Insert the first year:\n"))
                        last_year = int(input("Insert the last year:\n"))
                        if start_year < 1985 or last_year > 2022:
                            raise ValueError
                        result = a.create_a_table(table_name, start_year, last_year)
                        user_input_level3 = input("Do you want to add the data? (Yes or No)\n")
                        if user_input_level3.lower() == "yes":
                            result = a.add_data_to_a_table(table_name, start_year, last_year)
                            return result
                        if user_input_level3.lower() == "no":
                            return "OK, now you just have an empty table."
                    except ValueError:
                        print("The data is available between 1985 and 2022.") 
            else:
                return empty_str    

        if user_input_level2 == "b":
            while True:
                table_name = input("Type in the table name (without spaces). The table should already exist!:\n")
                country = input("Insert country:\n")
                a = EnergyData(country)
                if a.valid_country() == False:
                    print(f"No values found for {country}. Please try again.")
                    choice = input("Type 'quit' to exit or press Enter to try again: \n")
                    if choice.lower() == 'quit':
                        user_quit = True
                        break
                    else:
                        break

            if user_quit == False:
                while True:
                    try:
                        start_year = int(input("Insert the first year:\n"))
                        last_year = int(input("Insert the last year:\n"))
                        if start_year < 1985 or last_year > 2022:
                            raise ValueError
                        result = a.add_data_to_a_table(table_name, start_year, last_year)
                        return result
                    except ValueError:
                        print("The data is available between 1985 and 2022.")
            else:
                return empty_str 

        if user_input_level2 == "c":
            while True:
                table_name = input("Type in the table name (without spaces). The table should already exist!:\n")
                country = input("Insert country:\n")
                a = EnergyData(country)
                if a.valid_country() == False:
                    print(f"No values found for {country}. Please try again.")
                    choice = input("Type 'quit' to exit or press Enter to try again: \n")
                    if choice.lower() == 'quit':
                        user_quit = True
                        break
                    else:
                        break  

            if user_quit == False:
                while True:
                    try:
                        start_year = int(input("Insert the first year:\n"))
                        last_year = int(input("Insert the last year:\n"))
                        if start_year < 1985 or last_year > 2022:
                            raise ValueError
                        result = a.delete_the_table(table_name)
                        return result
                    except ValueError:
                        print("The data is available between 1985 and 2022.")  
            else:
                return empty_str 
                
        else:
            return "The action was not found."   
        
       
print(getting_started())