# Predictive Analysis

## Objective

This analysis utilizes logistic regression to predict the binary classification probabilities of carts for determining cart abandonment based on the features.

### Data

Synthetic data containing 10,000 rows was generated for the analysis. Data was split to allocate 80% for training and 20% for testing.

#### Features

The features include:

* `advertisement`, which specifies the total amount spent on advertisement for the item
* `item_id`, which specifies the ID of the item
* `total_days_before_cart_creation`, which specifies the total number of days an item has been listed when the cart was created
* `year_date_created`, which specifies the year the cart was created
* `month_date_created`, which specifies the month the cart was created
* `day_date_created`, which specifies the day the cart was created
* `year_cart_transition`, which specifies the year the cart transitioned away from being a cart
* `month_cart_transition`, which specifies the month the cart transitioned away from being a cart
* `day_cart_transition`, which specifies the day the cart transitioned away from being a cart
* `year_item_listed`, which specifies the year the item was listed
* `month_item_listed`, which specifies the month the item was listed
* `day_item_listed`, which specifies the day the item was listed

#### Target

The target details include:

* `became_order`, which specifies the cart order as an integer. 1 indicates the cart successfully transitioned into an order, and 0 indicates the cart was not ordered.

## Results

### Receiver Operating Characteristic

The area under the curve achieved a score of 97%.

### Classification Report Metrics

#### Accuracy

The logistic regression model achieved an accuracy score of 89%.

#### Precision

The precision score achieved:

* 91% classifying 1
* 86% classifying 0
* 88% for the macro-average
* 89% for the weighted average

#### Recall

The recall score achieved:

* 88% classifying 1
* 89% classifying 0
* 89% for the macro-average
* 89% for the weighted average

#### F1-score

The F1-score achieved:

* 90% classifying 1
* 87% classifying 0
* 88% for the macro-average
* 89% for the weighted average

#### Visualizations

Classification Counts:

The graph titled Classification Counts illustrates the number of carts counted for each binary classification.

![Figure 1: Classification Counts](<Figure 1 Classification Counts.png>)

\
Logistic Regression Curve:

The graph titled Logistic Regression Curve illustrates the probabilities for classifying carts as advertisements increase. This graph reveals that more carts are becoming orders when more advertisement is spent.

![Figure 2: Logistic Regression Curve](<Figure 2 Logistic Regression Curve.png>)

\
Receiver Operating Characteristic Curve:

The graph titled Receiver Operating Characteristic Curve illustrates the plot between the True Positive Rate and the False Positive Rate. An area under the curve score of 97% demonstrates the model is effectively identifying both positive and negative classifications.

![Figure 3: Receiver Operating Characteristic Curve](<Figure 3 Receiver Operating Characteristic Curve.png>)

### Confusion Matrix

The confusion matrix heatmap details include:

* True Positive: 980
* True Negative: 791
* False Positive: 95
* False Negative: 134

![Figure 4: Confusion Matrix](<Figure 4 Confusion Matrix.png>)

## Limitations

The advertisement feature within the synthetic dataset contains more weight. Adjusting the weight would require further evaluation of the metrics.