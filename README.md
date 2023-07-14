# Estimating Home Values

by Martin Reyes

<!-- <p>
  <a href="https://github.com/martin-reyes" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3291/3291695.png" alt="GitHub" width="40" height="40">
  </a>

  <a href="https://www.linkedin.com/in/martin-reyes-ds/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" alt="LinkedIn" width="40" height="40">
    </a>
</p>
 -->

## Project Description

In this project, I want to find key drivers of property value for single family properties. I want to make recommendations on which features predict home values well and those that don't. I want to present visualizations, analyses, and tests to support these claims. 

 
## Project Goals
 
- Perform EDA on Zillow dataset to see which features predict house prices well.
- Construct a ML Regression model that predicts property values.

 
## Initial Thoughts

I think sqft and bedrooms will be the biggest predictors of home value. I also think location will be a big predictor, but this will require feature engineering.

 
## The Plan
 
* **Acquire** zillow data from MySQL
 
* **Prepare** data. 
    1. Inspect raw data and note any desired transformations which may include any of the following:
        * Drop unnecessary columns (duplicate, redundant columns)
        * Handle missing values and impute appropriate values
            * check for explicit missing values (e.g. `np.nan`)
            * check for implicit missing values (e.g. whitespace, `'unknown'`, etc.)
        * Deal with any duplicate rows/homes (with same info, id's, or location).
        * Numeric columns should be numeric data types
        * Numeric data should be scaled appropriately
            * Min-max scale
        * Address and encode categorical columns
            * one-hot encode unordered categorical columns
    1. Inspect clean data
        * Ensure data is tidy:
            * one value per cell
            * each observation is one and only one row
            * each feature is one and only one column
    1. Split the data
        * Determine if homes have county imbalance. If, so stratify.
        * Perform 70/15/15 train/validate/test split.
        * **set RANDOM_STATE =123**
    1. Create data dictionary
    1. Summarize data transformations

* **Explore** data in search of value drivers
   1. General Inspect
       - `.info()` and `.describe()`
       - identify continuous and categorical columns
   1. Univariate Stats: 
       - Categorical
       - Nunerical
   1. Bivariate Stats:
       - Categorical features to property value (target) relationships
       - Continuous features to property value (target) relationship
       
   Ask Specific questions:
   - How does sqft relate to property value?
   - How do home values vary among counties?
   - How do home values vary among homes with X bedrooms and X bathrooms
      
* Develop a **model** to predict property value
   * Use drivers identified in explore to build predictive regression models
   * Create and run a baseline model with `sklearn`'s `DummyRegressor` to compare our results to
   * Create and run `Linear Regression`, `LassoLars`, and Polynomial regression models
   * Use the insights from the highest-performing model (with highest test `RMSE`) to confirm our initial hypotheses and insights on the features that are the biggest drivers of property value
   
* **Evaluate** models on train and validate data
   * Identify the metric to maximize
       * RMSE and R squared
   * Select the best model based on highest desired metric (RMSE)

* Evaluate the best model on validation data set. After we find the best model, test on the test set.
    * Interpret metrics to analyze test performance and insights
 
* Draw conclusions
 
 
<a name="data-dictionary"></a>
## Data Dictionary

| Feature             | Definition                                          |
|:---------------------|:----------------------------------------------------|
| parcelid             | Unique identifier for the parcel                     |
| id                   | Unique identifier for the property                   |
| bathrooms            | Number of bathrooms in the property                  |
| bedrooms             | Number of bedrooms in the property                   |
| sqft                 | Square footage of the property                       |
| latitude             | Latitude coordinates of the property location        |
| longitude            | Longitude coordinates of the property location       |
| regionidcity         | Identifier for the city where the property is located|
| regionidzip          | Identifier for the zip code where the property is located|
| property_value       | Value of the property                                |
| transaction_date     | Date of the property transaction                      |
| age                  | Age of the property in years                          |
| county               | County where the property is located                  |


 
## Steps to Reproduce
- pull final notebook and python files
- ensure you have access to the data
- run notebook
 
## Takeaways and Conclusions

Key drivers of property value:
- sqft
- bathrooms
- bedrooms

Best performing ML model:
- Linear Regression model with a .26 R^2 and 250,000 RMSE.
 

## Summary
* summarize findings/drivers and answers
* state model performance compared to baseline

## Recommendations
* Recommend stakeholder actions
* Recommend models to use

### Next Steps
With more time, I can:
- Engineer features the categorize home location
    - using zipcodes or latitude and longitude
- Train a ML model on these features if they are strong drivers
- Run non-linear regression models
- Use non-linear feature scaling techniques to fit linear models better

[Back to top](#top)