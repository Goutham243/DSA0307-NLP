#PROGRAM 2#
def finite_state_automaton(string):
    # States:
    # q0 = 0 (Start)
    # q1 = 1 (Last character is 'a')
    # q2 = 2 (String ends with 'ab') - Accepting state

    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 2
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        print("The string is accepted.")
        print("It ends with 'ab'.")
    else:
        print("The string is rejected.")
        print("It does not end with 'ab'.")

# Driver Code
string = input("Enter a string: ")
finite_state_automaton(string)
