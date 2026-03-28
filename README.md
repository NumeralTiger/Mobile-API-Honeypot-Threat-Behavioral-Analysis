# Mobile API Honeypot Threat Behavioral Analysis

## Behavioral Analysis of Unauthorized Location Service Exploitation

---

## Abstract
This project investigates the threat landscape of mobile location privacy by deploying a high-interaction honeypot simulating smartphone API endpoints. The goal was to analyze attacker behavior when encountering "Privacy-First" error responses (the privacy paradox in action).

---

## Architecture

### Sensor Layer
- Custom Flask-based Honey-API mimicking RESTful mobile services

### Analytics Layer
- ELK Stack for real-time visualization of global attack origins

### Containment
- Dockerized environment with automated IP shunning via Fail2Ban

---

## Key Findings

### Automated Reconnaissance
- 85% of attempts originated from known botnets targeting port 8080

### User-Agent Analysis
- Identified a trend of attackers spoofing mobile browser headers to bypass traditional WAFs
