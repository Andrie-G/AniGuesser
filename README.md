# AniGuesser

AniGuesser is an anime guessing game that can run in your browser!

# Requirements
- Latest version of Python 
- Latest vesion of Git

# How to Start the Game
1. Clone the Respository
2. Use your prefered command line and navigate to where the repository is cloned
3. Run mainServer.py, i.e. "python mainServer.py"
4. In your browser, (preferably chrome), type in the url search: "http://localhost:8000/"
5. Press the Start Button

# How to Play
1. You have 6 guesses to guess the anime
2. Every wrong guess reduces the blur on the image
## Notes
- Either the english or japanese name of an anime can be guessed using english characters
This means both "Sousou no Frieren" and "Frieren: Beyond Journey's End" are vaild answers
- Guesses are not case sensitive
- The guess of the anime has to be exact. For example if the correct answer is "Frieren: Beyond Journey's End", guessing "frieren" will result in an incorrect answer
- Pressing Start or Try Again will cause the webpage to load for a few seconds if needed, this is natural as it is confirming whether a valid anime is found
# Later Improvements
Some planned features to be implemented later:
- manga guessing
- character guessing
- database integration for videos and anime
# Video Demonstation
https://github.com/user-attachments/assets/3bfca94f-f6f3-4bad-9f0b-9576540b5a48

# Details 
This project is using the Jikan API. It is using the public API key that can be found at the offical Jikan website, https://jikan.moe/


https://github.com/user-attachments/assets/3bfca94f-f6f3-4bad-9f0b-9576540b5a48


The server calls the api for a random anime, it then takes the anime image and titles to displays on the localhost (AniGuesser webpage) 
# Resources used to create this project
https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/
https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
https://www.w3schools.com/python/module_requests.asp
https://www.w3schools.com/python/ref_requests_response.asp
https://www.w3schools.com/python/python_dictionaries.asp
https://www.geeksforgeeks.org/how-to-create-fade-in-effect-on-page-load-using-css/
https://www.w3schools.com/html/
https://www.w3schools.com/css/
https://www.w3schools.com/js/
https://stackoverflow.com/questions/13426875/text-border-using-css-border-around-text
https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Center_an_element
https://medium.com/@venu_madhav/master-the-python-f-string-26a426459bdb#:~:text=When%20using%20quotation%20marks%20inside,strings%20without%20causing%20syntax%20errors.&text=Let's%20see%20how%20to%20use,Stay%20curious%2C%20stay%20humble.%22
