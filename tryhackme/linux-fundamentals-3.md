## Overview

This room concludes the "Linux Fundamentals" module, showcasing useful utilities and applications that enhance day-to-day Linux usage. You've advanced your Linux skills by learning about automation, package management, and service/application logging.

## Key Concepts

* **Deploy Your Linux Machine:** Similar to Part 2, this involves deploying the target Linux machine within the TryHackMe environment.
* **Terminal Text Editors:** Exploring command-line based text editors like `nano` and `vim` for creating and modifying files directly in the terminal.

    * **Vim Cheat Sheet:** For a quick reference of Vim commands, you can check out this helpful cheat sheet: \[[https://vim.rtorr.com/](https://vim.rtorr.com/)\]
    * **TryHackMe Toolbox: Vim:** This room provides a comprehensive guide to learning Vim, from basic text editing to more advanced features. \[[TryHackMe Toolbox: Vim](https://tryhackme.com/room/toolboxvim)\]
* **General/Useful Utilities:** Discovering handy command-line utilities for various tasks, such as file manipulation (`tar`, `gzip`), process monitoring (`top`, `htop`), and system information (`uname`, `df`, `du`), and potentially downloading and serving content using a Python webserver.
* **Processes 101:** Understanding how processes work in Linux, how to view running processes, and how to manage them (e.g., `ps`, `kill`).
* **Maintaining Your System: Automation:** Learning about tools and techniques for automating tasks in Linux, such as `cron` jobs.
* **Maintaining Your System: Package Management:** Understanding how to manage software packages on your Linux system using tools like `apt` (Debian/Ubuntu based) or `yum`/`dnf` (Red Hat based).
* **Maintaining Your System: Logs:** Learning about system and application logs, their importance for troubleshooting, and how to view and manage them (e.g., using `journalctl`, viewing files in `/var/log`).
* **Conclusions & Summaries:** Reviewing the key concepts and commands learned throughout Part 3.

## Commands Used

*(Based on the "Key Concepts", you likely encountered commands like:)*

* `nano`: A simple terminal-based text editor.
* `vim`: A powerful and highly configurable terminal-based text editor.
* `tar`: An archiving utility.
* `gzip`: A compression utility.
* `gunzip`: A decompression utility.
* `top`: Displays dynamic real-time views of a running system's processes.
* `htop`: An interactive process viewer.
* `uname`: Displays system information.
* `df`: Displays disk space usage.
* `du`: Displays file and directory space usage.
* `ps`: Displays information about running processes.
* `kill`: Terminates processes.
* `cron`: A time-based job scheduler.
* `apt`: Package management tool for Debian and Ubuntu based systems.
* `yum`: Package management tool for older Red Hat based systems.
* `dnf`: Package management tool for newer Red Hat based systems.
* `journalctl`: A utility for querying and displaying logs collected by systemd.
* `cat`, `less`, `tail`: Commands for viewing log files.
* `python -m http.server <port>`: To serve content using a Python webserver.
* `wget`: To download content from a webserver.

*(Make sure this list reflects the actual commands you used in the room.)*

## What I Learned

In this final part of the Linux Fundamentals module, I learned how to effectively use terminal-based text editors for creating and modifying files, with helpful resources for learning Vim. I explored various general utilities for tasks such as archiving and compressing files, monitoring system resources and processes, and obtaining system information. I also gained an understanding of how Linux manages processes and how to interact with them. Furthermore, I learned how to maintain and automate my Linux system using `cron` for task scheduling, managing software packages with the appropriate package manager, and reviewing system and application logs for troubleshooting. I also got introduced to using Python's simple HTTP server to serve files and `wget` to download them.

## Room Link

\[[TryHackMe Room](https://tryhackme.com/room/linuxfundamentalspart3)\]

---

**Continue Your Learning:**

* **Bash Scripting:** \[[https://tryhackme.com/room/bashscripting](https://tryhackme.com/room/bashscripting)\]
* **Regular Expressions:** \[[https://tryhackme.com/room/catregex](https://tryhackme.com/room/catregex)\]
