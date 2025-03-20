# Tony-the-Slice-bot

1.1	Purpose 
The purpose of this project is to develop Slice Bot, an AI-powered chatbot for the Slice restaurant. It will integrate with the restaurant’s website to automate customer interactions, facilitating order placement, reservations, and inquiries. The chatbot aims to enhance service efficiency and improve the overall customer experience through intelligent and responsive communication.
1.2	Document Conventions
•	Uses IEEE SRS format.
•	Requirements are uniquely labeled (e.g., REQ-1, REQ-2) for easy tracking.
•	Technical terms are defined in the Glossary.
1.3	Intended Audience and Reading Suggestions
This document is intended for:
•	Restaurant Owners: Evaluate chatbot impact on customer experience.
•	Developers: Implement chatbot functionalities.
•	Testers: Ensure proper integration and functionality.
Project Scope
Tony the Slice-Bot will provide:
•	Order placement & customization.
•	Real-time order tracking.
•	Table reservations.
•	Menu assistance.
•	FAQ support.
•	Loyalty rewards system.

1.4	References
Dialogflow. (n.d.). Google Cloud. https://cloud.google.com/dialogflow/docs
API — Flask Documentation (3.1.x). (n.d.). https://flask.palletsprojects.com/en/stable/api/
MySQL Integration | Elastic integrations | Elastic. (n.d.). Elastic. https://www.elastic.co/guide/en/integrations/current/mysql.html

2.	Overall Description
2.1	Product Perspective
Tony the Slice-Bot is a standalone AI chatbot integrated with the Slice restaurant’s website. It enhances customer interaction through automation and personalization.
2.2	Product Features
AI-powered chatbot using Dialogflow
•	AI-powered chatbot using Dialogflow.
•	Seamless website integration.
•	Order management & tracking.
•	Table reservations.
•	Customer support for FAQs.
•	Loyalty rewards tracking.

2.3	User Classes and Characteristics
•	Customers: Place orders, book tables, and inquire about menu options.
•	Restaurant Staff: Manage orders and customer interactions.
•	Administrators: Oversee chatbot functionality, update menus, and analyze interactions.

2.4	Operating Environment
•	Web-based, accessible via Chrome, Firefox, and Edge.
•	Backend powered by Flask and MySQL.
•	Chatbot integration using Google Dialogflow API.


2.5	Design and Implementation Constraints
•	The chatbot must integrate seamlessly with the Slice restaurant’s existing website and backend systems.
•	The system must use Flask for backend processing and MySQL for database management.
•	Google Dialogflow API will be used for natural language processing (NLP).
•	Secure API implementation is required to protect user data and transactions.
•	The chatbot should be optimized for both desktop and mobile platforms.
•	It must ensure minimal latency, with responses delivered within 2 seconds.

2.6	User Documentation
·	User Manual
·	Administrator Guide

2.7	Assumptions and Dependencies
The chatbot will rely on Google Dialogflow for NLP processing.
	The reason we are using Dialogflow API over any other API for chatbot integration is given below:
Feature	Dialogflow (by Google)	Other APIs (e.g., Rasa, Microsoft Bot Framework, IBM Watson)
Ease of Integration	Easy integration with Google services, websites, and third-party platforms	Some APIs require more manual setup and custom development
Natural Language Processing (NLP)	Advanced NLP with Google’s AI, supports intent recognition and context handling	Varies by API, some may require external NLP services
Pre-built Models	Comes with pre-trained models for common use
cases	Many APIs require custom training from scratch
Multi-language Support	Supports multiple languages with built-in translation	Some APIs may require manual language setup
Voice and Text Support	Supports both voice and text-based interactions	Some APIs focus only on text or require additional setup for voice
Machine Learning Capabilities	Google’s AI enhances intent detection and entity recognition over time	Varies, some require external ML models
Cost	Free tier available; pay-as-you-go pricing for advanced features	Some APIs have high pricing for premium features
Deployment Options	Cloud-based with easy web and mobile integration	Some APIs require on-premise setup (e.g., Rasa)
Customization	Allows custom training but has some limitations	More customizable in some alternatives like Rasa
Security & Compliance	Follows Google’s security standards and compliance	Varies depending on the API provider
Integration with Other Tools	Seamless with Google services (Firebase, Google Assistant, etc.)	May require additional effort for third-party integration

3.	System Features
3.1	Order Management
Priority: High
Description: Customers can place, modify, and track orders.
Functional Requirements:
•	REQ-1: Display menu options and take orders.
•	REQ-2: Provide real-time order tracking.
•	REQ-3: Allow users to modify or cancel orders.

3.2	Customer Support
Priority: Medium
Description: Provides responses to FAQs and assists with navigation.
Functional Requirements:
•	REQ-4: Automate responses to FAQs.
•	REQ-5: Guide users through website navigation.

3.3	Table Reservations
Priority: Medium
Description: Users can check table availability and book reservations.
Functional Requirements:
•	REQ-6: Display table availability.
•	REQ-7: Confirm and manage reservations.

3.4 Loyalty Rewards
Priority: Low
Description: Users can earn and redeem reward points.
Functional Requirements:
•	REQ-8: Track user reward points.
•	REQ-9: Apply rewards to orders.

4.	External Interface Requirements
4.1	User Interfaces
•	The chatbot interface shall be embedded within the Slice website.
•	A pop-up chat window will appear when users click the chat icon.

 

