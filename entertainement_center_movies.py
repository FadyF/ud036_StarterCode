
#this is  where we create the instances of Movie class
#and run the file to view the movie website page
import fresh_tomatoes
import media

# These are instances of class movie


#Titanic
titanic = media.Movie("Titanic",
                      "195 minutes",
                      "19 December 1997",
                      "Epic Romance set against the ill-fated voyage of the RMS Titanic",
                      "James Cameron",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      "PG-13")

#The Wolf of Wall Sreet
the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street ",
                                      "180 minutes",
                                      "17 December 2013",
                                      "Biographical film that recounts Belfort's perspective on his career as a stockbroker in New York City and orruption and fraud on Wall Street.",
                                      "Martin Scorsese",
                                      "https://upload.wikimedia.org/wikipedia/en/d/d8/The_Wolf_of_Wall_Street_%282013%29.png",
                                      "https://www.youtube.com/watch?v=iszwuX1AK6A",
                                      "R")

#The Mummy                                          
the_mummy = media.Movie("The Mummy",
                        "125 minutes",
                        "7 May 1999",
                        "Adventurer Rick O'Connell travels to Hamunaptra, the city of the dead, with an archaeologist and her brother when  accidentally they awaken Imhotep, a high priest from the reign of the pharaoh Seti.",
                        "Stephen Sommers",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/The_mummy.jpg",
                        "https://www.youtube.com/watch?v=h3ptPtxWJRs",
                        "PG-13")

#Mission: Impossible - Ghost Protocol
mission_impossible_ghost_protocol = media.Movie("Mission: Impossible Ghost Protocol ",
                                                "133 minutes",
                                                "16 December 2011",
                                                "After been blamed for a terrorist attack, IMF agency go into ghost protocol and try to stop a nuclear attack",
                                                "Brad Bird",
                                                "https://upload.wikimedia.org/wikipedia/en/b/b5/Mission_impossible_ghost_protocol.jpg",
                                                "https://www.youtube.com/watch?v=5NKFDP7uaLI",
                                                "PG-13")
#Meet the Fockers
meet_the_fockers = media.Movie("Meet the Fockers",
                               "115 minutes",
                               "22 December 2004",                               
                               "Gaylord  Focker  and his fiancee Pam Byrnes  decide to introduce their parents to each other.",
                               "Jay Roach",
                               "https://upload.wikimedia.org/wikipedia/en/2/27/Meet_The_Fockers.jpg",
                               "https://www.youtube.com/watch?v=JG5NnOIKeew",
                               "PG-13")

#Spider-Man
spider_man = media.Movie("Spider-Man",
                         "121 minutes",
                         "3 May 2002",
                         "Peter Parker, a high school student living in New York City, who turns to crimefighting as Spider-Man after developing spider-like super powers",
                         "Sami Raimi",
                         "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
                         "https://www.youtube.com/watch?v=O7zvehDxttM",
                         "PG-13")

# this is a list of the instances of class movie  assigned  to movies variable
movies = [titanic,the_wolf_of_wall_street, the_mummy,
          mission_impossible_ghost_protocol, meet_the_fockers, spider_man]


# open_movies_page is a method inside fresh_tomatoes.py
# It takes a list of movies, and creates an HTML file

fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)

