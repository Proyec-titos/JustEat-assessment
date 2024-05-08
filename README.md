# JustEat-assessment - Juan Pereda Hernández
This is a repository created to track the completion of and share the proposed solution to a coding exercise that makes up a part of the assessment process for the "Early Careers Enterprise IT Program" at JustEat Takeaway.

* How to compile and run this code:
   All that is needed to run this code is a python-compatible IDE and having the "requests" library installed. Here's a link to a quick guide on how to do so using pip, Python's native package manager: https://datagy.io/install-requests-python/.
   My IDE of choice was VS Code with the Python extension.

* How to build this solution:
   This solution uses a set of nested functions to pull the data from the API, filter it to obtain the relevant data, create a list out of that data, and finally print it to the screen. The different blocks it is divided in are as follows:
      - 1. Importing relevant libraries and initializing the restaurant list variable that is as our end-goal variable.
      - 2. Definition of functions:
         2.1 transform_data: constructs the list of restaurants by filtering the pulled data, then adding the relevant attributes to a dictionary variable that will represent each individual restaurant, and finally adding that dictionary to our list.
         2.2 pull_data: pulls the data from the API.
         2.3 get_restaurants: requests a zip code from the user and initiates the data pull passing the zip_code variable on to the pull_data function. Once the nested functions have finished running, it also prints the final list.
      - 3. Running the outer function: running get_restaurants starts the process.

* Areas of improvement:
  While this solution works, there are aspects of it that could be polished if given more development time, namely:
     - Eventhough the code can pull data from any valid zip code once, the get_restaurants function can't load data from two different zip codes as it stands: the condition in line 26 only checks that a list of restaurants hasn't been generated yet. If the function was called twice for two different zip codes, it would run appropiately on the first run only. In the second, it would still ask for a zip code, but it would simply return the list of restaurants from the first one. To fix this, the zip code should be stored so that it could be checked against future inputs of zip code when the function is called again.
     - The list of restaurants printed to the screen lacks an easy-to-read format.
     - There should be a loop to check the zip code entered by the user and make sure it is a valid input.

* Note(s):
   - Version 2.0.0 of this code fulfills the prompt as written, while version 2.1.0 is a solution that accepts input from the user to select a zip code, and then generates the list as requested on the exercise. 
