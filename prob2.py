from sys import stdin

# class to find longest subsequence palindrome's length and resulting palindrome string
class LongestPalindromeSubsequence:

    # Initializing the requires strings and matrices for computation
    def __init__(self, og_str, rev_str, opt, pie_matrix):
        self.og_str = og_str
        self.rev_str = rev_str
        self.opt = opt
        self.pie_matrix = pie_matrix

    # Method to Find the Longest Palindrome Subsequence Length
    def longestPalindromeSubsequenceLength(self):

        # As the First Row and Column of Opt Table should be 0 we start with Indices 1 for both Row and Column
        # The Table has columns and rows both of equal size as the strings whose common subsequence to be found are reverse of each other
        # As we start from Indice 1 in Table we have kept row and column strength +1 of string length
        for i in range(1, str_len + 1):
            for j in range(1, str_len + 1):
                # If character of original and reverse string matches
                if self.og_str[i - 1] == self.rev_str[j - 1]:
                    # Adding the Value +1 from the Upper Left Diagonal Element when characters match
                    self.opt[i][j] = self.opt[i - 1][j - 1] + 1
                    # Giving the Reference of Diagonal from which the value has been updated
                    # Pie Matrix is to be used to the resulting subsequence string which in our case would be Palindorme
                    self.pie_matrix[i][j] = 'diag'
                # Other two conditions check for which element upper or left one is maximuma and update the value accordingly if the characters don't match
                elif self.opt[i][j - 1] >= self.opt[i - 1][j]:
                    self.opt[i][j] = self.opt[i][j - 1]
                    # Giving Reference of Left Element from where the value has been updated for the Opt Table
                    self.pie_matrix[i][j] = 'left'
                else:
                    self.opt[i][j] = self.opt[i - 1][j]
                    # Giving Reference of Upper Element from where the value has been updated for the Opt Table
                    self.pie_matrix[i][j] = 'up'

        # The Last Row's Last Column would have the longest common subsequence of the original and reverse string
        # As the other string is reverse of original, the subsequence would be Palindrome and hence the Longest Palindrome Length
        return self.opt[str_len][str_len]

    # Method to Find the Longest Palindrome Subsequence String
    def longestPalindromeSubsequenceString(self):

        i = j = len(self.og_str)
        subseq_str = ""

        # As in Previous Method while computing the Length we got the Pie Matrix wwe will check for the Diagonal Reference where the Value was updated in Opt Table
        # The Column position where we have the Diagonal Reference, is the Indice in the Original String to be considered for Palindrome
        while i > 0 and j > 0:
            if self.pie_matrix[i][j] == 'diag':
                subseq_str += self.og_str[i - 1]
                i -= 1
                j -= 1
            elif self.pie_matrix[i][j] == 'up':
                i -= 1
            else:
                j -= 1

        # Returning the Subsequence String which is Palindrome in our case
        return subseq_str

# Original String From Input File
og_str = stdin.read().strip()

# Reversed String so as the to find the Common Subsequence from Original String
rev_str = og_str[::-1]
str_len = len(og_str)

# Initialing the Opt Table to 0's and Pie Matrix as string 'null'
rows, cols = (str_len+1, str_len+1)
opt = []
pie_matrix = []
for i in range(rows):
    opt_col = []
    pie_col = []
    for j in range(cols):
        opt_col.append(0)
        pie_col.append('null')
    opt.append(opt_col)
    pie_matrix.append(pie_col)

# Object Creation of LongestPalindromeSubsequence Class in order to call Required Functions
LPS = LongestPalindromeSubsequence(og_str, rev_str, opt, pie_matrix)

# Calling Longest Palindrome Subsequence Function to get the Length and Display
print(LPS.longestPalindromeSubsequenceLength())

# Calling Longest Palindrome Subsequence Function to get the String and Display
print(LPS.longestPalindromeSubsequenceString())





