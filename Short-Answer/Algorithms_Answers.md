#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The while loop will run as long as "a" is less than n^3.
Meanwhile, each iteration of the loop, "a" will be increased by n^2.
Because a is increaasing at a constant rate O(1) and the while loop condition depends on the size of the output, I believe the time complexity is O(n).

b) The outer for loop depends on the size of the input and the size remains constant, so that would be a time complexity of O(n).
The inner while loop depends on "j" being less than the size of the input, and while it is, "j" gets doubled, meaning it will be larger than n quicker and the while loop will break quicker than if it were being increased by 1. Because of the doubling, I believe this while loop has a time complexity of O(log(n)).
Together, O(n) \* O(log(n)) would mean that the time complexity overall is O(log(n^2))

c) This is a recursive function that will subtract 1 from the value of bunnies until it is zero, returning 2 + the result of each execution. If the input is 5, for example, the function will execute five times and the return will be
2 + bunnyEars(4) -> 2 + bunnyEars(3) -> 2 + bunnyEars(2) + 2 + bunnyEars(1) -> 2 + bunnyEars(0) -> if bunnies == 0 return 0
2 + 2 + 2 + 2 + 2 + 0 = 10

Since the number of executions depends on the size of the input, I believe the time complexity is O(n)

## Exercise II

def save_eggs(n):

    for f in range(n): O(n)
      throw egg

      if egg breaks:
        return f - 1

Runtime Complexity of O(n)
