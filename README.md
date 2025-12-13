# 🚀 SpaceX Falcon 9 First Stage Landing Prediction

## 📄 Project Overview
The commercial space industry is racing to make space travel more affordable. SpaceX has revolutionized this by developing the **Falcon 9**, a rocket capable of landing its first stage for reuse. This reusability reduces the cost of launch from \$165 million to \$62 million per launch.

**Goal:** This project builds a machine learning pipeline to predict whether the Falcon 9 first stage will land successfully. These predictions can be used to estimate launch costs and assess mission risk.

## 🛠️ Methodology
The project follows a standard Data Science methodology:
1.  **Data Collection:** * **SpaceX REST API:** Retrieved launch data (Flight Number, Date, Booster Version, etc.).
    * **Web Scraping:** Scraped Falcon 9 historical data from Wikipedia using `BeautifulSoup`.
2.  **Data Wrangling:** * Handled missing values (imputation).
    * Filtered for Falcon 9 launches only.
    * One-Hot Encoded categorical variables (Orbits, Launch Sites).
3.  **Exploratory Data Analysis (EDA):**
    * **SQL:** Queried the dataset to find patterns in payload mass and mission outcomes.
    * **Visualization:** Used `Matplotlib` and `Seaborn` to visualize success rates by orbit, year, and payload.
4.  **Interactive Visual Analytics:**
    * **Folium Maps:** Built interactive maps to visualize launch sites and success clusters.
    * **Plotly Dash:** Created a dashboard to filter data by Launch Site and Payload Mass.
5.  **Predictive Analysis (Machine Learning):**
    * Built and tuned classification models: Logistic Regression, SVM, Decision Tree, and K-Nearest Neighbors (KNN).

## 📊 Key Findings
* **Launch Site Performance:** **KSC LC-39A** has the highest success rate (**76.9%**), confirming that newer, more mature launch sites yield better results.
* **Payload Sweet Spot:** Missions with payloads between **2,000 kg and 6,000 kg** have the highest landing success rate.
* **Technological Evolution:** Success is strongly correlated with the **Booster Version**. Older versions had higher failure rates, while modern versions (**FT, B4, B5**) are highly reliable.
* **Geographical Constraints:** All launch sites are located near the coast for safety (ocean trajectory) and optimized by latitude for specific orbital insertions.

## 🤖 Model Performance
We compared four machine learning models using `GridSearchCV` for hyperparameter tuning. The results were evaluated based on **Test Accuracy** and **Cross-Validation (CV) Score**.

| Model | Test Accuracy | Best CV Score |
| :--- | :--- | :--- |
| **Decision Tree** | 83.3% | **87.7%** |
| **K-Nearest Neighbors** | 83.3% | 84.8% |
| **Support Vector Machine** | 83.3% | 84.8% |
| **Logistic Regression** | 83.3% | 84.6% |

**Conclusion:** The **Decision Tree Classifier** was identified as the best model, achieving the highest Cross-Validation accuracy (88.9%) while maintaining robust performance on the test set.

## 💻 Tech Stack
* **Languages:** Python, SQL
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Folium, Plotly Dash, BeautifulSoup, Requests.

## 📂 File Structure
* `spacex_dash_app.py`: The code for the interactive Plotly dashboard.
* `notebooks/`: Jupyter notebooks covering Data Collection, Wrangling, EDA, and Modeling.
* `images/`: Screenshots of visualizations (Pie Charts, Confusion Matrices).

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/vatsun07-web/Data-Science-Capstone-Project.git]
    ```
2.  Install dependencies:
    ```bash
    pip install pandas dash plotly scikit-learn folium matplotlib seaborn
    ```
3.  Run the Dashboard:
    ```bash
    python spacex_dash_app.py
    ```

---
*Author: [Seiha Vat]* *Data Source: SpaceX Public API & Wikipedia*
