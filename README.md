# 🚀 End-to-End Azure DevOps Capstone Project

## 📌 Project Overview
This Capstone Project unifies all modern DevOps practices into a single, fully automated cloud pipeline. Pushing updates to the GitHub repository automatically provisions cloud infrastructure, configures server runtimes, and deploys a multi-container application on Microsoft Azure.

---

## 🏗️ Architecture & Workflow
[ Developer Push ]
│
▼
[ GitHub Actions Pipeline ]
├── 1. Code Quality & Unit Tests (Flake8 & PyTest)
├── 2. Provision Infrastructure (Terraform ➔ Azure VM & Networking)
├── 3. Configure Server Environment (Ansible ➔ Install Docker Engine)
└── 4. Deploy Application Stack (Docker Compose ➔ Flask + Redis)

---

## 🛠️ Toolchain & Technologies

| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Cloud Provider** | Microsoft Azure | Hosts Resource Group, VNet, Subnet, NSG, Public IP, and Virtual Machine |
| **Infrastructure as Code** | Terraform | Declaratively provisions all Azure infrastructure resources |
| **Configuration Mgmt** | Ansible | Installs Docker Engine, configures dependencies, and sets user permissions |
| **Container Runtime** | Docker Compose | Orchestrates two-tier app stack (Flask Web App + Redis Database) |
| **CI/CD Automation** | GitHub Actions | Executes automated test, build, provision, and deploy pipeline |

---

## 📋 Implementation Phases

- [ ] **Phase 1: Project Structuring & App Preparation** — Set up Flask web app, unit test suite, and local Docker Compose stack.
- [ ] **Phase 2: Modular Infrastructure as Code (Terraform)** — Build Azure Terraform scripts to spin up compute and networking resources.
- [ ] **Phase 3: Automated Host Configuration (Ansible)** — Write playbooks to configure Docker on target Azure VMs via SSH.
- [ ] **Phase 4: GitHub Actions Integration** — Store Azure secrets in GitHub and build the end-to-end multi-stage pipeline.
- [ ] **Phase 5: Teardown Automation** — Ensure single-command infrastructure destruction to manage cloud costs.
