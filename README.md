# 🔁 ResumeSync-AutoDeploy

> **Automatically sync your LinkedIn resume updates across GitHub, Jobberman, and Wellfound.**

🎯 Built by Soetan Adedeji Alabi | Cybersecurity | GRC | Automation Enthusiast  
📍 Nigeria | Powered by Python + Playwright | #FromZeroToCyberHero

---

## 🚀 Why This Project?

In today’s job market, **your resume needs to work even while you're sleeping**.  
This tool automates the process of syncing resume changes from **LinkedIn** to other job platforms like:

- 🐙 **GitHub** (`README.md`)
- 💼 **Jobberman** *(Coming Soon)*
- 🚀 **Wellfound** *(Coming Soon)*

Say goodbye to:
- Outdated resumes on multiple platforms
- Manual copy-paste fatigue
- Missed opportunities because your skills weren’t updated everywhere

---

## 🔧 What It Does

1. Detects changes in your **LinkedIn resume**
2. Compares the latest data with your previous sync
3. Pushes updates to:
   - ✅ **GitHub repo** (as your `README.md`)
   - 🔜 **Jobberman & Wellfound** (via Playwright automation)

---

## 📦 Tech Stack

| Tool        | Purpose                                |
|-------------|----------------------------------------|
| `Python`    | Core scripting                         |
| `Playwright`| LinkedIn, Jobberman & Wellfound scraping |
| `GitHub API`| Push updated content to your repo      |
| `Logging`   | Tracks every sync operation            |
| `JSON`      | Stores last synced resume hash         |

---

## 🛠 Project Structure
ResumeSync-AutoDeploy/
├── main.py
├── resume_state.json
├── requirements.txt
├── logs/
│ └── log_2025_06_17.txt
└── sync_modules/
├── linkedin.py
├── github.py
└── utils.py

---

## 📌 Status

✅ GitHub sync is **LIVE**  
⏳ Jobberman sync is **In Progress**  
⏳ Wellfound sync is **In Progress**

---

## 🧠 Inspiration

I created this to automate part of my job search and build **a real-world Python project** that shows hands-on experience in:

- 🛡️ Automation  
- 🔐 Secure credentials handling  
- 🧠 Change detection logic  
- 🔁 Cross-platform resume deployment

---

## 👨‍💻 About the Author

**Soetan Adedeji Alabi**  
🔍 Cybersecurity Specialist in training  
📚 GRC • Splunk • ISO 27001 • Python • Linux  
🔗 [LinkedIn](https://www.linkedin.com/in/your-username) *(Update this URL)*  
🧠 “Train like you already work in the field.”

---

## 🏷 Topics (To Add to Repo)
resume-sync
linkedin-automation
github-api
playwright-python
career-automation
python
grc

---

## 📬 Want to Collaborate or Recruit?

I’m open to mentorship, freelance roles, GRC opportunities, and automation projects.  
**DM me on LinkedIn or fork this repo and let’s build something amazing.**

---

> “Update once. Deploy everywhere.”  
> — ResumeSync Philosophy
Update README with full documentation and project roadmap
echo .idea/ >> .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
