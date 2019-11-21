def new_decorator(original_function):
    def wrapping_function():

        print("Code to execute before original function")

        original_function()

        print("Code to execute after original function ")

    return wrapping_function()

#decorated_function = new_decorator(function_that_needs_decorator)

@new_decorator
def function_that_needs_decorator():
    print("I am function_that_needs_decorator")

