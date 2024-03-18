import numpy as np
import matplotlib.pyplot as plt
import random

background_color = "black"
default_color = "white"
active_color = "#00FF00"
interaction_color = "red"
index_color = "#4AE6FF"
title_size = 30
figure_size = (18,11)




def bubble_sort(list):

    length = len(list)
    title = f"Bubble sort"


    x = np.arange(0, length, 1)
    plt.figure(figsize = figure_size, facecolor = background_color)
    last = length - 1
    for i in range(length):
        
        #keep an array of colors to know in which positions there was a swap access at the end of every for(j)

        colors = [default_color]*length
        colors[0] = active_color

        

        #active color is used to keep track of the position j which alwways starts from 0

        swapped = False

        for j in range(0, last):

            bar_list = plt.bar(x, list,color = colors)
            plt.title(title, color = default_color, fontsize = title_size)

            plt.axis(False)

            plt.pause(0.01)

            if(list[j] > list[j+1]):

                colors[j] = interaction_color
                colors[j+1] = active_color
                swapped = True

                last_swap = j

                #set interaction color to see which position was swapped 
                 
                var = list[j]
                list[j] = list[j+1]
                list[j+1] = var
                

            else:
                colors[j] = default_color
                colors[j+1] = active_color

            plt.clf()
        
        if (swapped == False):
            break

        last = last_swap

    final_transition(list, length, title)

    return





def selection_sort(list):

    length = len(list)


    title = f"Selection sort"

    plt.figure(figsize = figure_size, facecolor = background_color)

    x = np.arange(0, length, 1)

    for i in range(length):
        
        min = i
        bar_list = plt.bar(x, list, color = default_color)
        plt.title(title, color = default_color, fontsize = title_size)
        
        
        plt.axis(False)


        
        for j in range(i+1, length):

            #active color keeps track of the index that needs to be swapped at the end of every cicle and the current min position found

            bar_list[i].set_color(active_color)
            
            #interaction color is used to show in which position there was a swap

            bar_list[j].set_color(interaction_color)
            plt.pause(0.01)

            if(list[j]<list[min]):
                bar_list[j].set_color(active_color)
                bar_list[min].set_color(interaction_color)
                
                min = j

            else:

                #if there was no swap reset to default color 

                bar_list[j].set_color(default_color)

            plt.pause(0.01)

        plt.clf()



        var = list[min]
        list[min] = list[i]
        list[i] = var

        #update chart after swap

        bar_list = plt.bar(x, list, color = default_color)
        plt.title(title, color = default_color, fontsize = title_size)
        plt.axis(False)

        plt.pause(0.01)
        plt.clf()
    
    final_transition(list, length, title)
    
    
    return



def drunk_man_sort(list):

    #swap 2 elements and check if the list is sorted
    #repeat until the list isn't sorted


    length = len(list)

    plt.figure(figsize = figure_size, facecolor = background_color)

    x = np.arange(0, length, 1)

    is_sorted = False

    while(is_sorted == False):
    
        bar_list = plt.bar(x, list, color = default_color)
        plt.axis(False)
        
        
        i = random.randint(0, length-1)
        j = random.randint(0, length-1)

        bar_list[i].set_color("yellow")
        bar_list[j].set_color("yellow")

        plt.pause(0.05)
        plt.clf()

        var = list[i]
        list[i] = list[j]
        list[j] = var
        is_sorted = True

        bar_list = plt.bar(x, list, color = default_color)
        plt.axis(False)
        plt.pause(0.02)


        for i in range(length-1):

            bar_list[i].set_color(active_color)
            plt.pause(0.05)

            if (list[i] > list[i+1]):

                bar_list[i+1].set_color(interaction_color)
                plt.pause(0.05)
                is_sorted = False
                plt.clf()
                break

    bar_list[length-1].set_color(active_color)
    plt.pause(0.01)
    plt.show()
    

    return





