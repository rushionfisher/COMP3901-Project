CREATE DATABASE JobListings;

use JobListings;

CREATE TABLE jobs(
    jobID int NOT NULL ,
    jobTitle varchar(255),
    employer varchar(255),
    DatePosted date,
    status varchar(255),
    email varchar(255),
    jobDescription LONGTEXT,
    PRIMARY KEY (jobID)
);




INSERT INTO `jobs` (`jobID`, `jobTitle`, `employer`, `DatePosted`, `status`, `email`, `jobDescription`) VALUES
(1, 'Principal', 'UWI Mona Campus', '2023-03-04', 'Full Time', 'hrapplications@uwimona.edu.jm', 'The University of the West Indies is conducting an extensive search for Principal of its Mona Campus, and invites expressions of interest, applications and nominations.  The University is looking for a transformational leader with a proven track record and experience in crisis management, to lead the Mona Campus in these challenging times, by attaining Key performance indicators as indicated in its \"Strategic Plan.\" The  successful  applicant  will  be  expected  to  enhance  areas  of strength  and  address present and emerging priorities, which include but are not limited to: digital transformation, reduced funding, capital projects, entrepreneurship, and higher education in emergencies. The Principal  reports  directly  to  the  Vice-Chancellor  and  is  designated  Pro  Vice­Chancellor. He/she is a member of the Executive Management Team of the University and chairs the bodies responsible for the Campus academic, business and financial affairs. The Principal is responsible to the Vice-Chancellor for ensuring that the Campus makes the best possible contribution to the educational, social and cultural advancement of the Region and particularly to Jamaica. He/She is directly responsible for the maintenance and promotion of the security, efficiency and good order of the Campus, and addressing the Industrial Relations matters. The Principal shall also be responsible for the attainment of Key Performance Indicators as indicated in the Triple A Plan.'),
(2, 'DSMP-Intern', 'MITS', '2023-04-04', 'Part Time', 'intern-applications@uwimona.edu.jm', 'The Digital and Social Media Production Intern will support MITS delivery of audio-visual, multimedia, and communication services to the UWI Mona. The student assistant will have the opportunity to experience the breadth of MITS work and to interact with staff and stakeholders of the UWI on a range of projects. Student assistants can expect to work on a variety of audio-visual, multimedia, and communication projects including supporting the UWI Mona video asset management, the production of web and printed materials for a variety of purposes as well as graphics for the Mona Media website(s), multimedia and social media channels. Additional experience will be in the live video production of campus events and activities as well as engagement for special creative projects. Interns should have the ability to work independently and as a team player in a fast-paced environment, handle multiple tasks at once, and adhere to deadlines. Excellent verbal and written communication skills.'),
(3, 'Editor', 'UWI Press', '2023-04-08', 'Full Time', 'hrapplications@uwimona.edu.jm', 'The successful Editor will have responsibility for managing all non-journal publications produced by the Press from submission to final publication. Reporting to the Director, UWI Press, and the appointee will assume the following duties: Submissions Management, Track all submission entries, Identify appropriate peer reviewers to ensure the integrity of a double blind peer review system, Preparation of submission materials for Press Editorial Committee consideration; Communication with reviewers and Communication with authors. Editorial: Copy-editing and proofreading, Review and revise content for accuracy and quality including spelling, grammar, punctuation, and syntax, Ensure content adherence to House Style and/or Chicago Style, Preparation of files to meet production and publication deadlines.'),
(4, 'Multimedia Technologist', 'Deans Office, Faculty of Medical Sciences', '2023-03-04', 'Full Time', 'hrmd.sed@uwimona.edu.jm', 'To provide on and off-site multimedia support services to the Faculty of Medical Sciences for lectures, seminars, conferences, meetings and other events that may require the use of multimedia systems and video conferencing technologies. The successful candidate would be required to: provide technical support (multimedia/recording/editing) to users of the Faculty teaching and learning facilities, provide photographic support services for special events/activities by making arrangements for managing photography sessions and carrying out photography services, as well as editing photos for various use and maintaining photography equipment. Monitors and maintains efficient operation of multimedia systems and video conferencing technologies within the FMS. Provides advice and guidance to internal and external customers of the Faculty on the use of multimedia and videoconferencing equipment. Manages information flows between the Faculty IT Administrator/MITS and users of FMS multimedia and videoconferencing assets to ensure smooth daily operations. '),
(5, 'Administrative Assistant', 'UWI MSBM', '2023-05-04', 'Full Time', 'hrmd.sed@uwimona.edu.jm', 'To work collaboratively as part of the Departments administrative team and to fulfil the mission of the Department by providing efficient administrative support .Duties and Responsibilities include: reporting the Head of Department (HOD), the successful candidate will have the following responsibilities: Maintains records of outlines, tutorials, exam papers and other relevant course material. Assists with the co-ordination of the mid-semester examination process. Assists With the checking of marked examination scripts to ensure accuracy in marking and documentation on mark sheets. Meets and greet customers and responds to their need for information and problem resolution. Organizes and maintain a filing system (electronically/manually) of all documents highly confidential and non-confidential and other work related material, ensuring security and easy retrieval. Coordinates the Departments timetable exercise. Assists with the co-ordinating and planning of the Department Summer School activities and other Department events and activities.'),
(6, 'Internship', 'CIBC FCIB', '2023-05-05', 'Part Time', 'cibcfcibtalent@cibcfcib.com', 'We are recruiting university students for internships in the following disciplines: Banking,Finance, Economics, Accounting, Computer Science, Information Technology, Data Analytics, Human Resources and Marketing.'),
(7, 'Database Admin', 'Sagicor Group LTD', '2023-05-06', 'Full Time', 'info@sagicor.com ', 'Coordinate and execute database administration (DBA) functions for all database platforms for the production environment, the offsite high availability (Disaster Recovery) environment as well as for a significant array of replica development and test environments. Provide specialized database administration support for mission critical systems. Conduct assessments, proactive monitoring and participate in the implementation of all database environments and upgrades. Perform routine system checks as per standards prescribed by the Database Administrator and or the Network Administrator to ensure proper functioning of all Business Systems. Proactively monitor the database systems to ensure secure services with minimum downtime exposure. Periodically review/ update database auditing logs/ log configuration to ensure the security and integrity of the data. Participate in ongoing planning, designing, installing and implementation of all database production, user acceptance testing and development environments. Responsible for improvement and maintenance of all databases to include rollout, upgrades and migrations. Perform backups and restoration of production, User Acceptance Testing and Development database environments. Provide trend analysis to the management team to enable them to make informed decisions regarding resource management. Work with the infrastructure team to ensure that the associated hardware resources are allocated to the databases, in order to ensure high resilience and performance tuning. Be responsible for the troubleshooting and problem solving of all development environments.');
