import sorting_algorithms
import numpy as np



menu_text = f"Welcome to the sorting algorithm visualizer. Select one of the following options: \n"
menu_text += f"1- Run a sorting algorithm\n"
menu_text += f"2- View the current list\n"
menu_text += f"3- Edit the list\n"
menu_text += f"4- Exit\n"



algo_text = f"Select one of the following algorithm to visualize \n"
algo_text+= f"1- Bubble sort \n"
algo_text+= f"2- Selection sort \n"
algo_text+= f"3- Insertion sort \n"
algo_text+= f"4- Quick sort \n"
algo_text+= f"5- Merge sort \n"
algo_text+= f"6- Cocktail shaker sort \n"
algo_text+= f"7- Stalin sort \n"
algo_text+= f"8- Drunk man sort \n"
algo_text+= f"9- Back to menu \n"





def menu(list):

    while True:

        try:
            response = int(input(menu_text))

            match (response):

                case (1):
                    select_algorithm(list)

                case (2):
                    print(f"Here is the current list \n{list}")

                case (3):
                    list = edit_list(list)
                    
                case (4):
                    break

        except:
            print(f"Invalid response, please try again")
        



    return



def select_algorithm(list):


    while (True):
        try:
            response = int(input(algo_text))
            copy_list = np.array(list)

            match (response):

                case (1):
                    sorting_algorithms.bubble_sort(copy_list)

                case (2):
                    sorting_algorithms.selection_sort(copy_list)

                case (3):
                    sorting_algorithms.insertion_sort(copy_list)

                case (4):
                    sorting_algorithms.quick_sort(copy_list)

                case (5):
                    sorting_algorithms.merge_sort(copy_list)

                case (6):
                    sorting_algorithms.cocktail_shaker_sort(copy_list)

                case (7):
                    sorting_algorithms.stalin_sort(copy_list)

                case (8):
                    sorting_algorithms.drunk_man_sort(copy_list)

                case (9):
                    break

        except:
            print(f"Invalid response, please try again")
    # end while


    return






def edit_list(list):

    print(f"The current list has {len(list)} elements: \n{list}\n")


    while (True):

        try:
            new_length = int(input("Write the number of elements of the new list\n"))
            list = np.array(np.random.randint(1, 250, new_length))

            print(f"Here is your new list \n{list}")
            break

        except:
            print("Entered an invalid number, please try again\n")
        
        

    return list






    

