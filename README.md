# tissera_yasser_DS_project
Movie Suggestor / Critics vs. User Review Scores 
- Project Type: Visualization / Classification 
    - Visualizing discrepancies between Critic Review Scores and User Review Scores 
    - Classifiying movies based on audience score vs critic score, genre, in order to suggest movies to users who want a movie suggestion

Why
- If you are reading this, you probably love movies and there are probably some movies you love that might not be loved by the critics. Or you are looking for a movie to watch and you are duped into thinking you are about to watch a great movie because rotten tomatoes tells you it's certified fresh but you're half asleep twenty minutes in. Whatever the case may be, ratings affect the way you make decisions to watch this movie over another movie and we think having this information available to you might help you make a better decision about how to spend your valuable time watching a movie. 

Functionality 
1. User will type in a movie that hopefully exists in the database, output will be the movie title, poster, description, genre, and most importantly, whether critics and viewers differed or agreed in their rating of the movie. 
    - This can either be in the form of a +/- score which will be the audience score - critic score or we can just print out audiences liked this more than the         critics and vice versa or we can do both 
2. Can also have a feature where the user can ask for a movie suggestion, the user would let us know which genre they would like to watch and maybe whether they would like a movie where critics were either on the same page with viewers, liked a movie more than viewers, or disliked a movie more than viewers, or they can have no preference and we can select a movie for them 
    - To add increased complexity, we can ask the user to input a couple movies they liked or have watched recently and extract information like the directors         and the cast from those movies to try and find a movie with similar directors and actors from those movies to curate the movie pick better 


Resources
1. https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+movies.csv
2. http://www.omdbapi.com/
3. http://rstudio-pubs-static.s3.amazonaws.com/336722_2193716117584b63a2a6ebb837217d85.html#imdb-rotten-tomatoes-datasets-from-ocdf
4. Web scraping audience scores from RT and Metacritic 
