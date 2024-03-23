# Web-Scraping-Analysis-Clustering-on-Real-time-data
This project aims to perform data analysis and clustering on the Reddit Tech forum. It involves web scraping, data preprocessing, topic selection, clustering algorithms, and real-time data processing. The project is divided into two parts: data collection and storage, and forum analysis &amp; clustering algorithms.

## 1. Initial Setup

### Tools / Libraries Used:
1. Requests/Selenium: These tools are employed for web scraping, enabling the extraction of data from web pages. Requests is used for making HTTP requests to retrieve HTML content, while Selenium automates web browser interaction, allowing dynamic page scraping.
2. BeautifulSoup4: This library is utilized for parsing HTML content obtained through web scraping. It provides convenient methods and data structures for navigating, searching, and modifying parsed HTML documents.
3. MySQL Database: The project leverages MySQL as the database management system for storing the collected data. MySQL offers robust features for managing relational databases, ensuring efficient storage and retrieval of structured data.

## 2. Data Collection / Storage
1. Resource: The project focuses on extracting data from the Reddit Tech forum (r/tech). This forum serves as a rich source of discussions, news, and insights related to various technology topics.
2. Web Scraping Method: The Praw API is utilized for web scraping, offering convenient access to Reddit's data through Python. Praw simplifies the process of fetching posts, comments, and other forum content.
3. Script Functionality: A Python script is developed to fetch posts from the Reddit forum, ensuring that it can handle large requests efficiently. The script preprocesses the collected data and stores it in a MySQL database for further analysis.
## 3. Data Preprocessing
### Preprocessing Steps:
Removal of HTML tags, special characters, and irrelevant information such as advertisements and promoted messages.

Conversion of timestamps to a standard format for consistency and ease of analysis.

Masking of user names to maintain data privacy and confidentiality.

Identification of keywords and topics based on message content, enabling the creation of additional fields in 
the database for storing this metadata.

Extraction of text from embedded images using image recognition tools like pytesseract, enhancing the comprehensiveness of the data analysis.

### Resources:
Handling Missing Data with Pandas: Pandas library is utilized for handling missing data, providing powerful tools for data manipulation and analysis.

Keyword Extraction: Natural Language Processing (NLP) techniques are employed for keyword extraction, enabling the identification of important terms and phrases within the forum content.

## 4. Forum Analysis & Clustering Algorithms

### Message Content Abstraction

Method Used: The project employs Doc2Vec for message content abstraction. Doc2Vec is a neural network-based approach that learns distributed representations of documents, enabling the conversion of messages into fixed-dimensional vectors representing their meanings.

Functionality: Doc2Vec facilitates the creation of vector representations for each message, which are stored in the database alongside the cleaned message text.

### Clustering Messages

Clustering Algorithm: A simplified clustering algorithm is developed based on the keywords extracted from the text. The algorithm groups similar messages together into clusters, enabling the identification of common themes and topics within the forum content.

Libraries Used: Scikit-Learn, NLTK Python, TextBlob are employed for clustering tasks, providing a range of clustering algorithms and NLP functionalities.

Visualization: The project utilizes visualization tools such as Matplotlib to display the clusters and their associated keywords in a visually informative manner.

### Automation

Script Functionality: An automation script is developed to periodically update the database with new forum data. The script runs at fixed intervals, fetching fresh data, preprocessing it, and storing it in the database for real-time analysis.

Input: The script takes an interval (in minutes) as input from the user, ensuring flexibility in scheduling the data update process.

Error Handling: The automation script includes error handling mechanisms to provide informative messages in case of failures during data collection, preprocessing, or database updates.
## Libraries/Tools/Technologies Used:

- Python: The project is implemented using Python, a versatile programming language known for its simplicity and readability.

- Requests/Selenium: These tools facilitate web scraping, allowing the project to fetch data from web pages efficiently.
- BeautifulSoup4: This library aids in parsing HTML content obtained through web scraping, enabling structured data extraction.
- MySQL Database: MySQL serves as the database management system for storing and managing the collected forum data.
- Pandas: Pandas is used for data manipulation and analysis tasks, providing powerful tools for working with structured data.
- Doc2Vec: Doc2Vec is employed for message content abstraction, enabling the conversion of text data into fixed-dimensional vectors.
- Scikit-Learn: Scikit-Learn provides a range of machine learning algorithms and tools, including clustering algorithms used in this project.
- NLTK Python: NLTK offers a suite of libraries and programs for NLP tasks, enhancing the project's capabilities in text processing and analysis.
- TextBlob: TextBlob is utilized for text processing tasks, providing functionalities for tasks such as sentiment analysis and part-of-speech tagging.
- Matplotlib: Matplotlib is employed for data visualization, enabling the creation of informative plots and charts to visualize clustering results.

## Conclusion

This project demonstrates the application of various techniques and tools for comprehensive data analysis and clustering on the Reddit Tech forum. By leveraging web scraping, data preprocessing, and clustering algorithms, valuable insights can be extracted from the forum's content, facilitating a deeper understanding of technology-related discussions and trends. The automation aspect ensures the continuous updating of the database for real-time analysis, enabling timely decision-making and insights generation.