def insertion_sort(list):
    
    length = len(list)
    title = f"Insertion sort"
    x = np.arange(0, length, 1)
    plt.figure(figsize = figure_size, facecolor = background_color)


    for i in range(1, length):


        var = list[i]
        j = i-1

        while (j >= 0 and list[j] > var):

            plt.clf()
            
            list[j+1] = list[j]
            list[j] = var

            #update the chart after every swap
            bar_list = plt.bar(x, list, color = default_color)
            plt.axis(False)
            plt.title(title, color = default_color, fontsize = title_size)

            #highlight the positions swapped

            bar_list[i].set_color(active_color)
            bar_list[j].set_color(interaction_color)
            bar_list[j+1].set_color(interaction_color)
            plt.pause(0.02)


            j = j-1

            #highlight the next interaction
            bar_list[j].set_color(interaction_color)
            plt.pause(0.01)
     
        plt.clf()
    
    
    final_transition(list, length, title)
    
    
    return









def quick_sort(list):

    title = f"Quick sort"
    low = 0
    high = len(list) - 1

    plt.figure(figsize = figure_size, facecolor = background_color)

    quick_sort_sorting(list, low, high, title)

    final_transition(list, high+1, title) 

    return



def quick_sort_sorting(list, low, high, title):

    
    x = np.arange(0, len(list), 1)
    
    
    bar_list = plt.bar(x, list, color = default_color)
    plt.title(title, color = default_color, fontsize = title_size)
    plt.axis(False)

    #active color is set to the pivot of the sublist
    bar_list[high].set_color(active_color)
    plt.pause(0.02)

    if(low < high):

        pivot = list[high]
        j = low - 1
        for i in range(low, high+1):

            if(list[i] <= pivot):

                
                j = j + 1

                #highlight the items in positions i and j

                bar_list[i].set_color(interaction_color)
                bar_list[j].set_color(interaction_color)
                plt.pause(0.02)

                if (i > j):

                    var = list[i]
                    list[i] = list[j]
                    list[j] = var 

                    #update chart after swap

                    plt.clf()
                    bar_list = plt.bar(x, list, color = default_color)
                    plt.title(title, color = default_color, fontsize = title_size)
                    plt.axis(False)
                    bar_list[high].set_color(active_color)
                    plt.pause(0.02)

                else:

                    #reset color to default because there wasn't any access to the array positions

                    bar_list[i].set_color(default_color)
                    bar_list[j].set_color(default_color)

                    plt.pause(0.02)

                    

        
        plt.clf()
        quick_sort_sorting(list, low, j-1, title)
        quick_sort_sorting(list, j+1, high, title) 
    
    plt.clf()
    
    

    return








def cocktail_shaker_sort(list):  #bubble sort that goes both ways

    plt.figure(figsize = figure_size, facecolor = background_color)

    length = len(list)

    title = f"Cocktail shaker sort"

    x = np.arange(0, len(list), 1)
    count_i = length - 1
    count_j = 0
    last_swap_i = 0
    last_swap_j = 0
    swapped = True

    
    while (swapped == True):

        swapped = False

        colors = [default_color] * length
        colors[count_j] = active_color

        for i in range(count_j, count_i):

            bar_list = plt.bar(x, list, color = colors)
            plt.title(title, color = default_color, fontsize = title_size)
            plt.axis(False)
            plt.pause(0.01)

            if(list[i] > list[i+1]):

                var = list[i]
                list[i] = list[i+1]
                list[i+1] = var
                colors[i] = interaction_color
                colors[i+1] = active_color


                swapped = True
                last_swap_i = i
            
            else:
                colors[i] = default_color
                colors[i+1] = active_color
            
            plt.clf()
        
        count_i = last_swap_i

        if (swapped == False):
            break
        
        swapped = False
        colors = [default_color] * length
        colors[count_i] = active_color

        for j in range(count_i, count_j, -1):

            bar_list = plt.bar(x, list, color = colors)
            plt.title(title, color = default_color, fontsize = title_size)
            plt.axis(False)
            plt.pause(0.01)

            if(list[j] < list[j-1]):

                var = list[j]
                list[j] = list[j-1]
                list[j-1] = var

                colors[j] = interaction_color
                colors[j-1] = active_color
                swapped = True
                last_swap_j = j


            else:
                colors[j] = default_color
                colors[j-1] = active_color

            plt.clf()
        count_j = last_swap_j

    final_transition(list, length, title)



    return






