# OSI Model – TryHackMe

## ✅ Overview

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into **seven distinct layers**. It helps us understand how different networking protocols and devices interact and communicate with one another.

---

## 🧠 Key Concepts

### 1. Physical Layer (Layer 1)
- Transmits raw bitstream over a physical medium (e.g., cables, fiber)
- Deals with voltages, cables, pins

### 2. Data Link Layer (Layer 2)
- Responsible for node-to-node data transfer
- Error detection and correction
- Protocols: Ethernet, PPP

### 3. Network Layer (Layer 3)
- Routing of packets across networks
- Logical addressing (IP addresses)
- Protocols: IP, ICMP, IPsec

### 4. Transport Layer (Layer 4)
- Reliable data transfer between hosts
- Segmentation, flow control, error control
- Protocols: TCP (reliable), UDP (fast, unreliable)

### 5. Session Layer (Layer 5)
- Establishes, manages, and terminates sessions
- Ensures ongoing communication

### 6. Presentation Layer (Layer 6)
- Data translation, encryption, compression
- Transforms data into readable formats

### 7. Application Layer (Layer 7)
- Closest to the user
- Provides network services to applications
- Protocols: HTTP, FTP, SMTP, DNS, etc.

---

## 🧩 Bonus: OSI Mnemonics

- **All People Seem To Need Data Processing** (Layer 7 → 1)
- **Please Do Not Throw Sausage Pizza Away** (Layer 1 → 7)

---

## 🕹️ Commands Used in Practical Task

In the TryHackMe practical challenge, you might interact with:

```bash
ping <ip-address>               # Check host availability (Layer 3 - Network)
tracert (Windows) / traceroute <ip> # Trace route to a host (Layer 3)
ipconfig / ifconfig             # View network config (Layer 3)
netstat                         # Check connections & ports (Layer 4)
telnet <ip> <port>             # Connect to services (Layer 7)
curl http://<ip>:<port>        # Fetch web resources (Layer 7)

