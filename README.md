# JustEat-assessment - Juan Pereda Hernández
This is a repository created to track the completion of and share the proposed solution to a coding exercise that makes up a part of the assessment process for the "Early Careers Enterprise IT Program" at JustEat Takeaway.

* How to compile and run this code:
   All that is needed to run this code is a python-compatible IDE and having the "requests" library installed. Here's a link to a quick guide on how to do so using pip, Python's native package manager: https://datagy.io/install-requests-python/
   In my case, I used VS Code with the Python extension.

* How to build this solution:
   This solution uses a set of nested functions to pull the data from the API, filter it to obtain the relevant data, create a list out of that data, and finally print it to the screen. The different blocks it is divided in are as follows:
   1. Importing relevant libraries and initializing the restaurant list variable that is as our end-goal variable.
   2. Definition of functions:
      2.1 transform_data: constructs the list of restaurants by filtering the pulled data, then adding the relevant attributes to a dictionary variable that will represent each individual restaurant, and finally adding that dictionary to our list.
      2.2 pull_data: pulls the data from the API.
      2.3 get_restaurants: requests a zip code from the user and initiates the data pull passing the zip_code variable on to the pull_data function. Once the nested functions have finished running, it also prints the final list.
   3. Running the outer function: running get_restaurants starts the process.

  
