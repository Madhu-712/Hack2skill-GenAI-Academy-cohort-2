# 💼 Legal-ContractIQ-BQ Agent

[![Powered by Google Cloud](https://img.shields.io/badge/Powered%20By-Google%20Cloud-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![BigQuery](https://img.shields.io/badge/Database-BigQuery-669DF6?logo=google-bigquery&logoColor=white)](https://cloud.google.com/bigquery)

A sophisticated AI-powered legal data intelligence agent that enables natural language interaction with complex legal datasets using **Vertex AI BigQuery Data Agents** and **Streamlit**.

---

## 📖 Project Overview
The **Legal-ContractIQ-BQ Agent** is a generative AI solution designed to bridge the gap between complex legal data and actionable insights. By leveraging Google Cloud's Vertex AI and BigQuery, this application allows legal professionals to query thousands of contracts, clauses, and summaries using simple English. The core of the system is a BigQuery Data Agent that translates natural language into optimized SQL queries, providing instant answers without requiring technical expertise.

## 🏗️ Architecture
The system follows a modern cloud-native data pipeline:
1.  **Data Ingestion:** A Python ETL script (`hf_to_bigquery.py`) fetches the **Strova AI Legal Dataset** from Hugging Face.
2.  **Data Warehouse:** Sanitized data is stored in **Google BigQuery** across multiple tables (`clauses`, `contracts`, `legal_terms`, `summaries`).
3.  **AI Layer:** **Vertex AI BigQuery Data Agents** process natural language inputs and interact with the BigQuery dataset.
4.  **UI/UX:** A **Streamlit** dashboard provides a clean, professional interface for users to chat with the data agent and view dataset metrics.

## ⚠️ Problem Statement
Legal departments often manage vast repositories of contracts and clauses. Traditionally, searching for specific terms (e.g., "force majeure" or "liability limits") across hundreds of documents is either a slow manual process or requires a data analyst to write complex SQL queries. This friction slows down legal audits, compliance checks, and due diligence.

## 📊 Dataset Description
The dataset consists of structured legal contracts, clauses, and summaries sourced from the [Strova AI legal contract dataset](https://huggingface.co/datasets/strova-ai/legal_contract_dataset) on Hugging Face.

## 🔍 Analysis with a Scenario
**Scenario:** A legal team is performing a risk assessment for a new merger and needs to identify all "termination" clauses that don't require notice.
*   **Traditional Method:** Manually open 200+ PDF/CSV files or wait for an IT professional to query the database.
*   **Legal-ContractIQ-BQ Agent:** The user simply types: *"Find all termination clauses in the clauses table that mention 'without notice'."*
*   **Outcome:** The agent immediately returns the specific rows, allowing the legal team to complete a day's worth of work in minutes.

## 🌍 Real-World Adoption (Problem Solving)
-   **Contract Lifecycle Management (CLM):** Automate the extraction of key dates and obligations.
-   **Regulatory Compliance:** Rapidly cross-reference new laws against existing contract libraries.
-   **M&A Due Diligence:** Speed up the review of acquired legal liabilities during corporate mergers.

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
1. Clone the repository:
   ```bash
   git clone https://github.com/Madhu-712/Hack2skill-GenAI-Academy-cohort-2-Legal-ContractIq-BQ-Agent.git
   cd Hack2skill-GenAI-Academy-cohort-2-Legal-ContractIq-BQ-Agent
   ```
2. Place your `service-account-key.json` in the `Legal-ContractIQ-BQ Agent/` directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Data Ingestion
Populate your BigQuery dataset by running the ETL script:
```bash
python "Legal-ContractIQ-BQ Agent/hf_to_bigquery.py"
```

### 4. Running the App
Launch the Streamlit dashboard:
```bash
streamlit run "Legal-ContractIQ-BQ Agent/app.py"
```

## 🐳 Deployment
To run the project in a containerized environment:
```bash
docker build -t legal-agent .
docker run -p 8501:8501 --env-file .env legal-agent
```

## 🔗 Live Demo
[Check out the Live Demo here!](https://github.com/Madhu-712/Hack2skill-GenAI-Academy-cohort-2-Legal-ContractIq-BQ-Agent) *(Replace with actual URL if hosted)*

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