def stalin_sort(list):

    #just delete any element that is not in order

    title = f"Stalin sort"
    i = 1
    plt.figure(figsize = figure_size, facecolor = background_color)

    while (i < len(list)):

        x = np.arange(0, len(list), 1)
        bar_list = plt.bar(x, list, color = default_color)
        plt.axis(False)
        plt.title(title, color = default_color, fontsize = title_size)
        bar_list[i].set_color(active_color)

        plt.pause(0.01)

        plt.clf()

         
        if (list[i] < list[i-1]):
            list = np.delete(list, i)

        else:

            i = i+1 

    final_transition(list, len(list), title)

    return list




def merge_sort(list):

    plt.figure(figsize = figure_size, facecolor = background_color)

    low = 0
    length = len(list)
    high = length - 1
    title = f"Merge sort"

    merge_sort_sorting(list, low, high)

    final_transition(list, length, title)


    return

def merge_sort_sorting(list, low, high, title = f"Merge sort"):


    x = np.arange(0, len(list), 1)

    if (low < high):

        half = int((low + high) / 2)

        #split the list in 2 parts
        list1 = merge_sort_sorting(list, half + 1, high)
        list2 = merge_sort_sorting(list, low, half)

        i = 0
        j = 0
        k = low

        #merge the 2 sorted lists

        while(i < len(list1) and j < len(list2)):

            bar_list = plt.bar(x, list, color = default_color)
            plt.axis(False)
            plt.title(title, color = default_color, fontsize = title_size)
            bar_list[high].set_color(active_color)
            bar_list[low].set_color(active_color)
            bar_list[low + j].set_color(index_color)
            bar_list[half + i].set_color(index_color)
            bar_list[k].set_color(interaction_color)

            plt.pause(0.02)
            plt.clf()

            if (list1[i] < list2[j]):

                list[k] = list1[i]
                i = i + 1 
            
            else:

                list[k] = list2[j]
                j = j + 1

            k = k + 1

        while(i < len(list1)):

            bar_list = plt.bar(x, list, color = default_color)
            plt.axis(False)
            plt.title(title, color = default_color, fontsize = title_size)
            bar_list[high].set_color(active_color)
            bar_list[low].set_color(active_color)
            bar_list[low + j].set_color(index_color)
            bar_list[half + i].set_color(index_color)
            bar_list[k].set_color(interaction_color)

            plt.pause(0.02)
            plt.clf()

            list[k] = list1[i]
            i = i + 1
            k = k + 1

            
          
        while(j < len(list2)):

            bar_list = plt.bar(x, list, color = default_color)
            plt.axis(False)
            plt.title(title, color = default_color, fontsize = title_size)
            bar_list[high].set_color(active_color)
            bar_list[low].set_color(active_color)
            bar_list[low + j].set_color(index_color)
            bar_list[half + i].set_color(index_color)
            bar_list[k].set_color(interaction_color)

            plt.pause(0.02)
            plt.clf()

            list[k] = list2[j]
            j = j + 1
            k = k + 1
        
    #if low = high return the array with one element to merge it with the other half
    
    #if low < high returns the merged array
            
    return np.array(list[low:high+1])






def final_transition(list, length, title):

    x = np.arange(0, length, 1)

    bar_list = plt.bar(x, list, color = default_color)
    plt.axis(False)
    plt.title(title, color = default_color, fontsize = title_size)

    for i in range(0, length-1):

        bar_list[i].set_color(active_color)
        bar_list[i+1].set_color(interaction_color)
        plt.pause(0.01)

    bar_list[length-1].set_color(active_color)
    plt.pause(0.01)
    
    
    plt.pause(5)
    plt.close()

    return


