# Python_Content_Aggregator_WebApp
Content Aggregator
A Python-based web application developed using Django that collects, analyzes, and organizes content from multiple websites to simplify information retrieval. Users can input a search term, and the aggregator scrapes pre-selected websites stored in a database, retrieves relevant articles, and ranks them by relevance using an algorithm.
Key Features:
Scrapes content from sources like Wikipedia, Sky Sports, and Euro News using custom parameters for each site.
Allows users to add or remove websites in the database, with manual configuration for site-specific scraping rules.
Implements a FastDamerauLevenstein algorithm for ranking search results based on accuracy and proximity to the search term.
Utilizes Django for backend development, SQLite for database management, and HTML/CSS with a Colorlib template for the frontend design.
Challenges and Solutions:
Addressed the variability in site structures by customizing scraping rules for each site.
Leveraged virtual environments for package management to avoid conflicts across projects.
Designed the project to be extensible, enabling future integration with more websites or features.
This project was completed as the final examination for my Software Engineering Program, showcasing my ability to combine Python expertise, web development skills, and algorithmic thinking.
