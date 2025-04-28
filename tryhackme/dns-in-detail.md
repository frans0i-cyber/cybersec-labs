## Overview

This room on TryHackMe covers the fundamentals of the Domain Name System (DNS).  It explores how DNS works to translate human-readable domain names into IP addresses that computers use to communicate. The room likely provides a mix of theoretical concepts and practical exercises.

## Key Concepts

Based on the image, the room covers these key concepts:

* **What is DNS?** (Understanding the basic function and purpose of DNS)
* **Domain Hierarchy** (Learning about the structure of the DNS namespace, including root domains, top-level domains, and subdomains)
* **Record Types** (Exploring different types of DNS records, such as A, CNAME, MX, and TXT records, and their specific uses)
* **Making a Request** (Understanding the process of a DNS query, from the initial request to the final response)
* **Practical** (Hands-on exercises to apply the concepts learned)

## What I Learned

    * How DNS queries work recursively and iteratively.
    * The role of different DNS servers (recursive resolvers, authoritative name servers).
    * How to use command-line tools (like `nslookup` or `dig`) to query DNS records.
    * Practical skills in configuring or troubleshooting DNS.

## Making a Request

Here's what happens when you make a DNS request:

1.  **Local Cache Check:** Your computer first checks its local cache to see if you've recently looked up the domain name. If found, the process ends here.
2.  **Recursive DNS Server Query:** If the address isn't in the local cache, a request is sent to your Recursive DNS Server (often provided by your ISP, but you can choose your own). This server also has a local cache. If found here, the result is sent back to your computer.
3.  **Root Server Redirection:** If the Recursive DNS Server doesn't have the address, it queries the root DNS servers. These servers direct the query to the appropriate Top Level Domain (TLD) server (e.g., the .com TLD server for tryhackme.com).
4.  **TLD Server Referral:** The TLD server holds records pointing to the authoritative DNS server (or nameserver) for the domain.
5.  **Authoritative DNS Server Response:** The authoritative DNS server stores the actual DNS records for the domain. It sends the relevant record (e.g., the A record for the IP address) back to the Recursive DNS Server. The Recursive DNS Server caches this response for future requests and then relays it to your computer.
    * DNS records have a Time To Live (TTL) value, which determines how long the response is cached. Caching improves efficiency by reducing the need to make a full DNS request every time.

## Commands Used

* No commands used, just checked the different domains

## Room Link

* [TryHackMe Room](https://tryhackme.com/room/dnsindetail)
* [Domain Links](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
