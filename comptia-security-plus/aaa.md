# 📘 Lesson 4: Authentication, Authorization, and Accounting (AAA) — CompTIA Security+ (Professor Messer)

This lesson covers the **AAA framework**—a core component of network and security architecture that ensures users are properly **authenticated**, **authorized**, and **accounted for**. Essential knowledge for the CompTIA Security+ (SY0-701) exam and real-world cybersecurity.

---

## 🔐 What Is AAA?

- **Authentication**: Verifying a user’s identity (e.g., username + password, MFA).\
- **Authorization**: Granting permissions and access levels once identity is confirmed.\
- **Accounting**: Tracking user activity—login/logout times, resource usage—for auditing and analysis. :contentReference[oaicite:1]{index=1}

The process typically starts with **identification** (username), followed by authentication, then authorization, and finally accounting.

---

## 🛡️ AAA in Action

- **AAA Servers** manage this flow via protocols like RADIUS, TACACS+, and Diameter. :contentReference[oaicite:2]{index=2}  
- In a login scenario:
  1. User enters credentials → authentication  
  2. System checks their roles → authorization  
  3. All actions get logged → accounting

---

## 🧭 AAA Protocols Overview

| Protocol     | Authentication | Authorization | Accounting | Remarks |
|--------------|----------------|----------------|-------------|---------|
| **RADIUS**   | ✔              | ✔              | ✔           | Uses UDP; common for VPNs, Wi‑Fi. :contentReference[oaicite:3]{index=3} |
| **TACACS+**  | ✔              | ✔              | ✔           | Uses TCP; fully encrypts sessions; Cisco‑centric. :contentReference[oaicite:4]{index=4} |
| **Diameter** | ✔              | ✔              | ✔           | Modern replacement for RADIUS in telecom networks. :contentReference[oaicite:5]{index=5} |

---

## 📌 Why It Matters

- **Centralized control**: One point for managing access across device types. :contentReference[oaicite:6]{index=6}  
- **Security & compliance**: Logs support audits, legal requirements, and security forensic efforts.  
- **Scalability**: Easily manage permissions and access as your environment grows.

---

## ✅ Key Takeaways

- **Authentication** = who you are  
- **Authorization** = what you can do  
- **Accounting** = what you've done

- AAA is critical for **network access**, **VPNs**, **secure Wi‑Fi**, **remote management**, and regulatory compliance.  
- **Understand differences** between main protocols (RADIUS vs TACACS+ vs Diameter), including transport and encryption mechanics.

---

🎓 *This summary is based on Professor Messer’s CompTIA Security+ (SY0-701) training.*  
📺 [Watch Lesson 4: Authentication, Authorization, and Accounting](https://www.youtube.com/watch?v=AhaZtj5P2a8&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=6)
