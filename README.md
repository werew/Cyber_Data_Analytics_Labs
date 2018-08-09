# Cyber Data Analytics Labs 
(from https://www.4tu.nl/cybsec/en/course-program/cda/)

## Fraud detection

One of the big tasks in cyber data analytics is detecting malicious or fraudulent data records. 
This is a machine learning task that is extra complicated due to several properties of the data and its domain:

 * The large majority (typically over 99%) of the data is benign
 * Malicious users actively try to hide
 * The amount of data to learn from is enormous
 * Often this data is unlabeled

This lab focuses on the first property: how to deal with large class imbalances in machine learning.

The full description of the lab is available [here](fraud_detection/docs/lab1_cda_2018.docx ).

## Anomaly detection

Most data in cyber data analytics is sequential in nature. 
Applying machine learning to sequential data is difficult because past data (rows) provide information for future data (rows). 
The data points are thus not i.i.d (independently and identically distributed). Learning from sequential data and time series is a
large domain covering many problems, solutions, and algorithms.

In this lab  focuses on the problem of anomaly detection in 
SCADA systems. Anomaly detecting is typically harder than classification because the data are unlabeled. We
have to rely on statistics such as occurrence counts or value ranges to find anomalies, rendering many machine learning 
methods inapplicable. Securing SCADA system is considered one of the most important problems in cyber security.

The full description of the lab is available [here](anomaly_detection/docs/cda_lab_2.docx).
