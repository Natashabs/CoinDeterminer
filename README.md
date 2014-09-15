#Step 2 - Practice test
##Problem One: Coin Determiner

Using the Python language, have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to
250, and return an integer output that will specify the least number of coins, that when added, equal the input integer. 
Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: 
if num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, 
then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins. 
Use the Parameter Testing feature in the box below to test your code with different arguments.

Input Test:
6
16
23

Test Output:
2
2
3

#Introduction to the Problems

    •The resolution must be a web application.
    •There must be a way to supply the application with the input data via text file that will be uploaded
    •The application must run
    •The code needs to be hosted in your GitHub account
    •You should provide sufficient evidence that your solution is complete by, as a minimum, indicating that it works correctly against the supplied test data

#Contents
    *`coin.py` - Algorithm to solve the problem.
    *`coin_web.py` - Web code to upload the text file and show the result.
    *`test.py` - Unit test
    *`examples.txt` - Text file with some input examples tests.

#Run the project
It's necessary the Python version 3.4.1 and the Pyramid to run the project.
    1. Download the project
    2. Run the `coin_web.py` 
        *For example: 
            C:\> python.exe coin_web.py
        This command will not return and nothing will be printed to the console.    
        When port 8080 is visited by a browser on the URL http://localhost:8080, the server will simply serve up a page to upload the text file (you can "_examples.txt_" if you want to). 
        If the application is running on your local system, the http://localhost:8080/result in a browser will show the result.

#Tests
You also can run the unit tests (_test.py_ file)  to test the project.