# The Recipe Bot
Recipe Bot provides all the info you need for whatever you want to cook, even taking dietary needs into consideration

# Video Demo
<a href="https://vimeo.com/226063384"><img src="/images/video-demo-screenshot.png?raw=true" width=500></a>

# It's Built With...
* lex
* lambda
* python
* cloudformation
* amazon-web-services
* aws

# The Team
* Rachel
* Shawn
* Ralph
* Reginald
* Michael

# Inspiration
People that enoy cooking (and even those that don't) sometimes find themselves at a loss for what to cook.  Maybe they've run through all of their go-to recipes or maybe they just have no idea of what to whip up.  Another problem might be that they have an idea for what they want to cook, but need to find a way to accomodate certain dietary needs.  And finally, it can be diffiult to scale ingredients up or down when the number of servings is more or less than what the recipe was written for.

Recipe Bot solves all of these problems.

# What Recipe Bot Does
Recipe Bot listens for direct messages (DMs) in Slack.  A Slack user starts a conversation with Recipe Bot by telling it the main item.  Recipe Bot prompts the user for the number of servings needed and then replies with a link to a top-rated recipe along with ingridents scaled to the correct amounts for the requested serving.

# How We Built It
Our team approached the problem in three ways.

We started with the Lex implementation.  For this phase, we developed the correct utterances and repsonses until we had a working prototype that could capture requests and prepare a query for Yummly, a recipe search engine.

Next, we developed a python script deployed in Lambda that captured the query from Lex and made an API call to Yummly.  With the reply from Yummly, the script parsed the recipe for serving sizes and ingredient amounts.  Given the serving size need for the query, the script scaled the ingridents accordingly for the response.  The response was then returned with the name of the recipe, the ingredients, and a link to the recipe.

Finally, we used the Slack API to deploy an application that could receive the requests; parse the request through Lex; submit the query to Yummly via Lambda; and then reply with the recipe and specifics on the ingredients.

# Challenges We Ran Into
The main challenge we ran into was getting Recipe Bot deployed to Slack.  While implementing a bot in Lex was fairly easy, getting the connection between Slack and Lex proved troublesome.  Specifically, we had problems getting the bot to respond to all team members via Direct Message.  

Initial deployments had Recipe Bot only responding to the team member that did the deployment.  We experimented with deploying the bot to the 'general' channel but then anything that was entered in the channel was interpretted by the bot as a request for a recipe.

Finally, we were able to work through the deployment issues and found a solution that allowed for all team members to correctly DM Recipe Bot and recieve proper responses.

We found another challenge in parsing the resposes from Yummly.  To begin with, making calls to the Yummly API were unintuitive in the order that parameters needed to be passed.  The responses would also come back in unspecified orders.  And finally, we encountered problems parsing ingredients that included fractional measurements like "1/2 cups".  Measurements that were given as strings ("a dash of salt", for example) also proved difficult to parse when amounts needed to be scaled up or down.

# Accomplishments That We're Proud Of
We are proud that we came together as a team to learn more about using Lex as a service for parsing conversational input; using Lambda for making triggered calls to remote APIs; and using Slack as a medium for interacting with bots.

Getting the bot successfully deployed to Slack was a great accomplishment for the team.  After having bots that weren't very conversational, it was great getting a complete response once everything was correctly in place.

# What We Learned
We learned alot about breaking up duties in the team so we could work on different parts of the project in parallel.  We also learned that some APIs might seem easy to interface with but may require substantial testing and debugging to really learn how to use them in spite of what is given as documentation.

# What's Next for Recipe Bot and the Team
We already have ideas for improving recipe bot.  First we'll take care of the major bugs in this minimum viable product.  That includes any quirks in the responses from the bot and getting fractional ingredients properly parsed.  We may also take the time to explore a different API for searching recipes, looking for one that is a bit easier to interface with. In any case, the team will continue to learn more about programing and deploying software that includes natural language processing.

# Try it Out
To try the Recipe Bot for yourself, you can add it to a Slack network: 
<p><a href="https://slack.com/oauth/authorize?&client_id=185786192579.213968000915&scope=bot,chat:write:bot,im:read,links:write"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>
<p>

To deploy the application end-to-end:
* Get a Slack account and Yummly API credentials
* Access the Github repo is here: https://github.com/bit-chatbot-challenge/recipe-bot
* `RecipeBot.json` contains the Lex bot definition.  Use this file to deploy the bot the Amazon Lex
*  `backend/template.yaml` is the Cloudformation template.  Zip the project up and place it in an S3 bucket.  Edit the template with the location of the zip file and the Yummly API credentials
* Connect the Lex bot to the Lambda deployment and publisht the bot
* Create an application in Slack and connect it to the Lex bot
* Start a direct message with the bot and tell it what you would like to cook!

# Image gallery
### Getting a Recipe for Tuna salad:
<img src="/images/recipebot1.png?raw=true" width=500>

### Asking for Directions to Cook Meatloaf:
<img src="/images/recipebot4.png?raw=true" width=500>

### Getting a Recipe for Celery Soup:
<img src="/images/recipebot5.png?raw=true" width=500>

# Privacy Policy 
Our bot does not collect any data from the user. After the recipe requirements are used to retrieve a recipe, that data is not stored anywhere.