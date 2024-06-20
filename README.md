# Comparative Analysis of Statistical and Machine Learning Models for Enhanced Cryptocurrency Price Prediction with Technical Indicator Integration

## Introduction
This repository contains the code and resources for a class project on forecasting cryptocurrency prices using statistical models and machine learning algorithms. The project explores the performance of Linear Regression, ARIMA, Recurrent Neural Networks (RNN), Gated Recurrent Units (GRU), Long Short-Term Memory (LSTM) networks, VARMAR, Kalman Filter,Meta Learning, NBeats, NHiTS in forecasting the stock prices of Bank.

## Dataset
The dataset used in this project is collected from finance.yahoo.com, containing daily data for Bitcoin, Ethereum, and Dogecoin from 2019-03-01 to 2024-06-01. The dataset includes features such as open price, high price, low price, close price, adjusted close price, and trading volume.

## Feature Engineering
To improve the predictive performance of the models, the project incorporates technical indicators as features. These indicators, such as moving averages and momentum indicators, provide insights into market sentiment and trends, aiding in the prediction of price movements.

## Models
The following models are implemented and evaluated in this project:

- Linear Regression
- ARIMA
- VARMA
- Recurrent Neural Networks (RNN)
- Gated Recurrent Units (GRU)
- Long Short-Term Memory (LSTM)
- Meta Learning
- Kalman Filter
- NBeats
-NHiTS

## Evaluation
The models are evaluated using various performance metrics, such as Root Mean Squared Error (RMSE), Mean Absolute Percent Error (MAPE), and Symmetric Mean Absolute Error (MAE). Three different train-test split ratios are used for each model: 70:30, 80:20, and 90:10. The results are compared to assess the strengths and weaknesses of each model in accurately predicting cryptocurrency prices.

## Division of Work
| Member | Responsibilities |
| --- | --- |
| Tran Hoang Phuc | Implemented RNN, NBeats models.|
| Nguyen Viet Hoang | Implemented LSTM, Meta Learning models.|
| Le Ba Nhat Long | Implemented GRU, Kalman Filter models.|
| Nguyen Hung Tuan | Implemented Linear Regression, NHiTS models.|
| Le Anh Duy | Implemented ARIMA, VARMA models.|


## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments
We would like to thank our instructor and the University of Information Technology for providing the resources and support for this class project.