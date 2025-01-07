from apiFun import *
# web server parts
from http.server import HTTPServer, BaseHTTPRequestHandler;

# used to parse the URL and extract form data for GET requests
# from urllib.parse import urlparse, parse_qsl;
import os

class handler(BaseHTTPRequestHandler):
    # Step 1 Have the intro to the website with a start button which will go to a post method
    def do_GET(self):
        if self.path.endswith(".jpg"):
            file_path = os.getcwd() + "\\image.jpg"
            print(f"file path is {file_path}")
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
                return
        else:
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            title_html = """
            <!DOCTYPE html>
            <html>
                <head>
                    <style>
                        body {
                            background-color: #353535;
                        }
                        #title {
                            position: relative;
                            animation:fadeInAnimation ease 5s;
                            text-align: center;
                            font-family:'Courier New', Courier, monospace;
                            font-size: 10vw;
                            color: white;
                        }
                        #start{
                            position: relative;
                            text-align: center;
                            animation: fadeInAnimation ease 5s;
                            font-size: 3vw;
                            -webkit-text-stroke: 0.5px #000000;

                        }
                        .button{
                            background-color: #ff7fc5;
                            border:black;
                            color: white;
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            font-weight: bold;
                        }
                        /* fading animation */
                        @keyframes fadeInAnimation {
                            0% {
                                opacity: 0;
                                top: -50px
                            }

                            100% {
                                opacity: 1;
                                top: 0px
                            }
                        }

                    </style>
                </head>

                <body>
                    <h1 id="title">
                        AniGuesser!
                    </h1>
                    <div id="start">
                        <form method=POST action="/game">
                            <button class="button">
                                Start
                            </button>
                        </form>
                    </div>
                </body>
            </html>
            """
            self.wfile.write(title_html.encode())
    
    def do_POST(self):
        if self.path.endswith("/game"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            rand_anime = get_rand_anime()
            # print(rand_anime)
            titles = ""
            for title in rand_anime:
                titles += f"'{title}',"
            # print(titles)
            game_html = ""
            game_html += """
<!DOCTYPE html>
<html>
    <head>
        <style>
            p{
                text-align: center;
                color:#ffffff
            }
            body {
                background-color: #353535;
            }

            #image{
                text-align: center;
                filter: blur(40px);
            }
            #allinput{
                display: flex;
                justify-content: center;
                align-items: center;

            }
            .input{
                border-style: solid;
                border-color: white;
                border-width: 2px;
                background-color: #ff7fc5;
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                -webkit-text-stroke: 0.5px #000000;
            }
            #again{
                display: none;
            }
            #guess{
                animation: none;
            }
            @keyframes fadeRed {
                0% {
                    background-color: #ff7fc5;
                } 
                50% {
                    background-color: red;
                }
                100% {
                    background-color: #ff7fc5;
                }
            }
            @keyframes fadeGreen {
                0% {
                    background-color: #ff7fc5;
                }  
                50% {
                    background-color: lightgreen;
                }
                100% {
                    background-color: #ff7fc5;
                }
            }
        </style>
        <body>
            <div id="image">
                <img src="http://localhost:8000/image.jpg">
            </div>
            <br>
            <p id="count">
                You have 6 guesses left
            </p>
            <p id="titles"></p>
            <br>
            <p id="message"></p>
            <!-- all things that the user interfaces with will be under 1 container -->
            <div id="allinput">
                <!-- this is where the user types -->
                <input class = "input" type="text" id="guess">
                <!-- this is where the user submits -->
                <button class = "input" id="go">
                    Guess
                </button>
                <!-- this is where the user will ask to play again, will reload the page with new anime -->
                <form method=POST action="/game">
                    <button class="input" id="again">
                        Try Again?
                    </button>
                </form>
                <br>
            </div>
            <br>
            <script>
                // keeps track of the number of attempts
                let tries = 6
                // all the titles of the correct animes
                let correct = ["""
            game_html += titles  
            game_html +="""] 
                // flag to end the game
                let found = 0  
                // blur quantity
                let blurQuan = 40
                // set a listener on the submit button that will call the function
                document.getElementById("go").addEventListener("click", checkGuess)
                function checkGuess(){
                    // get the value in the text field
                    let userGuess = document.getElementById("guess").value
                    // the logic will only check if the user still has tries and hasn't won
                    if (tries > 0 && found == 0){
                        // goes through every anime title
                        for(let i = 0; i < correct.length; i++){
                            if (userGuess.toLowerCase() == correct[i].toLowerCase()){
                                document.getElementById("message").innerHTML = "Correct!";
                                // show the try again button
                                document.getElementById("again").style.display = "inline-block";
                                // hide the sentecnce that tracks the number of guesses left
                                document.getElementById("count").style.display = "none";
                                // proper grammer
                                if(correct.length == 1){
                                    document.getElementById("titles").innerHTML = "The Correct Answer was: <br>" + correct;
                                }
                                else{
                                    document.getElementById("titles").innerHTML = "The Correct Answers are: <br>" + correct;
                                }
                                // unblur the image to show the answer
                                document.getElementById("image").style.filter = "blur(0)";
                                // ends the for loop
                                i = correct.length
                                // flag to end the game
                                found = 1
                                // first remove property and cause reflow to ensure animations can be done more than once
                                document.getElementById("guess").style.removeProperty("animation")
                                document.getElementById("guess").offsetWidth //reflow
                                document.getElementById("guess").style.animation = "fadeGreen ease 2s"                              
                                
                            }  
                        }
                        // if the guess isn't right
                        if(found == 0){
                            document.getElementById("message").innerHTML = "Wrong :(";
                            tries = tries - 1;
                            // will run if last guess is wrong
                            if(tries == 0){
                                document.getElementById("message").innerHTML = "Ran Out of Guesses :(";
                                document.getElementById("again").style.display = "inline-block";
                                document.getElementById("count").style.display = "none";
                                // proper grammer
                                if(correct.length == 1){
                                    document.getElementById("titles").innerHTML = "The Correct Answer was: <br>" + correct;
                                }
                                else{
                                    document.getElementById("titles").innerHTML = "The Correct Answers are: <br>" + correct;
                                }
                                    document.getElementById("image").style.filter = "blur(0)";                
                            }
                            // will run if more guess are there
                            else{
                                document.getElementById("count").innerHTML = "You have "+ tries + " guesses left";
                                // less blur on next attempt
                                blurQuan = blurQuan - 5
                                document.getElementById("image").style.filter = "blur("+blurQuan+"px)";
                            }
                            document.getElementById("guess").style.removeProperty("animation")
                            document.getElementById("guess").offsetWidth //reflow
                            document.getElementById("guess").style.animation = "fadeRed ease 2s" 
                            
                        }
                    }
                }
                   
            </script>
        </body>
    </head>
</html>
"""
            self.wfile.write(game_html.encode())
def main():
    PORT = 8000
    server = HTTPServer(("", PORT), handler)
    print(f"Server is running on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()