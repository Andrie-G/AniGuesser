# This file will initialize the api key and call on
import requests
import os
api_key = "https://api.jikan.moe/v4"

"""
this function will return a list that contains a all titles of a random anime and stores it
image in the local directory to be used for displaying on the website
this will return False if it is unable to get an anime
"""    
def get_rand_anime():
    all_titles = []
    # set this for the loop to start, this flag 
    # will be set when an anime retrived is popular enough
    is_valid_anime = False
    # this call can call for a random anime
    api_url = f"{api_key}/random/anime"

    while is_valid_anime is False:
        response = requests.get(api_url)
        if check_status_code(response) is False:
            return False
        # if all checks work, convert the json data into a python dictionary
        anime_description = response.json()
        # print(anime_description)
        # checks if the response from the api is working and worth using in game
        is_valid_anime = valid_anime(anime_description)
     
    # after the checks are complete, we then save the info needed for the website
    
    if anime_description["data"]["title"] is not None:
        all_titles.append(anime_description["data"]["title"])
    if anime_description["data"]["title_english"] is not None:
        all_titles.append(anime_description["data"]["title_english"])
    if anime_description["data"]["title_synonyms"] is not None:
        for title in anime_description["data"]["title_synonyms"]:
            all_titles.append(title)
    # print(all_titles)
    save_image(anime_description)
    return all_titles
    

"""
this method will check the status code of the response
if the call generates 400 or 404 it tries again
otherwise if the issue isn't with the call but with the service it returns None
if all else works, it returns the status code which should be 200
"""
def check_status_code(response):
    while response.status_code == 400 or response.status_code == 404:
        if response.status_code == 400:
            print("400 - Invalid Request")
        else:
            print("404 - Resource was Not Found or MAL is Inactive")
        response = requests.get(f"{api_key}/random/anime")
    if response.status_code == 405:
        print("405 - Requested Method is not supported")
        return False
    elif response.status_code == 429:
        print("429 - Rated-Limited by Jikan or MAL")
        return False
    elif response.status_code == 500:
        print("500 - Something Didn't Work, Try Again Later")
        return False
    elif response.status_code == 503:
        print("503 - Service is Down, Try Again Later")
        return False
    else:
        print("200 - Responsive")
        return response

"""
This method will check if the random anime retrived is valid for the purposes of the game,
some things it checks are rank, popularity, image availibility, score, and suitable anime 
"""
def valid_anime(description):
    # if an anime doesn't have a proper rank or populatory score, then it won't be added
    if (description["data"]["rank"] is None or description["data"]["popularity"] is None):
        return False
    # this is a range for an anime to be accepted for guessing
    elif description["data"]["rank"] > 6000 and description["data"]["popularity"] > 6000:
        return False
    # blocking animes with particular genres to not show up in the game
    if description["data"]["genres"] is not None:
        for genre in description["data"]["genres"]:
            if genre["name"] == "Hentai" or genre["name"] == "Erotica" or genre["name"] == "Ecchi":
                return False
    else:
        return False
    if description["data"]["images"]["jpg"] is None:
        return False
    if description["data"]["score"] > 0 and description["data"]["score"] < 7:
        return False
        

"""
This method gets the image from the json data and saves it to the local directory
"""
def save_image(desc):
    if desc["data"]["images"] is None:
        return False    
    image_url = desc["data"]["images"]["jpg"]["large_image_url"]
    image_res = requests.get(image_url)
    image_data = image_res.content
    if os.path.exists("image.jpg"):
        os.remove("image.jpg")
    f = open("image.jpg", "wb")
    f.write(image_data)
    f.close()
    
    
    

