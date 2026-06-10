# 💼 Multilingual Legal-ContractIQ-BQ Agent

[![Powered by Google Cloud](https://img.shields.io/badge/Powered%20By-Google%20Cloud-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![BigQuery](https://img.shields.io/badge/Database-BigQuery-669DF6?logo=google-bigquery&logoColor=white)](https://cloud.google.com/bigquery)


---
## 📖 Project Overview
The **Legal-ContractIQ-BQ Agent** is a generative AI solution designed to bridge the gap between complex legal data and actionable insights. By leveraging **Vertex AI BigQuery Data Agents** and **Streamlit** this application allows legal professionals to query thousands of contracts, clauses, and summaries using simple English. The core of the system is a BigQuery Data Agent that translates natural language into optimized SQL queries, providing instant answers without requiring technical expertise.(Non lawyers) in multiple languages.



## 🏗️ Architecture

Users interact with ContractIQ through a conversational interface. The Agent layer leverages Gemini for reasoning and Natural Language-to-SQL generation, queries structured legal knowledge stored in BigQuery, and returns contract intelligence, risk analysis, compliance insights, and conversational analytics in natural language.

The system follows a modern cloud-native data pipeline:
1.  **Data Ingestion:** A Python ETL script (`hf_to_bigquery.py`) fetches the **Strova AI Legal Dataset** from Hugging Face and other csv files are imported into the BQ tables.
2.  **Data Warehouse(Data layer):** Sanitized data is stored in **Google BigQuery** across multiple tables (`clauses`, `contracts`, `legal_terms`, `summaries`).
3.  **AI Layer:** **Vertex AI BigQuery Data Agents** process natural language inputs and interact with the BigQuery dataset.
4.  **UI/UX:** A **Streamlit** dashboard provides a clean, professional interface for users to chat with the data agent to get insights on legal contracts and view dataset metrics.


<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/c8fc4c08-d3a1-449b-b548-9f9adc53af0f" />



## 📊 Dataset Overview & Key Insights
The dataset consists of structured legal contracts, clauses, and summaries sourced from the [Strova AI legal contract dataset](https://huggingface.co/datasets/strova-ai/legal_contract_dataset) on Hugging Face.
and also encompasses other datasets consisting  of four interconnected tables that power a GenAI-driven Legal Contract Intelligence and Conversational Analytics Platform using BigQuery and Gemini.

#📄 Contracts Dataset

Stores core contract information such as contract type, involved parties, duration, status, governing law, renewal terms, and notice periods.

Insights

Contains 50 unique contracts across multiple agreement types.
NDAs (38%) and Vendor Agreements (36%) are the most common contract categories.
42% of contracts are active, while 22% have expired.
New York is the most frequently used governing jurisdiction.
Half of the contracts include auto-renewal clauses.

| Column                   | Description                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| **contract_id**          | Unique identifier assigned to each contract.                                              |
| **contract_type**        | Type of agreement (NDA, Vendor Agreement, Service Agreement, Employment Agreement, etc.). |
| **party_a**              | First organization or entity involved in the contract.                                    |
| **party_b**              | Second organization or entity involved in the contract.                                   |
| **effective_date**       | Date on which the contract becomes legally effective.                                     |
| **expiration_date**      | Date when the contract expires or ends.                                                   |
| **contract_period_days** | Total duration of the contract in days.                                                   |
| **status**               | Current contract state (Active, Expired, Pending, etc.).                                  |
| **governing_law**        | Legal jurisdiction whose laws govern the agreement.                                       |
| **renewal_type**         | Renewal mechanism (Auto-Renew or Manual Renewal).                                         |
| **notice_period_days**   | Number of days' notice required before termination or renewal changes.                    |


#⚖️ Clauses Dataset

Contains individual legal clauses extracted from contracts along with clause type and risk level.

Insights

Includes 600 legal clauses across all contracts.
Termination clauses are the most frequently occurring clause type.
High-risk clauses account for 34% of all clauses analyzed.
Common clause categories include Confidentiality, Termination, Indemnification, Payment Terms, and Governing Law.

| Column          | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| **contract_id** | Links the clause to a specific contract.                                       |
| **clause_id**   | Unique identifier for each clause.                                             |
| **clause_type** | Category of clause (Confidentiality, Termination, Indemnification, SLA, etc.). |
| **clause_text** | Full textual content of the clause.                                            |
| **risk_level**  | AI-assigned or predefined legal risk rating (High, Medium, Low).               |


#📋 Summaries Dataset

Provides AI-generated contract intelligence including executive summaries, obligations, and risks.

Insights

Covers 100 contract summaries.
Enables rapid contract understanding without reviewing full documents.
Highlights key obligations, deadlines, and legal risks.
| Column                | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| **contract_id**       | Contract identifier linked to the master contract table.                 |
| **executive_summary** | Short business-friendly summary of the contract.                         |
| **key_obligations**   | Important responsibilities or commitments of the parties.                |
| **key_risks**         | Major legal, financial, or operational risks identified in the contract. |



#📚 Legal Terms Dataset

Acts as a legal knowledge base containing legal terms, definitions, and business-friendly explanations.

Insights

Contains legal terminology and definitions.
Simplifies complex legal concepts for business users.
Enhances AI-powered legal assistance and knowledge retrieval.

| Column                   | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| **term**                 | Legal concept or terminology.                                      |
| **definition**           | Formal legal definition of the term.                               |
| **business_explanation** | Simplified explanation describing the business impact of the term. |



## ⚠️ Problem Statement
Legal departments often manage vast repositories of contracts and clauses. Traditionally, searching for specific terms (e.g., "force majeure" or "liability limits") across hundreds and thousands of documents is either a tedious , slow manual process or requires a data analyst to write complex SQL queries. This friction slows down legal audits, compliance checks, and due diligence.


## 🔍 Analysis with a Scenario
**Scenario:** A legal team is performing a risk assessment for a new merger and needs to identify all "termination" clauses that don't require notice.
*   **Traditional Method:** Manually open 200+ PDF/CSV files or wait for an IT professional to query the database.
*   **Legal-ContractIQ-BQ Agent:** The user simply types: *"Find all termination clauses in the clauses table that mention 'without notice'."*
*   **Outcome:** The agent immediately returns the specific rows, allowing the legal team to complete a day's worth of work in minutes.

## 🌍 Real-World Adoption (Problem Solving)
-   **Contract Lifecycle Management (CLM):** Automate the extraction of key dates and obligations.
-   **Regulatory Compliance:** Rapidly cross-reference new laws against existing contract libraries.
-   **M&A Due Diligence:** Speed up the review of acquired legal liabilities during corporate mergers.
-   **Multilingual Support:** Get queries answered in multiple language of your choice.(Hindi, English, Kannada,Tamil, Malyalam & Telgu)

## 📂 Project Structure
```text
Legal-ContractIQ-BQ Agent/
├── app.py                      # Main Streamlit application
├── hf_to_bigquery.py           # ETL pipeline script
├── Dockerfile                  # Containerization config
├── requirements.txt            # Python dependencies
├── .streamlit/                 # Streamlit configuration
│   └── config.toml
├── .env                        # Environment variables (GCP Project ID, etc.)
├── service-account-key.json    # Google Cloud service account credentials
└── *.csv                       # Local dataset caches
```

## 🚀 Steps of Execution

### 1. Prerequisites
- Google Cloud Project with BigQuery and Vertex AI APIs enabled.
- Python 3.9+ installed.
- A service account key with BigQuery Data Editor and Vertex AI User roles.

### 2. Setup
1. Project setup :
   gcloud auth list
   gcloud config list project
   gcloud auth login OR
   gcloud auth application-default login
   export PROJECT_ID=<YOUR_PROJECT_ID>
   gcloud config set project <YOUR_PROJECT_ID>

2.  Clone the repository:
   ```bash
   git clone https://github.com/Madhu-712/Hack2skill-GenAI-Academy-cohort-2-Legal-ContractIq-BQ-Agent.git
   cd Hack2skill-GenAI-Academy-cohort-2-Legal-ContractIq-BQ-Agent
   ```
3. cd Legal-ContractIQ-BQ Agent
   Place your `service-account-key.json` in the `Legal-ContractIQ-BQ Agent/` directory.

### 3. Data Ingestion
Populate your BigQuery dataset by running the ETL script:
```bash
python "Legal-ContractIQ-BQ Agent/hf_to_bigquery.py"
```
Other tables are added directly inside BQ datasets (Clauses, Contracts, Summmaries, legal terms).

 Install dependencies:
   ```bash
   pip install -r requirements.txt
   
   ```
### 4. Running the App
 Make sure an <Agent ID >placeholder is replaced with an unique, system-generated alphanumeric string (usually a UUID, like f9f8f8c0-f8f8-4f8f-8f8f-8f8f8f8f8f88) that Google Cloud uses behind the scenes to pinpoint your specific AI agent in app.py file.
From your URLs, we can see you are using the new BigQuery Data Agents infrastructure. Your key credentials are right there in the path https://lookerstudio.google.com/conversation?agent=projects/notebooklm-491108/locations/us/dataAgents/agent_c03cf192-61ec-4859-a042-4bd22d531bc5

Project ID: notebooklm-491108
Location: us (This is important! It's multi-region us, not us-central1)
Agent ID: agent_c03cf192-61ec-4859-a042-4bd22d531bc5

Start the streamlit server by running
   ```bash
   python3 -m streamlit run app.py --server.port 8080 --server.enableCORS false --server.enableXsrfProtection false
  
   OR if streamlit/config.toml is not set
   
   streamlit run app.py --server.port 8080

```

## 🐳 Deployment
To run the project in a containerized environment:

1.-Create a Dockerfile

2.Enable required API's
-gcloud services enable artifactregistry.googleapis.com run.googleapis.com cloudbuild.googleapis.com

3.Create a docker repo in artifact registry
-gcloud artifacts repositories create legal-repo \
    --repository-format=docker \
    --location=us \
    --description="Docker repository for legal agent app"

4.Build the container image using Cloud build
-gcloud builds submit --tag us-docker.pkg.dev/notebooklm-491108/legal-repo/legal-agent-app:v1 

5.Deploy using docker command
gcloud run deploy legal-agent-service \
    --image=us-docker.pkg.dev/notebooklm-491108/legal-repo/legal-agent-app:v1 \
    --region=us-central1 \
    --allow-unauthenticated

    
## 🔗 Live Demo link

Streamlit App hosted on CloudRun service url
https://legal-agent-service-881601845310.us-central1.run.app

Medium post link:
https://medium.com/@madhu.712/contractiq-transforming-legal-contracts-into-conversational-intelligence-with-bigquery-and-gemini-69bf909e3606

YouTube link:
https://youtu.be/YMFUGzbjPfQ?si=rNiBQZfD4AZ0Ap2I

## Example Queries
Contract Summary:

Summarize CTR-0004
Summarize the risks across all NDAs.

Contract Comparison:

Compare termination clauses across vendor agreements

Risk Analysis:

Identify contracts containing high-risk clauses
Show all contracts with high-risk termination clauses.
What are the key obligations in active vendor agreements?

Legal Explanation:

What does indemnification mean?

Multilingual Query:

NDA-001 का सारांश बताइए
EMP-101 ಒಪ್ಪಂದದ ಪ್ರಮುಖ ಅಪಾಯಗಳು ಯಾವುವು?


## 🤝 Contributions
Contributions are welcome! If you have suggestions for new features or data visualizations, please:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Disclaimer:** This tool is intended for informational purposes and should not replace professional legal advice.
