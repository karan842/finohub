# FinoHub®
<img src='https://github.com/karan842/finohub/blob/master/media/FinoHub.png' height=290px width=300px></img>

- AI driven loan eligibility prediction webapp💵🤖
[Click Here](http://finohub-env-1.eba-fcih6jie.us-east-1.elasticbeanstalk.com/)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

------------------------------------
## What is FinoHub?🤔
FinoHub is the loan eligibility or status prediction webapp which is based on data science lifecycle. It helps and gives the idea to the people who wanted to apply for a loan.
FinoHub gives you the result of loan status such as accepted or rejected in one click, just all you need to fill your personal information in the website. FinoHub reduces the human efforts for evaluating the loan applicants for loans and also reduces the time of both loan applicants and those who are evaluating the loan applicants for loans in old-style manner. 

<img src='https://github.com/karan842/finohub/blob/master/media/cover.png' height=300px width=550px></img>

--------------------------------

## How its made?🍨
FinoHub is made by Data Science and business analytical pipeline;

*Phase 1*:
- End goal(business perspective):
1. The main goal is to automate the loan eligibility prediction with the help of predictive machine learning models.
2. To reduce the human efforts and to produce a cost-effective platform for all loan applicants and the finance firm, this actually helps the finance firm and reduces the money that they are heavily spending on the employees who are working in this loan application evaluation department.
3. Collects the data which have *a binary target variable* and understands its feature meaning and importance.
4. Understands the requirement of web app

*Phase 2*:
-  Exploring and cleaning the data:
1. Performing exploratory data analysis and data visualization to gather and gain some useful/important pieces of information from the raw data.
2. Analyzing the data in a univariate and bivariate fashion to see the relationship between different features from the data.
3. Finding some strong relationships and importance between independent and dependent features.
4. Fining correlation between features of the data.
5. Did all these tasks with Python libraries (NumPy, pandas, matplotlib, and seaborn).

*Phase 3*:
- Data cleaning and preparation:
1. Encoding all ordinal, nominal, and, numerical variables into numbers(i.e. 1s or 0s or 2s or 3s)
2. Dealing with null/missing values and imputing them with mean or mode.
3. Analyzing some statistical parts of the data such as Handling outliers and eliminating them.
4. Making data ready for the Machine Learning lifecycle.

*Phase 4*:
- Training data with Machine Learning:
1. Splitting the data into train and test 0.25 splitting rate.
2. Use different ML classification algorithms and avoid overfitting using the Cross-Validation technique.
3. To gain more accuracy using *hyperparameter tuning* i.e. **GridSearchCV**.
4. Training the data with the best parameters and again using Cross-Validation(using a mean of 5 folds).
5. Evaluating the classification algorithms(on training data) with *ROC_CURVE & ROC_AUC_SCORE* and selecting top performers and eliminating bad performers.
6. Again evaluating well-performed classifiers with *ROC_CURVE & ROC_AUC_SCORE* but now with test data.
7. Selecting the winner and runner-up models and evaluating with *Classification report, precision-recall curve & confusion matrix*.
8. Saving both the models and using the winner model(classification algorithm) for further process.

*Phase 5*:
- Creating Streamlit based web app:
1. Writing code for FinoHub web app which is created by Python-Streamlit library with interactive UI
2. Inserting ML model in software development and creating fields as input and summarizing into prediction state.
3. Running the web app and trying with different inputs.
4. Making the FinoHub logo, cover image, and intro video with the help of Canva.

*Phase 6*:
- Deployment for end-users:
1. Containerization of Streamlit web app with the help of Docker. Find FinoHub's official docker image [here](https://hub.docker.com/repository/docker/karan842/finohub)
2. Building a docker image and running it in a container.
3. Pushing docker image into docker registry.
4. Pulling it again and running in the local machine.
5. Deployed the web app on AWS E2 instance with Ubuntu Server.
6. Accessed a web app through the AWS CLI and PuTTY CLI.
7. Running webapp in a EC2 instance.
8. Closing the EC2 instance and creating a webapp in AWS Elastic Beanstalk with Docker environments.
9. Sharing the FinoHub webapp into public.

*Phase 7*:
- Creating an analytical report with Tableau dashboard and key observations.
### [Click here](https://docs.google.com/document/d/1tY9XMglj3yZSzz0tw56NR4U3hlmDbNG40aX4rNDUqZE/edit?usp=sharing) to see the first analytical report of FinoHub.
--------------------------------
# Post Script📜:
- Well as you can see that [FinoHub](http://finohub-env-1.eba-fcih6jie.us-east-1.elasticbeanstalk.com/) is made by dummy dataset because it is just my final project of computer science and for learning the data science lifecycle and machine learning pipeline with AWS. I created this with scratch and I've learned many more things about Data Science. If any you can find any bug or improvement kindly contact me:

## Contact📬:

- My Gmail: karanshingde@gmail.com

- [My Twitter](https://twitter.com/KuchBhiKaran)

- [My LinkedIn](linkedin.com/in/karan-shingde-75a062217)
--------------------------
## Special Thanks(references) 🤝:
- GitHub, StackOverFlow, Towards Data Science, and, Analytics Vidhya
---------------------
# Thank You😉
