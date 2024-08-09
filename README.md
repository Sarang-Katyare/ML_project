In this project, I developed a machine learning model to predict real estate prices based on various property attributes. The data was scraped from Domain.com.au, a popular Australian real estate website.I utilized web scraping techniques to gather data from Domain.com.au. Once the data was collected, I imported it into a Pandas DataFrame. This involved cleaning the data by handling missing values, outliers, and ensuring consistency in data types.I selected the dependent variable as price and used the independent variables bedrooms, bathrooms, parkings, area, and state to train the model. Multiple machine learning algorithms were experimented with, including linear regression, decision trees, and ensemble methods, to find the best model for predicting property prices.I used catboost model since it gave the best r2 score. I then created a user-friendly web interface using Flask, a lightweight web framework.
