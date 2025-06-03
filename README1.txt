README file
-----------
You must also submit a README file (named README.txt) with clearly delineated sections for the following.

0. Please write down the full names and netids of both your team members.

Harsh Borkhetaria hpb34
Cleon Monis cvm53
Sameel Arif sma369
Saanvi Pandey sp2404

1. Are there known issues or functions that aren't working currently in your
attached code? If so, explain. (note that you will get half credit for any reasonably sized bug that is fully explained in the readme)

There is only one bug in the code that we have. Everything works fine and the tables come back mostly similar except for the 
applicant data so that is the applicant race, ethnicity, and those columns. I faced a lot of trouble in creating the relation and figuring out a common 
key for all of those that would work out. It was fine with every other row and everything worked out perfectly for all the other rows however 
because there were some null values and duplicates in the columns that we were using to match applicant and application id we were unable to do it.
That resulted in not being able to use the join function on that and so the data we were unable to put it back into the final csv and that wasn't
taken back in and so we just nulled out the other columns in that section. The data transferred into the smaller tables and the tables contain
everything but it wasn't able to be matched and taken back into the csv. Other than that all of the other columns and all the other data transferred 
over perfectly so if that bug can be figured out it wouldn't have any big issues. Also the loan table transmitted the data but was coming up empty yet 
the data transferred properly in the final csv.


2. Collaboration: Who did you collaborate with on this project? What resources and 
references did you consult? Please also specify on what aspect of the project you collaborated or consulted.

For this project we used a mix of online resources and some help from online group chats as well 
https://stackoverflow.com/questions/20648480/how-to-split-table-into-multiple-tables-using-sql was used for inputting the data into various tables
https://www.w3schools.com/sql/sql_case.asp was used to understand the case expression for inputting some of the data into the tables
https://www.w3schools.com/sql/func_sqlserver_cast.asp was also used so that we could cast and convert some of the datatypes necessary and 
prevent errors that we had a lot of when we first created our tables and tried to input the data using Insert into. 
https://www.youtube.com/watch?v=rBPQ5fg_kiY
https://sqlmct.com/sql-coalesce-function/ 

Assistance from some LLMs on the null or text codes for some of the columns, casting help, coalescing, also some assistance in figuring out how to turn 
it back into the CSV formatting at the end, it helped for this specific cases in our assignment and we ensured to understand the uses of it 
and apply rather than just copying what it helped us with.

3.What are some interesting questions about mortgages in NJ your database can answer?

Our database can answer questions about loan approvals and what other connections that people might have like if ethnicity or 
race makes an impact on loan approvals. Furthermore it could help just a general demographic study so what 
ethnicity applies for mortgages more often and who might be denied more often. You could even query things such as what is the 
reason for most denials in NJ and in what county does it happen most often. 

4. What problems did you face developing code for this project? Around how long did you spend on this project 
(This helps me decide what I need to explain more clearly for the next projects)

We had a lot of issues and time wasted in just having the relations in the database work so that it would give us the exact same csv back. 
Connecting and relating some of the data took a long time and in the end we still couldn't figure it out. There was a lot of 
issues when it came to connecting all the different database components to make sure that they all were able to rejoin and be related after 
everything which ended up in us doing it more manually using the application table to connect all of the other tables. 

In total each group member would have spent between 4-5 hours on the project but the coding members had spent some more time figuring out 
how to get all the relations to work and such.

It would be nice if there was more guidance on example outputs and what you're looking for and more hints towards the complicated stuff especially
for a project that was as tedious at times as this.

5. If you prefer, you can turn in your videos here as links instead of uploading
them to canvas. These links must remain live until you recieve your final grade in
this course, and should include some dating indication such as upload date to show they were done before the deadline.

