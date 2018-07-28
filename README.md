# Movie Trailer Website

## Description
   
   Movie trailer Website is a project that consists f server-side code 
   to store a list of movies  titles, along with its respective box art 
   imagery and movie trailer website.  


## Installation
  
  * Python needed to be installed on computer  (https://www.python.org/downloads/)
  
  * Within the download, there will be 3 files to use :
     
     *entertainement_center_movies
    
    *media.py
    
    *fresh_tomatoes.py
 
 * open "entertainement_center_movies" file and run it.

## Usage
  
  -in the "entertainement_center_movies" file :
   
   * we import _fresh_tomatoes_ file which contains codes for the html page,
     and  _media_ file which contain movie variables.
  
  - _media_  file:
   
   def __init__(self, movie_title, movie_duration, movie_release_date, movie_storyline,movie_director, poster_image,
                 trailer_youtube, movie_rating):
                 
  
  - _fresh_tomatoes_ file:
     
     content += movie_tile_content.format(
            movie_title=movie.title,
            movie_duration=movie.duration,
            movie_release_date=movie.release_date,
            movie_storyline=movie.storyline,
            movie_director=movie.director,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_rating=movie.rating
        )
    return content
    
  -`fresh_tomatoes.open_movies_page(movies)` allow the creation of an html file.
  To run this program open the "entertainement_center_movies", the movies instances 
  are assigned to the variable "movies" which `fresh_tomatoes.open_movies_pag` function uses
  to create the html file. Click Run Module and the browser will open with webpage. 
  

## Contributions
  
   if you want to contribute to the project, open "entertainement_center_movies" file
   and add your favorite movie with its respective data including poster image and trailer website.


##  Licence

      PROJECT LICENSE

   This project was submitted by Fady Fouad as part of the Nanodegree At Udacity.

  As part of Udacity Honor code, your submissions must be your own work, hence
  submitting this project as yours will cause you to break the Udacity Honor Code
  and the suspension of your account.

  Me, the author of the project, allow you to check the code as a reference, but if
  you submit it, it's your own responsibility if you get expelled.

  Copyright (c) 2017 Fady Fouad
  
  ## Resources 
   
   1- https://gist.github.com/laramartin/7796d730bba8cf689f628d9b011e91d8
  
   2- https://google.github.io/styleguide/pyguide.html
   
   3- https://www.python.org/dev/peps/pep-0008/
   
