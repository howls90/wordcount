# wordcount

Dear Zaidin,

I’m Marti Floriach and recently I applied for a job position at Virtusize.
Mark told me to contact directly you if I have questions about the “backend assignment”.

 Before starting the task there are some points that I would like to clarify:

- Which environment should I use to deploy the task? I mean, Mark told me that you are using lambdas to deploy the APIs. This task should be done taking into account that in production it will work inside an AWS lambda function? Or can it run in a server with multiples cores?

- The request definition is up to me so I guess I can add as many optional parameters as I want, correct? Therefore, in order to implement the necessary functions and suitable functions for the future, what is the reason to create a wordcount? Or what will do the user with the response content?
(If there are not, I will make up one and build the API according to that idea)
 
- Just to be sure, I must count just the word "fit", right? In this format “ fit ” without variation, if the word is uppercase, lowercase or Capitalize doesn’t matter.

- In the description of the assignment, you ask to count the word “fit” in the html source. Inner, Outer or both? Ex: ```<h1 class=”fit”>FIT<h1>```
Count just the text inside the tag “FIT” → 1

- Can the API have multiples endpoints? To update the database for example.
 
- Are there any requirements in terms of performance? Not to use too much memory, high number of request per second, …

- Must the final version contain the deployment code? For example, zappa configured to make the deployment inside a lambda. Or a docker compose file is enough?

Thank you for your time, I look forward to your response.
