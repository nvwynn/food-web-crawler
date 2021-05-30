# food-web-crawler

This Python script is based on a 2018 tutorial by Felippe Rodrigues.
My motivation for creating this specific crawler was inspired by two things:
1) Twitter data related to my area of research is quite limited; and
2) Facebook's API process is intimidating!

About my research: I'm interested in public dialogue around food and hunger, especially how the USDA's Supplemental Nutrition Assistance Program (SNAP, but also sometimes called EBT, Electronic Benefit Transfer, and food stamps) is perceived.  

My process: At first, I explored Twitter using a web crawler to pull out Tweets with keywords "food stamps" and "EBT" that were in specific geographic areas. I defined parameters to pull from the following areas: Seattle, WA; Spokane, WA; Lafayette, LA; Colorado Springs, CO; and Mesa, AZ. My hypothesis was that a pattern of negative or positive sentiment could be mapped on to areas that are politically conservative and liberal, respectively. What I found was that there was not enough data on Twitter to test this hypothesis and make a broad generalization, but at a very granular level (i.e. individual tweets), I did find some fascinating perspectives related to my topic. I decided that the best way forward would be to perform a sentiment analysis with the help of Reddit. This analysis will connect to two arguments made in my paper and will be discussed as a methodology itself as well.

Purpose of script: As is, this script will pull out the 100 most upvoted posts in the subreddit r/foodstamps. It can easily be modified to pull from any subreddit, search posts based on keywords, or filter based on other parameters that Reddit uses. These definitions are written as notes in the script itself.

Thank you for reading and happy scripting! 
