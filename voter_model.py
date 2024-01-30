import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation


def initial_state(v, N):
    """initial state

    Args:
        N (int): number of lattice
        v (int): number of vote

    Returns:
        array: initial state
    """
    lattice = np.random.choice(range(v),(N,N))
    return lattice


def checkflip(r, c, lattice, p , N):
    """check the vote is flip or not

    Args:
        r (int): rth row
        c (int): cth column
        lattice (2d_array): lattice
        p (float): probability of fliping
        N (int): number of lattice
    """
    def bc(i):
        """periodic boundry condition"""
        if i > N-1:
            return 0
        if i < 0:
            return N-1
        else:
            return i
        
    choice = np.random.choice(["up", "down", "right", "left", "upright", "upleft", "downright", "downleft"])
    
    if np.random.random() < p:
        
        if choice == "up":
            lattice[r][bc(c+1)] = lattice[r][c]

        elif choice == "down":
           lattice[r][bc(c-1)] = lattice[r][c]

        elif choice == "right":
            lattice[bc(r+1)][c] = lattice[r][c]

        elif choice == "left":
            lattice[bc(r-1)][c] = lattice[r][c]

        elif choice == "upright":
           lattice[bc(r+1)][bc(c+1)] = lattice[r][c]

        elif choice == "upleft":
            lattice[bc(r-1)][bc(c+1)] = lattice[r][c]

        elif choice == "downright":
            lattice[bc(r+1)][bc(c-1)] = lattice[r][c]
        
        else:
            lattice[bc(r-1)][bc(c-1)] = lattice[r][c]

    return lattice
 
def magnetization(lattice , N):
    """find the number of maximum vote

    Args:
        lattice (2d_array): lattice
        N (int): number of lattice
    """

    def CountFrequency(my_list):
        """counr frequency of the list

        Args:
            my_list (list):

        Returns:
            dictinary: a dictionary that keys keys are items in list and its values are frequency of items
        """
        freq = {}
        for item in my_list:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

    lattice = lattice.reshape(N*N).tolist()
    mag = CountFrequency(lattice)
    return dict(sorted(mag.items()))


def step(lattice, N, p, nstep):
    """simluate voter model

    Args:
        lattice (2d_array): lattice
        N (int): number of lattice
        p (float): probability of flipping
        nstep (int): number of simlulation steps

    Returns:
        2d_array: lattice after eqSteps 
    """
    for _ in range(nstep):
        for j in range(0, N**2):
                            
            row = np.random.randint(0, N)
            col = np.random.randint(0, N) 
            lattice = checkflip(row, col, lattice, p, N)

    return lattice





if __name__ == "__main__":

    vote = 8  ##number of vote
    N = 32  ##number of lattice
    p = 0.3 ##the probability of accepting flipping

    lattice = initial_state(vote, N)

    fig = plt.figure(figsize=(7,7))
    ax = plt.axes()
    cmap= "cubehelix"
    
    sns.heatmap(lattice, cmap=cmap, cbar=False, yticklabels=False, xticklabels=False, vmin = 0, vmax = vote)
    ax.set_title(magnetization(lattice, N))
    plt.savefig("initial_state_voter_model")

    def animate(i):
        sns.heatmap(step(lattice, N , p, i), cmap=cmap, cbar=False, yticklabels=False, xticklabels=False, vmin = 0, vmax = vote)
        ax.set_title(magnetization(lattice, N))
        if i in [20, 40, 60, 80, 100]:
            plt.savefig(f"{i}frame_of_voter_model")

    anim = animation.FuncAnimation(fig, animate, frames=120, repeat=False)
    f = r"/home/mohaddeseh/Documents/Programing/Stochastic/voter_model.mp4" 
    writervideo = animation.FFMpegWriter(fps=10) 
    anim.save(f, writer=writervideo)

    plt.savefig("last_state_voter_model")
