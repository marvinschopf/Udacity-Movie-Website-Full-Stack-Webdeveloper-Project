from media import *
import time
import fresh_tomatoes

# Creates the Movie instances
harry_potter_part_1 = Movie("Harry Potter and the Philospher's Stone",
                            "Harry Potter's parents are killed by the dark wizard Voldemort when Harry was still a baby and his aunt concealed him from being a wizard until Hagrid comes to him on his eleventh birthday.",
                            "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
                            "https://www.youtube.com/watch?v=eKSB0gXl9dw",
                            "en")

spiderman_homecoming = Movie("Spiderman: Homecoming",
                             "",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t",
                             "https://www.youtube.com/watch?v=n9DwoQ7HWvI",
                             "en")

beauty_andthe_beast = Movie("The Beauty and the Beast",
                            "",
                            "http://www.kino.de/wp-content/uploads/2017/04/die-schne-und-das-biest-2017-filmplakat-rcm150x212.jpg",
                            "https://www.youtube.com/watch?v=OvW_L8sTu5E",
                            "en")

the_boss_baby = Movie("The Boss Baby",
                      "A baby is the boss!",
                      "http://www.kino.de/wp-content/uploads/2017/04/the-boss-baby-2017-filmplakat-rcm150x212.jpg",
                      "https://www.youtube.com/watch?v=tquIfapGVqs",
                      "en")

ghost_inthe_shell = Movie("Ghost in the Shell",
                          "",
                          "http://www.kino.de/wp-content/uploads/2017/04/ghost-in-the-shell-2017-filmplakat-rcm150x212.jpg",
                          "https://www.youtube.com/watch?v=G4VmJcZR0Yg",
                          "en")

schoene_biest = beauty_andthe_beast = Movie("The Beauty and the Beast",
                                            "",
                                            "http://www.kino.de/wp-content/uploads/2017/04/die-schne-und-das-biest-2017-filmplakat-rcm150x212.jpg",
                                            "https://www.youtube.com/watch?v=OvW_L8sTu5E",
                                            "de")



movies_en = [the_boss_baby,
             spiderman_homecoming,
             beauty_andthe_beast,
             ghost_inthe_shell]

movies_de = [schoene_biest]

fresh_tomatoes.open_movies_page_en(movies_en)
fresh_tomatoes.open_movies_page_de(movies_de)

