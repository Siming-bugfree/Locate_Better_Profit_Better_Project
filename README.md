# Locate_Better_Profit_Better_Project
Use data from Yelp, TripAdvisor, New York Government to help restaurants better locate their new store
README

1. scrape_Tripadvisor.py: We scrape Tripadvisor using BeautifulSoup in order to get detailed information of restaurants in Toronto

2. scrape_Tripadvisor_detail_page: code for scraping Tripadvisor detailed page.

3. Yelp_data_ preprocessing.ipynb: We preprocess Yelp data to select related features.

4. exploratory_data_heatmap.ipynb: We use heatmap to explore the distribution of business and reviews in Toronto.  

5. merge_Yelp_Tripadvisor.py: We merge Yelp data and Tripadvisor data on business names.

6. user_neighborhood.ipynb: Assign each user to a neighborhood and attach a label.

7. select_review.py: We select 200,000 out of 230,000 review data with value 1 on the restaurant tag.

8. review_neighborhood.py: We determine the start neighborhood and the destination neighborhood for each review data.

9. transition_frequency.py: We directly use the number of reviews to get a transition matrix.

10. transition_extend.py: We use the collaborative filtering algorithm to modify and get another transition matrix.

11. transition_matrix.ipynb: We calculate the transition matrix T and the potential customer matrix C (C = D * T).

12. concat.py: We concat potential customer matrix C with business matrix B and get a final profile of businesses with business-related features and potential customer features X (X = B left join C)

13. feature_extension.py: We process demographics features and add interaction items to capture non-linearity.

14. lasso.r: model feature selection and engineering.

15. 10_folds_cv_for_predictive_models.py: We use 10 folds cross validation for all predictive models.
