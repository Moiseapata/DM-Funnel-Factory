# ⚡ Automation Blueprint – DM Funnel Generation System

## Overview

This blueprint automates the entire DM funnel creation process using **Make.com** (or Zapier), **Claude API**, and **Google Sheets**. It transforms a client brief into a polished 4-step DM funnel delivered to a Slack channel in minutes, not hours.

---

## Tools Required

| Tool | Purpose |
|:---|:---|
| **Google Sheets** | Client brief input & final copy storage |
| **Claude API** | AI copy generation using engineered prompts |
| **Make.com** | Workflow orchestration |
| **Slack** | Team review & approval |

---

## Step-by-Step Workflow

### 1. Trigger: New Client Brief Submitted

A new row is added to the **"Client Briefs"** Google Sheet with these columns:

| Column | Example |
|:---|:---|
| Client Name | Amy Porterfield |
| Webinar Title | How to Launch Your First Online Course |
| Tone | Inspirational |
| Target Audience | Aspiring course creators |
| Benefit 1 | Validate your course idea |
| Benefit 2 | 3-step launch framework |
| Benefit 3 | Attract first students |
| CTA Trigger | WEBINAR |
| Program Name | Course Launch Lab |

### 2. Make.com Webhook Catches the Row

- A **Google Sheets "Watch New Row"** module triggers the workflow
- The row data is parsed into a structured JSON payload

### 3. Claude API Generates the 4-Step Funnel

Four sequential HTTP requests are made to the Claude API, each using an **engineered prompt** from the prompt library:

### 4. Output Formatting

The 4 generated messages are compiled into a formatted Slack message:

### 5. Slack Delivery

The formatted funnel is posted to a private **#dm-copy-review** Slack channel for the creative team to review.

### 6. Human Approval & Storage

- Team members approve or request edits via Slack thread
- Approved funnels are automatically saved to the **"Final Copy"** tab in Google Sheets

---

## Workflow Diagram

```mermaid
graph TD
    A[New Row in Google Sheets] --> B[Make.com Trigger]
    B --> C[Parse Row Data to JSON]
    C --> D1[Claude API: Opt-in DM Prompt]
    C --> D2[Claude API: Nurture DM Prompt]
    C --> D3[Claude API: Reminder DM Prompt]
    C --> D4[Claude API: Sales DM Prompt]
    D1 --> E[Compile 4-Step Funnel]
    D2 --> E
    D3 --> E
    D4 --> E
    E --> F[Format for Slack]
    F --> G[Post to #dm-copy-review]
    G --> H[Human Review]
    H --> I[Save Final Version to Google Sheets]
