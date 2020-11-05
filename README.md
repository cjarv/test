#Welcome to Encore interviewing process!
###This consists of interviews as well as some code questions, below.

The code questions:

 

In answering the code questions, please submit code as if you intended to ship it to production. The details matter. Tests are expected, as is well written, simple idiomatic code. Feel free to use a service like github gist to send us the result or attach in the email body or give as an URL for the files hosted in dropbox or google drive.

 

Use Python as the language to solve the problems as this is what we mostly use in production.

 

We believe this should take around 4 hours to complete. Please let us know (roughly) when we should expect your answers (e.g. “over the weekend”). Let us know if you need more time.

 

It may take us 1 to 3 days to review your answers. They’re passed to our pipeline team to review.


    1. What’s your proudest achievement? It can be a personal project or something you’ve worked on professionally. Just a short paragraph is fine, but I’d love to know why you’re proud of it.
        - I would say my proudest achievement would be the scheduling tool I built. It was a unique problem that when implemented could solve problems
          most vfx companies face on a daily basis and has direct impact on every level of the company. Giving artists better date managment to have more 
          realistic deadlines, producers to have insight directly into their production, give leads real data to manage their teams fluidly. The other
          important aspect of the system was to hav data for post mortems and charting options for EPs and company owner to see how their production 
          is burning down. It also taught me a valuable lesson about the development lifecycle. Building an app this large takes a certain kind of management
          to see it through and it will never be perfect the first time around. 
    
    2. Tell me about a technical book or article you read recently, why you liked it, and why I should read it.
        - I can't say that I finished the book but the last coding book I read was called "Clean Code" what the book did is cover best coding practices.
          It is speaking irectly to c++ but I find many of the practices that book highlights are general enough to translate to every language as well
          as broken into chapters that are great discussion points among teams.
    
    3. Tell me about something on visual effects that you really like, and why.
        - I always find lighting in computer graphics very interesting. Many of the primers wrote by Paul Debevick on capturing light rays from scans and images 
          for use in computer generated refraction and subsurface scattering is amazing. How it got to the point it is today I find interresting even though
          we take much of it for granted in the DCCs. Building a raytracer has ben on my list of things to do for some time now. 
    
    4. Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
        TempTracker.py flatten_array()
        
        
    5. Write a class TempTracker with these methods:
        insert()—records a new temperature.
        get_max()—returns the highest temp we've seen so far.
        get_min()—returns the lowest temp we've seen so far.
        get_mean()—returns the mean of all temps we've seen so far.
        **get_mean() should return a float, but the rest of the getter functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.
    
