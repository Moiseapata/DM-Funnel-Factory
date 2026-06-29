# 🧪 Live Test Results – Claude API Prompts

All prompts were tested on Claude (claude.ai) on June 29, 2026. These are real, unedited outputs proving the prompt library works.

---

## 1. Opt-in DM

**Prompt used:** `prompts/opt-in-dm.md`

**Variables:**
- Target: Aspiring course creators
- Webinar: How to Launch Your First Online Course in 30 Days
- Tone: Inspirational

**Claude Output:**
> Hey [First Name]! ✨ Dreaming of turning your expertise into an online course, but the thought of doing it all alone keeps you stuck before you even start? My free webinar shows you how to go from idea to launch in 30 days, stress-free — reply 'WEBINAR' for the link!

---

## 2. Nurture DM

**Prompt used:** `prompts/nurture-dm.md`

**Variables:**
- Date/Time: June 10, 2 PM EST
- Benefits: Validate idea, 3-step framework, attract first students

**Claude Output:**
> Here's your link: [LINK] — join us June 10 at 2 PM EST for a moment that could change everything for you. ✨ You'll learn: 1) How to validate your course idea, 2) The 3-step launch framework, and 3) How to attract your first students. Can't wait to see you there! 🙌

---

## 3. Reminder DM

**Prompt used:** `prompts/reminder-dm.md`

**Variables:**
- Key topic: How to launch without overwhelm

**Claude Output:**
> Hey [First Name], the webinar starts in 1 hour! 🚀 Join us here: [LINK] — we're diving into how to launch your course without the overwhelm or the stress. Don't miss this moment, it could change your trajectory!

---

## 4. Sales DM

**Prompt used:** `prompts/sales-dm.md`

**Variables:**
- Program: Course Launch Lab
- Pain point: Guesswork and overwhelm

**Claude Output:**
> Thank you so much for being there for the webinar! ✨ You now have the exact steps to launch your course, but I know turning theory into action alone can quickly turn into doubt and overwhelm. That's exactly why Course Launch Lab exists — to walk with you, step by step, with no guesswork, all the way to launch. If you feel it's time to move forward with real support, reply 'YES' and let's talk. 🙌

---

## 5. Brand Voice Adaptation (Prince EA)

**Prompt used:** `prompts/brand-voice-adapter.md`

**Original message:** "Hey [First Name]! Want to turn your expertise into a profitable online course—but not sure where to start? My free webinar shows you the exact steps to launch in 30 days. Reply 'WEBINAR' for the link!"

**Claude Output (Prince EA tone):**
> Hey [First Name]... imagine for a moment waking up every single day knowing that the course living inside you isn't just an idea anymore — it's out there, transforming lives, giving people the exact thing they've been searching for. ✨ You already have the expertise. What you might be missing is the path that turns it into something that resonates, something that matters. My free webinar walks you through the exact steps to launch your course in 30 days — with purpose, with clarity, with meaning. 🙌 Reply 'WEBINAR' and let's begin this journey together.

---

## 6. Brand Voice Adaptation (Nike)

**Prompt used:** `prompts/brand-voice-adapter.md`

**Original message:** (same as above)

**Claude Output (Nike tone):**
> Hey [First Name]. Got expertise? Turn it into a course. Fast. My free webinar shows you how — exact steps, 30 days, real results. Ready? Reply 'WEBINAR' for the link.

---

## 7. Brand Voice Adaptation (Mindvalley)

**Prompt used:** `prompts/brand-voice-adapter.md`

**Original message:** (same as above)

**Claude Output (Mindvalley tone):**
> Hey [First Name]... what if the course you're meant to create already exists within you, waiting for the right path to reveal itself? 🌟 There's a hidden process behind every successful launch — one most people never uncover. My free webinar reveals the secret steps to launching effortlessly in 30 days. ✨ Curious? Reply 'WEBINAR' and discover the truth.

---

## 8. AI Optimizer (Raw → Human-Optimized)

**Prompt used:** `prompts/ai-optimizer.md`

**Raw AI input:** "Hey [First Name]! Ever dreamed of turning your knowledge into a course that changes lives? My free webinar shows you how. Reply 'WEBINAR' for the link!"

**Claude Output (Optimized + changelog):**
> **Optimized message:**
>
> Hey [First Name]! Got the knowledge but no idea where to even start turning it into a course? My free webinar breaks down the exact 3-step framework to launch in 30 days — even if you're starting from zero. Reply 'WEBINAR' now and I'll send you the link.
>
> **Changes made:**
> - **Added pain point** ("no idea where to even start") — replaces the vague "ever dreamed" with the audience's real frustration: the freeze at the starting line, not just lack of ambition.
> - **Added specificity** ("3-step framework," "30 days," "starting from zero") — replaces "shows you how" with a concrete, numbered framework, making the promise credible.
> - **Cut the fluff** — "changes lives" was a broad, generic promise; removed to get straight to the concrete benefit.
> - **Strengthened CTA** ("Reply 'WEBINAR' now") — added "now" to create an immediate action trigger with zero friction.
> - **More human tone** — phrasing it as a direct question ("Got the knowledge but no idea where to start?") feels like real conversation, not a script.

---

## ✅ Key Takeaways from Testing

1. All prompts produced **usable, on-brand copy** on the first attempt
2. The **Brand Voice Adapter** successfully transformed one message into three completely different tones
3. The **AI Optimizer** demonstrated the critical difference between raw AI output and conversion-ready copy
4. These prompts are now **proven, versioned, and ready for automation** via Make.com or direct API calls
