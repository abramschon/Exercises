# Find the largest palindromic substring using Manchester's algorithm
# Source for code: https://en.wikipedia.org/wiki/Longest_palindromic_substring 

#%%
import numpy as np

s = input("Enter lots of palindromes.")
sep_s = "|".join(s) #seperate each chacter in s with | so we don't have to deal with even length palindromes

N = len(sep_s) #length
max_radii = [0 for i in range(N)] # store 'radius' of the longest palindrome centered at each character in sep_s

center = 0 
radius = 0

while center<N:
    # find longest palindrome centered at 'center' 
    while center-(radius+1) >= 0 and center+(radius+1) < N and ( sep_s[center-(radius+1)] == sep_s[center+(radius+1)] ):
        radius += 1       
    max_radii[center] = radius # record the radius 
    
    # since palindromes are symmetric, any palindromes p_sub within a palindrome p_big have a counterpart p_sub' reflected across the center of p_sub
    # we can thus use the alrady calcuated radius of any p_sub for p_sub', provided me are within a larger palindrome p_big.

    old_center = center
    old_radius = radius
    center += 1
    radius = 0
    while center <= old_center + old_radius: # check whether we are within a larger palindrome
        mirrored_center = old_center - (center - old_center)
        max_mirrored_radius = old_center + old_radius - center 
        if max_radii[mirrored_center] < max_mirrored_radius: # then we have p_sub completely contained in p_big, and p_sub' = p_sub
            max_radii[center] = max_radii[mirrored_center]
            center += 1
        elif max_radii[mirrored_center] > max_mirrored_radius: # then a previous palindrome, p_bey went beyond the bounds of p_big, and p_sub differs from p_bey outside of the characters within p_big  
            max_radii[center] = max_mirrored_radius
            center += 1
        else: #max_radii[mirrored_center] = max_mirrored_radius - in this case, p_sub' is at least a palindrom of radius max_mirrored_radius, and it could be longer...
            radius = max_mirrored_radius
            break

longest_radius = max(max_radii)
center = np.argmax(max_radii)
longest_palindrome = sep_s[center-longest_radius:center+longest_radius+1].replace("|", "")
print(longest_palindrome)

