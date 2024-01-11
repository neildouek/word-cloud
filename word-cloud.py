from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# Initial list of words related to platform engineering
words = [
    "Plaftorm Engineering", "DevOps", "Microservices", "Cloud Computing", "Containerization", 
    "Kubernetes", "CI/CD", "Infrastructure as Code", "Automation", 
    "Scalability", "Security", "Monitoring", "Logging", "API Management", 
    "Load Balancing", "Service Mesh", "Configuration Management", "Serverless",
    "Data", "Performance Tuning", "High Availability", "Docker", 
    "Version Control", "Network Architecture", "PaaS", "Continuous Deployment",
    "Continuous Integration", "Orchestration", "Virtualization", "Database Management",
    "Fault Tolerance", "Resource Management", "Observability", "Software Lifecycle Management",
    "System Architecture", "Deployment Strategies", "Cloud Services", "Application Lifecycle Management",
    "Artificial Intelligence", "Machine Learning", "Big Data", "Data Science", 
    "Predictive Analytics", "Natural Language Processing", "AI Ethics", 
    "Data Privacy", "Cloud Security", "Intelligent Automation", "IoT", 
    "Blockchain", "Digital Transformation", "Edge Computing", "Cybersecurity",
    "Data Governance", "Cloud Migration", "Business Intelligence", "Neural Networks",
    "Deep Learning", "Data Analysis", "AI Strategy", "Tech Innovation", 
    "User Experience", "Agile Development", "SaaS", "Data Storage", 
    "Tech Consulting", "IT Solutions", "Cloud Solutions", "AI Solutions",
    "Sustainability", "Scalability", "DevSecOps", "Cloud Native", "Gen AI"
]

# Create a frequency dictionary from the words list
word_freq = Counter(words)

# Create a word cloud with the frequency dictionary
wordcloud = WordCloud(width=1600, height=900, background_color='white').generate_from_frequencies(word_freq)

#Set the frequency of "Platform" and "Engineering" to a high value
# This value should be higher than the frequency of any other word in the list
word_freq["Platform Engineering"] = 100


# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()