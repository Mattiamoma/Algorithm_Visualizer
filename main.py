import cmd_menu 
import numpy as np


if __name__ == "__main__":
    
    amount = 50
    unsorted_list = np.random.randint(1, 250, amount)

    cmd_menu.menu(unsorted_list)