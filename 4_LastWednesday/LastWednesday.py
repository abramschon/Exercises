import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

#       j   f   m   a   m   j   j   a   s   0   n   d
days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],   #non leap year days 
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]   #leap year days

def main():
    year_day_matrix, no_wed, no_last_wed = mark_days()
    print("Total Wednesdays:",no_wed)
    print("Wednesdays at end of month:", no_last_wed ) 
    print("Prop. of Wed. at end of month:", float(no_last_wed/no_wed) )

    visualise_matrix(year_day_matrix)

def visualise_matrix(matrix):
    plt.rcParams["font.family"] = "futura"
    colours = np.array([[1,1,1,0],         #transparent  - background
                        [1,0.2,0.4,0.5],   #red    - wednesdays
                        [0.2,0.3,1,0.5],   #blue   - end of month
                        [0.2,0,0.2,1]])    #purple - both    
    newcmap = ListedColormap(colours)
    plt.imshow(matrix, cmap=newcmap)
    plt.title("Wednesdays at the end of the month")
    plt.xlabel("Day")
    plt.ylabel("Years since 2001",rotation=0,labelpad=40)
    plt.show()
    
def mark_days():
    #matrix to of the days of each year of the 21st Century 
    #mark as 1 for wednesday, 2 for end of month, 3 for both
    year_day_matrix = np.zeros( (100,366), dtype=int) 
    
    cumul_days = 1                 #an overall counter of how many days have passed
    leap = False                   #whether leap year or now
    month_ind = 0                  #index of which month we are on
    next_month_end = days[leap][0] #day of the next month end 
    next_wed = 3                   #day of the next wednesday

    no_wed = 0                     #count wednesdays
    no_last_wed = 0                #count last wednesdays


    for i in range(100): #iterate through years

        year = 2001 + i     #which year we are in  
        
        #set days in year based on whether is leap year
        leap = False
        no_days=365
        if ( (year%4==0) and (year%100!=0) ): #(don't need to check whether year divisible by 400 since no year in [2001,2100] is)
            leap = True
            no_days=366

        for day in range(no_days): #iterate through days
            if cumul_days == next_wed: #its a wednesday

                next_wed += 7   #set next wed to a week's time
                no_wed += 1     #increment wednesday counter

                if cumul_days == next_month_end:            #also the end of the month
                    month_ind = (month_ind + 1) % 12        #move index to next month
                    next_month_end += days[leap][month_ind] #set next month end 

                    year_day_matrix[i,day] = 3  #mark as both
                    no_last_wed += 1            #incremenet last wednesday counter
                    
                else:
                    year_day_matrix[i,day] = 1 #mark as wednesday
            
            elif cumul_days == next_month_end: #just the end of the month
                month_ind = (month_ind + 1) % 12        #move index to next month
                next_month_end += days[leap][month_ind] #set next month end  

                year_day_matrix[i,day] = 2 #mark as end of month
            
            cumul_days += 1 #a day goes by
                

    return (year_day_matrix, no_wed, no_last_wed)

if __name__ == "__main__":
    main()