4.2	Hardware Interfaces
Hosted on a cloud-based server with necessary processing power.
4.3	Software Interfaces
•	The chatbot shall integrate with Google DialogFlow for natural language processing.
•	The system shall use Flask API for backend interactions and MySQL for data management.
•	The chatbot shall communicate with the restaurant’s ordering and reservation system to process user requests.
•	APIs shall be used to fetch and update restaurant information, menu details, and order statuses.
4.4	Communications Interfaces
•	The chatbot shall communicate using HTTPS protocols.
•	Secure authentication for user data protection.

5.	Other Nonfunctional Requirements
5.1	Performance Requirements
•	The chatbot shall respond to user queries within 2 seconds.
•	The system shall support up to 100 concurrent users.
5.2	Safety Requirements
•	The system shall comply with relevant data protection regulations (e.g., GDPR).
•	User data shall be encrypted in transit (SSL/TLS) and at rest.
•	Access control and regular security audits shall be implemented.
•	A data backup and recovery plan shall be in place.
5.3	Security Requirements
•	API communications shall use HTTPS for secure data transmission.
•	Secure authentication (e.g., JWT or OAuth) shall be implemented.
•	Prepared statements shall be used in MySQL to prevent SQL injection.
•	Input validation and sanitization shall be applied to prevent XSS.
•	Third-party APIs shall comply with security and data protection standards.
•	The system shall be regularly patched to fix security vulnerabilities.
5.4	Software Quality Attributes
•	Usability: The chatbot should be user-friendly and intuitive.
•	Reliability: The chatbot must handle unexpected queries using fallback intent.

6.	Other Requirements
•	The chatbot shall allow users to provide feedback and ratings on their interaction experience.
•	The chatbot should offer proactive order suggestions based on user preferences and past orders.

Appendix A: Glossary
A
•	API: Set of protocols for building software applications, enabling communication between the chatbot, backend, and external services like Dialogflow.
B
•	Backend: Server-side component handling data processing, storage, and business logic. Uses Flask and MySQL in this project.
C
•	Chatbot: AI-powered app simulating human conversation, assisting with orders, reservations, and FAQs.
•	Concurrent Users: Number of users interacting with the system at once; supports up to 100 users.
D
•	Dialogflow: Google Cloud's NLP platform for building conversational interfaces like chatbots.
•	Data Encryption: Converting data into a secure format to prevent unauthorized access, using SSL/TLS in transit and at rest.
E
•	ERD: Diagram showing data model, entities, attributes, and relationships; used to design the chatbot’s database.
F
•	FAQ: List of common questions and answers; the chatbot automates responses to improve support.
•	Flask: Lightweight Python framework for backend development, handling API requests and database interaction.
•	Fallback Intent: Default response in Dialogflow when the chatbot cannot match a query.
G
•	GDPR: EU regulation ensuring data protection and privacy, complied with in handling user data.
H
•	HTTPS: Secure protocol for transmitting data; used by the chatbot to ensure data security.
I
•	Integration: Combining software components into a unified system; Tony the Slice-Bot integrates with the website, Dialogflow, and payment gateways.
•	JWT: Secure method for transmitting authentication data as a JSON object.
L
•	Loyalty Rewards: System tracking customer loyalty points; managed by the chatbot.
M
•	MySQL: Relational database for managing chatbot data such as orders and customer information.
N
•	NLP: AI branch enabling machines to understand and respond to human language; used by the chatbot through Dialogflow.
O
•	Order Management: Handling customer orders, including placement and tracking; the chatbot manages real-time order updates.
•	Payment Gateway: Service processing online payments securely, integrated into the chatbot.
•	Performance Requirements: System specifications for responsiveness and scalability; designed to respond in 2 seconds with 100 concurrent users.
R
•	Reservation Management: Handling table bookings, including availability and confirmations; automated by the chatbot.
•	REQ: Unique identifier for requirements in the SRS (e.g., REQ-1, REQ-2).
S
•	SRS: Document detailing system requirements; serves as the SRS for Tony the Slice-Bot.
•	SQL Injection: Security vulnerability; mitigated using prepared statements in MySQL.
•	SSL/TLS: Protocols securing data transmission; used by the chatbot for encryption.
T
•	Table Reservations: Booking process for restaurant tables; managed by the chatbot for availability and reservations.
U
•	UI: Visual and interactive part of the system; the chatbot’s UI appears as a pop-up on the restaurant's website.
•	Usability: Measure of how user-friendly and intuitive the system is.
X
•	XSS: Security vulnerability from malicious scripts; input validation and sanitization prevent it.

Appendix B: Analysis Models
•	Data Flow Diagram:
 

•	Entity-Relationship Diagram
 
•	Use Case Diagram:
 

Appendix C: Issues List
•	Challenges in setting up real-time order tracking and ensuring accuracy.
•	Difficulties integrating the chatbot with a cloud-based infrastructure for scalability.
•	Potential issues in providing multi-language support for diverse customers.
•	Ensuring data security and compliance with privacy regulations.
•	Handling unexpected queries and improving chatbot response accuracy.
•	Refining chatbot's ability to manage order modifications and cancellations efficiently.


To run the code:
1. Download this respository
2. Open folder using VS code.
3. In terminal, opne to the folder where q.py is present and type "python q.py"
4. You will recieve a link, which you can click on which leads you to your browser where the website runs.
