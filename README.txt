README file
-----------
You must also submit a README file (named README.txt) with clearly
delineated sections for the following.

0. Please write down the full names and netids of both your team members.
Harsh Borkhetaria hpb34
Cleon Monis cvm53
Sameel Arif sma369
Saanvi Pandey sp2404

1. Are there known issues or functions that aren't working currently in your
attached code? If so, explain. (note that you will get half credit for any reasonably sized bug that is fully explained in the readme)

No, there are no known issues or functions that aren’t working currently in our attached code. 

2. Collaboration: Who did you collaborate with on this project? What resources and
references did you consult? Please also specify on what aspect of the project you
collaborated or consulted.

For uploading the data to the database and copying all the information we used these online sources: 
https://www.youtube.com/watch?v=a5jYqMRIrVE 
https://neon.tech/postgresql/postgresql-tutorial/import-csv-file-into-posgresql-table
https://www.w3schools.com/sql/sql_primarykey.ASP 

These three sources were mainly used for the database part of it, because we needed to import the csv file and then also create the table and finally to add the column for id using ALTER TABLE so we referred to online for guidance and changed as required. 

Collaborated on the SQL script and some aspects of it.

3. What useful insights can you get from this data? What rules did you use for
dividing up the attributes into entities?

This data set enables us to derive insights about loan approvals, the demographic of loan applicants, and geographic disparities. For example, the loan_details table lets us calculate the percentage of approved loan applications and how the approval rates vary by loan type. We can also analyze the reasons for denial and display the most common ones. We can also see if denials reasons correlate with income levels, race, or geographic location. With the data on agencies, we can figure out which lenders have the highest and lowest approval rates. We can also check whether lenders favor specific income levels or races.

When splitting the attributes into different entities, we tried to tie each entity to a distinct business concept. For example, the loan_details table stores information only related to the loan itself. The applicants table strictly stores information about the borrower and co-borrower, and so on.  This pattern ensures a logical separation of concerns and makes the data easier to analyze. We also made sure to reduce any redundancy by storing repeated data in separate tables. An example of this is storing the agency details in the “agencies” table instead of storing its 3 columns in every loan record. Using foreign keys, we can reference PKs from other tables to establish connections throughout the data.

4. What problems did you face developing code for this project? Around how long did
you spend on this project (This helps me decide what I need to explain more clearly
for the next projects)

We weren’t able to use COPY for uploading the data and then the terminal gave a hint to use \copy. 
Spent about 1.5-2 hours for uploading the database to postgres, creating the table and adding new column, verifying the data.
Also took some time to decipher the output because it does seem to be a mess when printed in the terminal so maybe some guidance on what we should expect.
We initially had some issues with being able to share the table but were able to figure it out with a quick Google search.
