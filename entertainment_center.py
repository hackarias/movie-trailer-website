__author__ = 'zackarias gustavsson'
import media
import fresh_tomatoes


# All the movies I want to show together with a movie title and movie trailer for the Movie class
requiem_for_a_dream = media.Movie("Requiem For A Dream", "https://www.youtube.com/watch?v=jzk-lmU4KZ4")
the_road = media.Movie("The Road", "https://www.youtube.com/watch?v=94KcI0gLq1A")
angelas_ashes = media.Movie("Angela's Ashes", "https://www.youtube.com/watch?v=6zLpf1XDNko")
the_mist = media.Movie("The Mist", "https://www.youtube.com/watch?v=LhCKXJNGzN8")
the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel", "https://www.youtube.com/watch?v=1Fg5iWmQjwk")
jude = media.Movie("Jude", "https://www.youtube.com/watch?v=tIHhTaSsANQ")
doctor_zhivago = media.Movie("Doctor Zhivago", "https://www.youtube.com/watch?v=hvIL_A0UsJk")
grave_of_the_fireflies = media.Movie("Grave Of The Fireflies", "https://www.youtube.com/watch?v=4vPeTSRd580")
let_the_right_one_in = media.Movie("Let the Right One In", "https://www.youtube.com/watch?v=ICp4g9p_rgo")

# Listing them all in an array
films = \
    [
        requiem_for_a_dream,
        the_road,
        angelas_ashes,
        the_mist,
        the_grand_budapest_hotel,
        jude,
        doctor_zhivago,
        grave_of_the_fireflies,
        let_the_right_one_in
    ]

# Passing my array to the fresh_tomatoes script for the html page creation
fresh_tomatoes.open_movies_page(films)