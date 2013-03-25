OLPC Contributor Application
============================

1. Project Title & Shipment Detail
Name of Project: Platipy (http://platipy.org)
Shipping Address You've Verified:
521 Hunt Club Road
#24K (Austin Cory Bart, 302-384-2729)
Blacksburg, VA, 24060
Number of Laptops (or other hardware) You Request to Borrow:
	9 XO laptops
?	3 XO 1.0s
?	3 XO 1.5s
?	3 XO 1.75s
Loan Length�How Many Months:
	1 year
2. Team Participants
Name(s) & Contact Info: (include all email addresses & phone numbers)
?	Austin Cory Bart (acbart@vt.edu, 302-384-2729)
?	Robert Deaton (rdeaton@udel.edu, 302-242-5287)
?	Eric McGinnis (ericmcg@udel.edu, 610-628-0220)
Employer and/or School:
?	Austin Cory Bart: Graduate student at Virginia Tech
?	Robert Deaton: Undergraduate student at University of Delaware
?	Eric McGinnis: Graduate student at University of Delaware
Past Experience/Qualifications:
?	Austin Cory Bart (http://www.acbart.com)
?	Honors Bachelor of Science Degree in Computer Science with Distinction from the University of Delaware
?	Experience using Python for 3 years
?	Student in Educational Game Design class for two semesters
?	Contributor to Spyral
?	Primary developer of Conspyre
?	Author of Broadway and Wacky Writer
?	Author of Platipy
?	Robert Deaton
?	Bachelor of Science Mathematics, Computer Science, University of Delaware
?	Teaching Assistant for Educational Game Design class that uses XO laptops
?	Primary developer of Spyral
?	Contributor to Conspyre
?	Author of Platipy
?	Eric McGinnis
?	Bachelor of Science Degree in Computer Science from the University of Delaware
?	Teaching Assistant for Educational Game Design class that uses XO laptops
?	Experience teaching Scratch
?	Author of Platipy

3. Objectives
Project Objectives: (http://platipy.org/pages/contributor-application.html)
	The overarching objective of the Platipy project is to provide tools and guides to develop educational games for the XO laptop. Our team wants to provide not just an educational experience for programmers, but also spur developers to create new, useful activities for children.
	Specifically, our goals for this project are to develop and/or create the following tools:
?	Spyral: A pure-Pygame game development library. Offers a number of very powerful features, including automatic dirty rendering, actor-oriented programming (using greenlets), and a convenient API. Sits on top of Pygame completely, insulating the user from its intricacies. Status: Most of the interface and core functionality is established, although a lot of details need to be fleshed out, such as the Style system and Widgets. Some additional work needs to be done to make it a full Pygame replacement, e.g. replacing the audio modules. Progress can be tracked on Spyral�s Github.
?	Example.Activity: A template activity that greatly simplifies XO activity development. Contains powerful features for developing Spyral-based activities off the XO, including handling translations, game scaling for non-XO resolutions, and packaging the game for the XO and other platforms such as Windows and Mac. Status: Most core functionality is complete, including profiling and scaling. However, non-XO packaging still needs work. 
?	Platipy Docs: A complete guide for Python, XO activity, and Spyral development. Will also include a curated gallery of completed Spyral-based XO activities. Status: The first version of the Python guide is roughly 75%, but needs editing. The XO Activity development is mostly finished. Spyral documentation is out of date. There is currently no gallery.
?	Conspyre: A networking server framework and client library for school-based XO distributions that provides data persistence (in case of students not being allowed to own XOs) and student/teacher communication (especially with bad network connections) with minimal developer work. Designed to work directly with Spyral. Status: The current version needs to be rewritten, and the client-side front-end needs work. Consideration for network outages needs to be added to its core functionality. Lot�s of work needs to be done with this.
4. Plan of Action
Plan and Procedure for Achieving the Stated Objectives:
	Our plan of action is to iteratively develop our tools and deploy them in classroom settings and to the greater Python and OLPC communities. Using feedback from users we�ll continually improve our systems with greater stability and innovative features.
5. Needs
Why is this project needed?
	Presently, XO game development can be a harrowing task for beginners. Although true novices have Scratch, when they want to move onto more complicated programming their options are limited. PyGTK is more suitable for complicated applications, and neither Flash or Java has gained traction on the platform. HTML/Javascript game development is progressing, but suffers from speed and internet connectivity issues. Efforts to create a new language (KAGE) seem to have stalled, and the utility of teaching children a completely artificial game development language could be considered controversial. Pygame has historically been a favorite choice for game development.
However, Pygame is still an unnecessarily complicated system; for instance, do beginners need to comprehend the difference between the six different kinds of Groups that are available in Pygame? And the software engineering principles engendered by Pygame are very weak, with most games completely breaking from Model-View-Controller. Finally, most Pygame games suffer from being highly unoptimized, due to the high learning curve associated with understanding how best to optimize a Pygame game. XO activity development itself is also a difficult prospect, with XO files having a very precise and unforgiving structure. This can be a discouraging barrier for novice programmers from contributing to the program.
Locally?
	Locally, the University of Delaware works with the Chester Community Charter School by teaching a course to undergraduate Computer Science majors about educational game development. Early iterations of the class suffered from spending an inordinate amount of time teaching how to program in Pygame, severely detracting from the quality of the games produced. After several iterations of the class, Robert Deaton created Spyral to simplify many of the common difficulties encountered and to provide a number of optimizations to the platform (e.g. automatic dirty sprite updating). At present, Spyral is used extensively in the class as a full Pygame replacement. Although still not in it�s complete form, Spyral has already had an improvement on the games produced in the classroom, as evidenced by a small research study we�ve conducted where we compared games created pre- and post- Spyral in the Delaware class (http://platipy.org/publications/CHEP_2013.pdf). The games produced post-spyral are also available on our website (http://platipy.org/pages/games.html).
	As Spyral will be used for the foreseeable future in this class, it is very important that it continues to be developed along with its associated tools Conspyre, Platipy Docs, and Butterpy.
In the greater OLPC/Sugar community?
	The tools being generated as a result of this project have great potential to be used by the broader Sugar community to develop games; they are open-source, free, powerful, and flexible tools for game development and thus can be used by anyone to make any kind of game.
Outside the community?
	Spyral and its associated tools have great potential to be used outside of the project. In fact, Spyral is compatible with any system that provides Pygame, including the Raspberry Pi and Android (using the Pygame for Android Subset). 
Why can't this project be done in emulation using non-XO machines?
	Ultimately, rigorous testing is required in order to gauge the performance of our systems. Developing on a modern desktop computer will not give realistic information about the speed, reliability, etc. of a program on the XO. For that reason, we need XO laptops to develop on and test our examples and conduct unit/integration tests on. 
Why are you requesting the number of machines you are asking for?
Will you consider (1) salvaged/rebuilt or (2) damaged XO Laptops?
We can consider them, but damaged XOs might affect the results of our performance tests. Using them would be potentially suboptimal.

6. Sharing Deliverables
Project URL�where you'll Blog specific ongoing progress:
http://platipy.org
How will you convey tentative ideas & results back to the OLPC/Sugar community, prior to completion?
	Our primary form of communication will be through the official Platipy blog. However, as a natural consequence of our development process, we�ll be keeping all of our respective githubs up-to-date. Additionally, we will contact the OLPC listservs, news outlets, and relevant online communities at important milestones.
How will the final fruits of your labor be distributed to children or community members worldwide?
	All resources generated by this project will be available on public facing websites. Additionally, we will update official resources such as the Laptop Wiki with links and information pertaining to using our tools. Finally, we will notify the relevant blogs and news sources after each important release.
Will your work have any possible application or use outside our community?
Yes, our work will have extensive application outside of the OLPC community as previously
 described. We will use similar means to reach out to external communities, including contacting news sources, posting on sites like r/python, etc.
Have you investigated working with nearby XO Lending Libraries or Project Groups?
	We will be working with the Project Group at the University of Delaware and the XO distribution at Chester Community Charter School. Austin will be investigating establishing a Project Group at Virginia Tech, as there are no groups local to that area.
7. Quality/Mentoring
Would your Project benefit from Support, Documentation and/or Testing people?
	Yes. Software should always be tested, and we can benefit from having external eyes.
Teachers' input into Usability?
	Minimally. Most of our work is oriented towards developers, not teachers.
How will you promote your work?
	Through an official blog, online technology communities such as Hacker News, r/python, etc., and the official OLPC listservs.
Can we help you with an experienced mentor from the OLPC/Sugar community? 
Yes, an experienced mentor could be useful, who would be knowledgeable about the ways that our project could be fit into the OLPC/Sugar community.

8. Timeline (Start to Finish)
Please include a Proposed timeline for your Project life-cycle: (this can be in the form of Month 1, Month 2, etc rather than specific dates)
a.	Month 1: 
i.	Finished version 1.0 of Spyral (complete current todo.txt in github)
b.	Month 2:
i.	Finished version 1.0 of Platipy Docs (complete current todo.txt in github)
c.	Month 3:
i.	Finished version 1.0 of Example.Activity (complete current todo.txt in github)
d.	Month 4:
i.	Finished version 1.0 of Conspyre (complete current todo.txt in github)
e.	Month 5-12:
i.	Iteratively improve the products
Specify how you prefer to communicate your ongoing progress and obstacles!
Through our official blog (http://platipy.org)
[X] I agree to pass on the laptop(s) to a local OLPC group or other interested contributors in case I do not have need for the laptop(s) anymore or in case my project progress stalls.

