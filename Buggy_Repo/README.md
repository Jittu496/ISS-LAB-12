### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies  

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Name : Roll Number
- Chervith Reddy : 2024101076
- Jithendra Sai Ram Jetty : 2024101102

### Table to keep track

| ID  | Issue Description                        | Identified By | Fixed By     |
|-----|------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                                    |         Narain |     Whole Team     |
| 2   |In analytics.py --  Corrected field names  |     Jittu496          |     Jittu496         |
| 3   | Incorrect delete endpoint with two parameters in items.py  |     Jittu496        |     Jittu496       |
| 4   | No proper error handling  in items.py    |   Jittu496          |      Jittu496       | 
| 5   |    No proper type hints                  |     Jittu496         |    Jittu496          |  
| 6   | i have changed the items.py - Duplicate POST endpoint for create_item  |      Jittu496       |     Jittu496     |     
| 7   |   Added the missing <div class="container"> in items.html           |    Babu Shaik        |Babu Shaik   |
| 8   |                                          |               |              |
| 9   |                                          |               |              |
| 10  |                                          |               |              |
| 11  | GET method for submitting answers in quiz.py          |    Chervith Reddy           |     Chervith Reddy         |
| 12  |    The HTTP method for get_users() is incorrectly set to @router.post("/") instead of @router.get("/"). | vineel sai reddy         
|               |              |
| 13  |        There's a random comment about music genres: # whats ur favorite genre of music ??? mine is EDM which doesn't belong in production code.  vineel sai reddy
There's a duplicate route decorator @router.post("/") for both get_users() and create_user() functions, which would cause a route conflict. vineel sai reddy 
In the delete_user() function, it's using an incorrect method collection.delete_all() instead of the correct collection.delete_one({"_id": ObjectId(user_id)}).    vineel sai reddy                               |               |              |
| 14  |                                          |               |              |
| 15  |                                          |               |              |
| 16  |                                          |               |              |
| 17  |                                          |               |              |
| 18  |                                          |               |              |
| 19  |  Added <div id="news">Loading news...</div> inside the .container to ensure the script has a target element in news.html  | Babu Shaik     |  Babu Shaik           | 
| 20  |                                          |               |              |
| 21  |                                          |               |              |
| 22  |                                          |               |              |
| 23  |                                          |               |              |
| 24  | Changed <script src="styles/profile.js"></script> to <script src="scripts/profile.js"></script> in profile.html.  | Babu Shaik             |Babu Shaik      |
| 25  |                                          |               |              |
| 26  | <script src="scripts/quiz.js"></script>   in quiz.html                                     | Babu Shaik          | Babu Shaik            | 
 | 27 |                                            |          |                 |
| 28  |                                          |               |              |
| 29  |                                          |               |              |
| 30  |                                          |               |              |
