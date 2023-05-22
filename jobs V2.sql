-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 07, 2023 at 03:03 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uwicareers`
--

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `jobID` int(11) NOT NULL,
  `jobTitle` varchar(255) DEFAULT NULL,
  `employer` varchar(255) DEFAULT NULL,
  `DatePosted` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `jobDescription` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`jobID`, `jobTitle`, `employer`, `DatePosted`, `status`, `email`, `jobDescription`) VALUES
(1, 'Principal', 'UWI Mona Campus', '2023-03-04', 'Full Time', 'hrapplications@fakemails.com', 'The University of the West Indies is conducting an extensive search for Principal of its Mona Campus, and invites expressions of interest, applications and nominations.  The University is looking for a transformational leader with a proven track record and experience in crisis management, to lead the Mona Campus in these challenging times, by attaining Key performance indicators as indicated in its \"Strategic Plan.\" The  successful  applicant  will  be  expected  to  enhance  areas  of strength  and  address present and emerging priorities, which include but are not limited to: digital transformation, reduced funding, capital projects, entrepreneurship, and higher education in emergencies. The Principal  reports  directly  to  the  Vice-Chancellor  and  is  designated  Pro  Vice­Chancellor. He/she is a member of the Executive Management Team of the University and chairs the bodies responsible for the Campus academic, business and financial affairs.'),
(2, 'DSMP-Intern', 'MITS', '2023-04-04', 'Part Time', 'intern-applications@fakemails.com', 'The Digital and Social Media Production Intern will support MITS delivery of audio-visual, multimedia, and communication services to the UWI Mona. The student assistant will have the opportunity to experience the breadth of MITS work and to interact with staff and stakeholders of the UWI on a range of projects. Student assistants can expect to work on a variety of audio-visual, multimedia, and communication projects including supporting the UWI Mona video asset management, the production of web and printed materials for a variety of purposes as well as graphics for the Mona Media website(s), multimedia and social media channels. Additional experience will be in the live video production of campus events and activities as well as engagement for special creative projects. Interns should have the ability to work independently and as a team player in a fast-paced environment, handle multiple tasks at once, and adhere to deadlines.'),
(3, 'Editor', 'UWI Press', '2023-04-08', 'Full Time', 'hrapplications@fakemails.com', 'The successful Editor will have responsibility for managing all non-journal publications produced by the Press from submission to final publication. Reporting to the Director, UWI Press, and the appointee will assume the following duties: Submissions Management, Track all submission entries, Identify appropriate peer reviewers to ensure the integrity of a double blind peer review system, Preparation of submission materials for Press Editorial Committee consideration; Communication with reviewers and Communication with authors. Editorial: Copy-editing and proofreading, Review and revise content for accuracy and quality including spelling, grammar, punctuation, and syntax, Ensure content adherence to House Style and/or Chicago Style, Preparation of files to meet production and publication deadlines.'),
(4, 'Multimedia Technologist', 'Deans Office, Faculty of Medical Sciences', '2023-03-04', 'Full Time', 'hrmd.sed@fakemails.com', 'To provide on and off-site multimedia support services to the Faculty of Medical Sciences for lectures, seminars, conferences, meetings and other events that may require the use of multimedia systems and video conferencing technologies. The successful candidate would be required to: provide technical support (multimedia/recording/editing) to users of the Faculty teaching and learning facilities, provide photographic support services for special events/activities by making arrangements for managing photography sessions and carrying out photography services, as well as editing photos for various use and maintaining photography equipment. Monitors and maintains efficient operation of multimedia systems and video conferencing technologies within the FMS. Provides advice and guidance to internal and external customers of the Faculty on the use of multimedia and videoconferencing equipment. Manages information flows between the Faculty IT Administrator/MITS and users of FMS multimedia and videoconferencing assets to ensure smooth daily operations.'),
(5, 'Administrative Assistant', 'UWI MSBM', '2023-05-04', 'Full Time', 'hrmd.sed@fakemails.com', 'To work collaboratively as part of the Departments administrative team and to fulfil the mission of the Department by providing efficient administrative support .Duties and Responsibilities include: reporting the Head of Department (HOD), the successful candidate will have the following responsibilities: Maintains records of outlines, tutorials, exam papers and other relevant course material. Assists with the co-ordination of the mid-semester examination process. Assists With the checking of marked examination scripts to ensure accuracy in marking and documentation on mark sheets. Meets and greet customers and responds to their need for information and problem resolution. Organizes and maintain a filing system (electronically/manually) of all documents highly confidential and non-confidential and other work related material, ensuring security and easy retrieval. Coordinates the Departments timetable exercise. Assists with the co-ordinating and planning of the Department Summer School activities and other Department events and activities.'),
(6, 'Internship', 'CIBC FCIB', '2023-05-05', 'Part Time', 'cibcfcibtalent@feonbeb.com', 'We are recruiting university students for internships in the following disciplines: Banking,Finance, Economics, Accounting, Computer Science, Information Technology, Data Analytics, Human Resources and Marketing.'),
(7, 'Database Admin', 'Sagicor Group LTD', '2023-05-06', 'Full Time', 'info@sfbwrv.com ', 'Coordinate and execute database administration (DBA) functions for all database platforms for the production environment, the offsite high availability (Disaster Recovery) environment as well as for a significant array of replica development and test environments. Provide specialized database administration support for mission critical systems. Conduct assessments, proactive monitoring and participate in the implementation of all database environments and upgrades. Perform routine system checks as per standards prescribed by the Database Administrator and or the Network Administrator to ensure proper functioning of all Business Systems. Proactively monitor the database systems to ensure secure services with minimum downtime exposure. Periodically review/ update database auditing logs/ log configuration to ensure the security and integrity of the data. Participate in ongoing planning, designing, installing and implementation of all database production, user acceptance testing and development environments.'),
(8, 'Dispatcher', 'PriceSmart', '2023-04-04', 'Full Time', 'pricesmart@psdvnsd.com', 'To ensure the efficiency and productivity of the private fleet. The main duties and responsibilities include: direct report for Drivers and Assistant Drivers making sure to supply and use the right, safe protective accessories, define and assign driver scheduling, planning, controlling, tracing and tracking of loadings to and from the Clubs, Central Manufacturing and Domestic Distribution Centres (DDCs), including deliveries to members, define and design the delivery routes for member delivery and potential replenishment. Private fleet management, ensuring the maintenance, compliance, cleaning and productivity of the resources, control and analysis of private fleet costs, revenue and monthly reporting, manage and report on the Transportation KPIs and manage third party relationships for all transportation modes.'),
(9, 'Sales Representative', 'Alorica', '2023-03-05', 'Full Time', 'alorica@afvrubwoubve.com', 'The responsibilities for the job include: Marketing & sales of products of the client and company brand, maintain a high level of professionalism, field billing inquiries from customers, activate new service provisions, provide plan upgrade information, provide prompt resolution to customer inquiries by providing appropriate and accurate information and maintain diplomacy when addressing escalated matters.'),
(10, 'Real Estate Project Manager', 'Issa Homes Ltd', '2023-02-05', 'Full Time', 'issahome@fdfburwb.com', 'At Issa Homes Ltd, we are looking for an experienced real estate project manager to join our dynamic team and help us deliver high-quality projects on time and within budget. The ideal candidate will have experience managing all aspects of real estate development projects, from feasibility studies and site selection to construction and project close-out. He or she will be a strong leader with excellent communication and negotiation skills, and will be able to effectively manage a team of consultants and contractors. The real estate project manager will also be responsible for developing and maintaining relationships with key stakeholders, such as government agencies, utility companies, and community groups.'),
(11, 'Construction Project Manager', 'Escape Ltd', '2023-05-05', 'Full Time', 'escape@srgri.com', 'We are looking for an experienced Construction Project Manager to plan and supervise a wide range of construction projects from start to ?nish. You will organize and oversee construction procedures and ensure they are completed in a timely, cost effective and effcient manner. Interested persons must be well-versed in all construction methodologies and procedures and able to coordinate a team of professionals of different disciplines to achieve the best results. The ideal candidate will have an analytical mind and great organizational skills. The goal will be to ensure all projects are delivered on time according to requirements and without exceeding budget.'),
(12, 'Window Treatment Technician', 'Hardware & Lumber Ltd', '2023-05-05', 'Full Time', 'shanicejones567890@gmail.com', 'The Window Treatments Technician will safely cut and assemble material to manufacture blinds and awnings within the standards of quality and efficiency to support the timely delivery of customer orders, and positively impact customer satisfaction. '),
(13, 'Accountant', 'JCCUL', '2023-05-05', 'Full Time', 'shanicejones567890@gmail.com', 'The Accountant is responsible for the achievement of the Strategic Accounting Objectives for the Group, paying particular emphasis on the entity assigned while ensuring compliance with regulatory and statutory requirements. The account will be reporting to the Group CFO, the Accountant is responsible for the achievement of the Strategic Accounting Objectives for the Group, paying particular emphasis on the entity/project assigned, while ensuring compliance with regulatory and statutory requirements in order that the JCCUL Group achieves its Mission, Vision and Major Targets in a sustainable manner.'),
(14, 'Treasury Analyst', 'Supreme Ventures Group', '2023-05-22', 'Full Time', 'shanicejones567890@gmail.com', 'The Treasury Analyst is responsible for providing excellent customer service to all clients and personnel. Verifying the accuracy of all transactions and maintaining account integrity, as well as verifying the input into the accounting system.'),
(15, 'Cyber Security Specialist', 'Iterum BPO', '2023-05-21', 'Full Time', 'shanicejones567890@gmail.com', 'The Cyber Security Specialist takes care of the day-to-day operations and data structures by overseeing the operational performance. They configure anti-virus systems and consoles. The professionals must have an in-depth understanding of vulnerabilities management systems and common security applications. They conduct software upgrades and explains performance criteria, documents configurations, and systems specifications. This individual will be an integral part of the Information Technology organization reporting directly to the CIO. The IT Information Security Specialists in cyber security are among the most sought-after professionals in the tech sector as businesses and governments seek to fight off an increasingly daring and ruthless cohort of global cyber criminals and hackers. Skilled and dedicated security specialists work in this field that demands a mix of artistry and technical expertise. They need to be constantly one step ahead of the hackers and organized criminals behind a new crime wave.'),
(16, 'Finance Officer', 'Caribbean Solutions', '2023-04-04', 'Full Time', 'shanicejones567890@gmail.com', 'Reporting to the Branch Manager, the Finance Officer will perform accounting and clerical duties related to the efficient maintenance and processing of accounts payables transactions. These duties include: reparation of branch AR report for IAJ and Branch Manager, monthly accounting for branch business, preparation of Wire Transfer and Local Reinsurance Payments, provide AR support to the Cayman Branch, preparation of reconciliations as part of the Finance Control Framework, flag and clarify any unusual or questionable payment items or transactions, keep track of credits owed to the company and ensure all credits are properly applied to vendor’s payments, research and resolve accounting discrepancies and issues, maintain accurate historical records and accurate accounting files and assist in ensuring the daily operational requirements for Jamaica are maintained.'),
(17, 'Concierge Agent', 'GeeJam Hotel Group', '2023-04-07', 'Full Time', 'shanicejones567890@gmail.com', 'The ideal candidate will possess a positive attitude, collaborative leadership style and be focused on delivering exceptional customer service. You’re a problem solver who takes can take both direction and initiative and just gets it done. This person will pro-actively anticipate the needs of the guests so solutions can be offered before being requested, personalizing the delivery of the service to meet the specific needs of each guest, and reminding the guest of scheduled events and appointments. Your function is to provide the guest with an experience that will always be remembered and with the highest level of responsiveness.'),
(18, 'Administrative Officer', 'Dean Office, Faculty of Medical Sciences', '2023-05-09', 'Full Time', 'shanicejones567890@gmail.com', 'The individual will provide leadership, coordination, and administrative support in the ongoing development, implementation and administration of all curriculum, professional development and academic student-related activities in the MBBS programme. The individual will report to the Dean but work closely with MBBS Programme Director, Deputy Dean Student Success and the Director, Health Professions Education Unit in ensuring effective operation, implementation of administrative systems, procedures and policies, and monitoring related projects and activities.'),
(19, 'Junior Marketing Assitant', 'Kingston Bookshop ', '2023-03-05', 'Full Time', 'shanicejones567890@gmail.com', 'The Social Media Coordinator is responsible for promoting KB’s brand and developing strategies to attract and retain customers. These responsibilities include: provide support in the development of marketing strategies geared towards promoting the Company’s corporate image and growth in market share across multiple sales channels, support the collaboration with advertising agencies to develop promotional material in alignment with the Company’s image and strategic direction, assist with the design of marketing and promotional material such as brochures, pamphlets and assist in the development of the marketing budget.'),
(20, 'Supply Chain Manager', 'Digicel', '2023-11-04', 'Full Time', 'shanicejones567890@gmail.com', 'The position holder will lead the transformation and leadership of the Group Supply Chain Function, operating across all 25 markets. The individual will need to possess a combination of Commercial, Supply Chain, Logistics and Warehouse Management domain knowledge and experience. The role holder will need to think as an entrepreneur in creating commercial opportunities, leveraging market knowledge and working as a true business partner in problem solving and delivering a world class Supply Chain Service. Confident working within a fast paced, action orientated setting, the position holder will partner with vendors and internal stakeholders in managing multi-site and critical supply chains, delivering value for Digicel and its customers.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`jobID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
