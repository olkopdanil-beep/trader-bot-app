# PROJECT_CONTEXT.md

## Project Name

Trader Bot AI Mini App

---

# Project Goal

Create a Telegram Mini App that analyzes trading chart screenshots using AI vision models and returns simplified market direction predictions (UP/DOWN) with confidence and reasoning.

The project is NOT intended to be a real institutional trading system.

Primary business goal:

* user acquisition
* engagement
* retention
* affiliate funnel traffic
* AI perception + trading UX

---

# Current Stack

## Backend

* Python 3.13
* FastAPI
* Uvicorn
* Google Gemini API
* python-dotenv

## Telegram

* pyTelegramBotAPI
* Telegram Bot API
* Telegram Mini App integration

## Frontend

* Vanilla HTML
* Vanilla CSS
* Vanilla JavaScript
* Cyberpunk / Matrix terminal UI

---

# Current Architecture

Telegram User
?
Telegram Bot
?
Telegram Mini App
?
Frontend Upload UI
?
FastAPI Backend
?
Gemini Vision Analysis
?
Response JSON
?
Frontend Signal Rendering

---

# Existing Features

## Telegram Bot

* /start command
* inline button opening Mini App
* Telegram polling mode

## Mini App

* upload screenshot
* analyze button
* loading state
* AI signal output
* confidence display
* reasoning text

## Backend

* image upload endpoint
* Gemini API request
* AI prompt generation
* JSON response

---

# Project Philosophy

IMPORTANT:
This project is an MVP.

Do NOT overengineer.

The goal is:

* speed
* testing
* iteration
* retention
* viral potential

NOT:

* enterprise architecture
* complex infra
* perfect AI
* scalability optimization

---

# HARD RULES FOR AI AGENTS

## NEVER:

* rewrite project to React
* rewrite project to Next.js
* add Docker unless requested
* add PostgreSQL unless requested
* add Redis unless requested
* add authentication system
* add microservices
* add websocket complexity
* restructure whole project
* replace FastAPI
* replace Telegram architecture
* create unnecessary abstractions

---

# IMPORTANT DEVELOPMENT RULES

## Keep:

* FastAPI backend
* Vanilla frontend
* Telegram Mini App flow
* simple file structure
* fast iteration workflow

## Prioritize:

1. UX
2. Retention
3. Perceived AI quality
4. Simplicity
5. Fast deployment

---

# UI STYLE RULES

Visual identity:

* Matrix style
* cyberpunk trading terminal
* dark UI
* neon accents
* premium hacker aesthetic

Do NOT:

* make generic SaaS UI
* use bright white layouts
* remove cyberpunk atmosphere

---

# Current Product Positioning

The product should FEEL like:

* experimental AI trading system
* smart market scanner
* AI signal engine
* futuristic trading assistant

NOT:

* scam signal generator
* fake guru course
* complicated trading dashboard

---

# Current Technical Problems

## Known Issues

* Failed fetch issues when backend offline
* Telegram polling conflicts when multiple bot instances run
* no persistent signal history
* no retention mechanics
* no notifications system
* no analytics

---

# Current Priorities

## PRIORITY 1

Stabilize MVP.

## PRIORITY 2

Improve frontend UX.

## PRIORITY 3

Increase retention.

## PRIORITY 4

Improve perceived AI depth.

---

# Planned Features

## Short-Term

* signal history
* confidence colors
* better loading animations
* AI market status block
* richer reasoning output
* improved error handling

## Mid-Term

* signal feed
* Telegram channel integration
* engagement notifications
* trending assets section
* session memory

## Long-Term

* analytics
* user tracking
* affiliate optimization
* viral mechanics

---

# Folder Expectations

## backend/

Contains:

* FastAPI app
* Gemini integration
* API endpoints

## frontend/

Contains:

* HTML
* CSS
* JS
* Mini App UI

## bot.py

Telegram bot entry point.

---

# AI Coding Instructions

When modifying code:

1. Make minimal safe changes.
2. Do not rewrite working systems.
3. Preserve existing UI style.
4. Preserve Telegram flow.
5. Avoid unnecessary dependencies.
6. Explain major changes before applying.
7. Keep files readable.
8. Prefer direct solutions over abstractions.

---

# Terminal Workflow

## Backend

```bash
cd backend
uvicorn main:app --reload
```

## Bot

```bash
python bot.py
```

---

# Environment Variables

Stored in .env.

Expected values:

* TELEGRAM_BOT_TOKEN
* GEMINI_API_KEY
* MINI_APP_URL

IMPORTANT:
Never expose secrets.
Never commit .env.

---

# Git Rules

Required .gitignore entries:

```gitignore
.env
__pycache__/
```

---

# Product Strategy

Core strategy:

YouTube / Social Traffic
? Telegram Bot
? Mini App
? AI Analysis Experience
? Retention
? Affiliate Funnel

---

# Important Product Insight

The project is NOT selling accurate trading.

The product is selling:

* curiosity
* AI experience
* engagement
* experimentation
* futuristic interaction

This distinction is critical.

---

# Content Strategy Direction

Recommended content style:

* AI vs market
* AI trading experiments
* challenge videos
* documentary progression
* daily AI performance

Avoid:

* guru content
* fake flexing
* pure signals content

---

# Final Principle

SHIP FAST.
DO NOT CHASE PERFECTION.
ITERATE BASED ON REAL USER BEHAVIOR.