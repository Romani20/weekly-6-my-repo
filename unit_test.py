def getShowBasedOnChannel(channel, showTitles):
    """Checks which show is available for the user's channel.

    Args:
        channel (string): The channel the user has access to.
        showTitles (dict): A dictionary of available show to channel pairs. 

    Returns:
        String: Returns the show available for the user's 
                channel; returns None if no show is available. 
    """
    res = None
    for key in showTitles:
        if showTitles[key] == channel:
            return key
    return res

def genericUnitTest(test_func, desired_input_1, desired_input_2, desired_output):
    """A generic unit test to test a function, in this case one that 
        takes two args, like getShowBasedOnChannel. It asserts True if 
        the expected output of the function matches the actual, and False
        otherwise. It also records any exception encountered.

    Args:
        test_func (function): the two-argument function to be tested
        desired_input_1 (_type_): in this case, the user channel availability
        desired_input_2 (_type_): in this case, the show title of the show the user intends to watch
        desired_output (_type_): the expected return value of test_func
    """
    
    print("Testing " + test_func.__name__)
    print("Input:")
    print("\t (Param 1): " + str(desired_input_1) + ", \n\t (Param 2): ", desired_input_2)
    print("Expected output:", desired_output)
    print("Actual output: ", (test_func(desired_input_1, desired_input_2),))
    try:
        assert desired_output == (test_func(desired_input_1, desired_input_2),)
    except Exception as name:
        print("\nUNIT TEST RESULTS:")
        print("TEST FAILED. The following exception has occurred: " + type(name).__name__)


#TEST CASES
showsAndChannel1 = ("WeirdTV", {"Money Heist": "SpanishTV", "Stranger Things": "ScaryTV"})
tup = (None,)
genericUnitTest(getShowBasedOnChannel, *showsAndChannel1, tup)

print("\n")

showsAndChannel2 = ("ScaryTV", {"Money Heist": "SpanishTV", "Stranger Things": "ScaryTV"})
tup = ("Stranger Things",)
genericUnitTest(getShowBasedOnChannel, *showsAndChannel2, tup)
