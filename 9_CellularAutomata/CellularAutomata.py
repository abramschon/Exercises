import matplotlib.pyplot as plt

def main():
    rule = 150
    explain_rule(rule)
    init_row = [0 for i in range(101)]
    init_row[51] = 1
    CA = CellularAutomata(rule,init_row,100)
    visualise_grid(CA.grid)

class CellularAutomata:
    def __init__(self, 
                 rule_no=10, 
                 init_row=[0,0,1,0,0], 
                 n_steps=5):
        self.rule_no = rule_no
        self.map = get_binary_array(rule_no)
        self.grid = [init_row]
        self.n_steps = n_steps
        #define numpy array of zeros and update based on map
        self.evolve()

    

    def evolve(self):
        """
            Updates a row 
        """
        n = len(self.grid[0]) #no of units per row

        for t in range(self.n_steps):
            new_row = []
            for j in range(n):
                i = (j-1)%n
                k = (j+1)%n
                new_row.append(
                    self.map[
                        get_base_10(
                            self.grid[t][i],
                            self.grid[t][j],
                            self.grid[t][k]
                        )
                    ]
                )
            self.grid.append(new_row)


def get_base_10(i,j,k):
    return i*4 + j*2 + k

def get_binary_array(n):
    """
        Takes in base 10 numbers and creates a base 2 representation as an array of 0s and 1s
        args:
            n: int base 10 number
        returns: 
            array of ints
    """
    map = []
    twos = 2**7
    while twos>=1:
        if n>=twos:
            print()
            map.insert(0,1)
            n-=twos
            twos/=2
        else:
            map.insert(0,0)
            twos/=2
    return map

def explain_rule(n):
    print("Rule",n)
    print("Configuration:  111 110 101 100 011 010 001 000")
    map = get_binary_array(n)
    print(f"Maps to:         {map[7]}   {map[6]}   {map[5]}   {map[4]}   {map[3]}   {map[2]}   {map[1]}   {map[0]} ")

def visualise_grid(grid):
    plt.imshow(grid)
    plt.show()

if __name__=="__main__":
    main()