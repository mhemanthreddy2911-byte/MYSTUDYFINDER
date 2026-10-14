# STUDYFINDER INDIA 🇮🇳
### *“Find. Compare. Rank. Choose. Succeed.”*

**StudyFinder India** is a colorful, intelligent, mobile-first education discovery, ranking, and talent platform engineered to help students and parents discover, evaluate, compare, and connect with educational institutions anywhere in India — from premier universities (IITs, IIMs, AIIMS, NLUs) to leading schools, sports academies, creative arts conservatories, coaching centers, and verified student coliving.

---

## 🌟 Key Platform Pillars

### 1. Nationwide Education Discovery
- **Comprehensive Pan-India Coverage**: Seamless discovery across states (Delhi NCR, Maharashtra, Karnataka, Tamil Nadu, Gujarat, Rajasthan, Telangana, Uttarakhand, and more) without restricting searches to local GPS coordinates.
- **Full Spectrum of All 10 Institutional Categories**:
  1. **Schools & Junior Colleges**: Top CBSE, ICSE, and IB Day & Boarding schools (The Doon School, DPS R.K. Puram, The Cathedral & John Connon School).
  2. **Junior & Degree Colleges**: Premier arts, science, and commerce institutions (St. Xavier's Mumbai, SRCC Delhi).
  3. **Engineering & Tech Colleges**: Apex institutes (IIT Bombay, IIT Madras, BITS Pilani, NIT Trichy).
  4. **Medical Colleges**: Clinical healthcare giants (AIIMS New Delhi, CMC Vellore).
  5. **Management & B-Schools**: Pioneer business academies (IIM Ahmedabad).
  6. **Law Colleges**: Top National Law Universities (NLSIU Bengaluru, NALSAR Hyderabad).
  7. **Sports, Music, Dance & Arts Academies**: High-performance talent hubs (Padukone-Dravid Centre for Sports Excellence, Kalakshetra Foundation, National School of Drama, Bhaichung Bhutia Football Schools).
  8. **Research Institutes & Vocational Centers**: Scientific and creative powerhouses (IISc Bengaluru, National Institute of Design Ahmedabad).
  9. **Coaching & Test Prep Academies**: India's benchmarks for competitive exam guidance (Allen Career Institute Kota, Vision IAS Delhi).
  10. **Student Hostels & Accommodations**: Verified, safe student coliving spaces (Stanza Living, Your-Space).
- **Multi-Facet Search & Filter**: Search by keyword, course, location, state, district, PIN code (e.g. `110029`, `560012`), fee slider, facilities, ratings, and statutory verification status.

---

### 2. Advanced All-India Ranking System
- **12 Separate Transparent Leaderboards**:
  1. *Overall Institutional Performance* (Composite multi-factor index)
  2. *Teaching Quality and Teaching Methods* (Student-faculty ratio, pedagogy, PhD faculty %)
  3. *Academic Achievement* (Board results, competitive exam percentiles, university ranks)
  4. *Sports and Games* ("Top Schools for Sports in India" — Olympic standard facilities, national medals)
  5. *Cultural Events and Festivals* ("Best Cultural Activity Programs" — Asia's largest collegiate festivals like Mood Indigo, Saarang, Malhar, OASIS)
  6. *Dance, Music, Drama and Performing Arts* (Sangeet Natak Akademi and traditional gurukula lineages)
  7. *Innovation, Research and Technology* ("Institutions Excelling in Innovation" — patents, incubators, supercomputing)
  8. *Leadership and Student Development* (MUNs, student governance, entrepreneurship cells)
  9. *Infrastructure and Modern Facilities* (Smart classrooms, labs, libraries, athletic tracks)
  10. *Special Achievements and Unique Qualities* (Rare specializations, national awards)
  11. *Student Satisfaction and Parent Feedback* (Authentic verified sentiment)
  12. *Community Service and Extracurricular Participation* (NSS, rural healthcare outreach, environmental initiatives)
- **Transparent Methodology & Fraud Resistance**:
  - Independent verification: NIRF, NAAC A++, NBA, CBSE Gazette, and physical audit logs.
  - Zero paid ranking boosts: Algorithms strictly isolate commercial promotion from merit scoring.
  - **Data Sufficiency Indicators**: Non-applicable or unverified categories are clearly marked as `"Data Insufficient"` rather than fabricating misleading comparisons.

---

### 3. Rich Institution Profiles & Direct Actions
- **Rich Media & Data**: Verified badges, accreditation tags, course seat matrices, annual fee breakdowns (tuition, hostel, mess, scholarships), faculty ratios, sports facilities, and placement statistics.
- **Prominent Direct Action Controls**:
  - 📞 **Call Office**: Instant hotline and campus admissions hours.
  - 💬 **Live Counselor Chat**: Intelligent conversational admissions assistant powered by verified institutional data.
  - ✉️ **Email Admissions**: Direct enquiry dispatch.
  - 🌐 **Visit Official Website**: 1-click external link.
  - 📄 **Request Brochure**: Instant digital prospectus generation.
  - 🎯 **Enquire Now**: Lead capture with automated counselor routing.
  - 🗓️ **Book Campus Visit**: Guided tour scheduler with authorized digital QR visit passes.
  - ⚖️ **Add to Compare**: Multi-institution side-by-side comparison drawer.
  - ❤️ **Save to Shortlist**: LocalStorage-synced personal bookmarking.

---

### 4. Side-by-Side Comparison Matrix
- Compare **2 to 4 institutions** side-by-side across:
  - Annual fees and scholarship provisions
  - National overall & category ranks
  - Student-to-faculty ratios and PhD percentages
  - Highest and average placement packages
  - Hostel accommodations and campus sports facilities
  - Statutory approvals and accreditation grades

---

### 5. AI-Powered "EduMatch" Recommendation Engine
- **4-Step Matching Questionnaire**:
  1. *Education Stage* (School, UG, PG, Sports/Arts, Coaching, Hostel)
  2. *Target Discipline / Field* (Engineering, Medicine, Management, Law, Commerce, Sports, Design, Civil Services)
  3. *Location Flexibility & Budget Ceiling*
  4. *Priorities* (High Placements, Sports, Cultural Fests, Research, Affordable Fees, High Faculty Ratio)
- Calculates a multi-factor compatibility score (**0% to 100% Match**) and outputs personalized rationale explaining why the institution matches the applicant.

---

### 6. Trust, Verification & Institution Management
- **Statutory Claim Submission**: Registrars and Principals can claim their institution and upload accreditation letters for StudyFinder Platinum/Gold Verified badges.
- **Anti-Fraud Review Safeguards**: Reviews are screened for spam patterns, commercial solicitations, and verified against student enrollment tokens.
- **Public Discrepancy Reporting**: Students and parents can report inaccurate fees, expired dates, or false claims for immediate audit investigation.
- **Institution Registrar Portal**: Live dashboard to inspect incoming student enquiries, review campus visit passes, and monitor verification compliance.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ (Python 3.13 tested)
- FastAPI & Uvicorn (installed)

### 1-Click Launch (Windows)
Double-click `start.bat` or run:
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then open your browser to:
👉 **`http://localhost:8000`**

---

## 📁 Project Architecture
```
study-finder/
├── main.py                     # FastAPI server, REST routes & live chat engine
├── requirements.txt            # Dependencies (fastapi, uvicorn, pydantic)
├── start.bat                   # 1-click Windows launcher script
├── README.md                   # Complete documentation
├── data/
│   └── institutions.json       # 24+ verified premier institutions across 10 categories
├── services/
│   ├── ranking_engine.py       # 12-category transparent scoring algorithms
│   ├── search_service.py       # Multi-facet search, PIN code matcher & facet aggregator
│   ├── ai_recommender.py       # Multi-vector EduMatch recommendation engine
│   └── verification.py         # Anti-fraud verification, claim review & report desk
└── static/
    ├── index.html              # Mobile-first responsive single-page application
    ├── css/
    │   └── style.css           # Glassmorphism, animations & color tokens
    └── js/
        ├── app.js              # State manager, router, bookmarks & compare drawer
        ├── search.js           # Search inputs, filters, sliders & card rendering
        ├── rankings.js         # 12 Leaderboards & audit transparency views
        ├── profile.js          # Detailed dossier modal & direct action toolbar
        ├── compare.js          # Side-by-side comparative matrix
        ├── ai_matcher.js       # AI EduMatch wizard & results
        └── admin.js            # Institution claims, enquiries, visits & live chat
```
