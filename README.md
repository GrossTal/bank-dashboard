# Bank Dashboard
🏦 Bank Transactions Dashboard with Metabase.

This is a small data analysis project showcasing a dynamic Bank Transactions Dashboard built using **Python**, **PostgreSQL** and **Metabase**.

<img src="https://github.com/user-attachments/assets/9e3c1041-299f-4455-a2fb-92b256db1ddd" width="400"/>

The project simulates real-world BI/analytics work for a banking context — generating mock data, storing it in a relational database, and using Metabase to create interactive insights.

✅ Tools Used:
* Python – for generating mock data
* AWS RDS PostgreSQL – hosted relational database
* Metabase – to visualize and build dashboards from SQL queries

### 📊 Project Workflow
Data Generation:

Created a Python script to generate mock data for:

**customers** (with age, region, risk level),
**accounts** (per customer),
**transactions** (1,000 total)

#### Deployed a PostgreSQL instance on AWS RDS, uploaded the data, and connected Metabase to it - enabling the creation of SQL-based insights and visual dashboards.
🐳 Metabase was run locally using Docker with the command:

```docker run -d -p 3000:3000 --name metabase metabase/metabase```

Opened Metabase on http://localhost:3000 after running the container.

### Dashboard Insights Examples:

#### 🧑‍🤝‍🧑 Age group behavior (avg spend, transaction count, customer count)

<img src="https://github.com/user-attachments/assets/040f5920-9d2a-4cd7-bf46-6ca8955c2355" width="800"/>

#### 🧑‍🤝‍🧑 Total spend by age group
<img src="https://github.com/user-attachments/assets/ae762cd7-33bd-4a43-8064-16094d97d9c0" width="800"/>


#### 📍 Regional trends (count, average)
<img src="https://github.com/user-attachments/assets/0fc653b8-9b25-4c17-acec-fe13105aea74" width="800"/>

<img src="https://github.com/user-attachments/assets/3b71795c-573f-4ded-b29d-2b3f46f84f47" width="800"/>

🏦 Channel preferences per age group (ATM, Online, Mobile, Branch)

<img src="https://github.com/user-attachments/assets/b9fda4c4-2083-48f3-8a67-1198e6297b64" width="800"/>

