
# 📘Non-Repudiation — CompTIA Security+ (Professor Messer)

This lesson explains **Non-Repudiation**, a key concept in cybersecurity that ensures a person **cannot deny** their actions—particularly when it comes to sending or receiving data. Non-repudiation is critical in legal, forensic, and secure communications scenarios, and is a core topic in the CompTIA Security+ (SY0-701) exam.

---

## 🔐 What Is Non-Repudiation?

Non-repudiation guarantees that the **origin and integrity** of a message or action can be verified. It prevents individuals from denying their involvement in digital communication, especially where accountability is necessary.

This is achieved through two major components:

- **Proof of Integrity** — via hashing.
- **Proof of Origin** — via digital signatures.

---

## 🛠️ Tools That Support Non-Repudiation

| Mechanism             | Purpose                                      | How It Works                                                  |
|-----------------------|----------------------------------------------|---------------------------------------------------------------|
| **Hashing**           | Verifies **data integrity**                  | Generates a unique fingerprint of data; changes break the hash |
| **Digital Signatures**| Verifies **data origin + integrity**         | Uses asymmetric encryption to bind sender identity to data     |

---

## 🔁 How Digital Signatures Work

1. Sender creates a **hash** of the message.
2. Hash is **encrypted with the sender’s private key**.
3. Encrypted hash (the digital signature) is sent along with the message.
4. Receiver decrypts the signature using the **sender’s public key**.
5. Receiver hashes the message on their end.
6. If both hashes match → integrity & authenticity are verified.

---

## 🚨 Why Hashing Alone Isn't Enough

- A hash can confirm that data hasn’t changed.
- But it **can’t prove who sent it** — anyone could generate a hash.
- That’s why digital signatures are essential for full non-repudiation.

---

## 📌 Key Takeaways

- Non-repudiation ensures **accountability** and prevents denial of actions.
- Combines **integrity (hashing)** and **authentication (digital signatures)**.
- Common in secure emails, software distribution, and legal transactions.
- Understanding the **role of private/public key pairs** is crucial for exam success and real-world application.

---

🎓 *This summary is based on Professor Messer’s CompTIA Security+ (SY0-701) training series.*  
📺 [Watch Lesson 4: Non-Repudiation](https://www.youtube.com/watch?v=XxnCxPEllMg)
