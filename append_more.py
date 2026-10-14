import json

more_institutions = [
    {
        "id": "bits-pilani",
        "name": "Birla Institute of Technology and Science (BITS Pilani)",
        "tagline": "Innovate, Achieve, Lead — Zero Attendance Freedom & Startup Incubation",
        "type": "Engineering",
        "category_label": "Engineering & Technology",
        "established_year": 1964,
        "ownership": "Private Deemed University (Institution of Eminence)",
        "affiliation": "Deemed to be University under Section 3 of UGC Act",
        "accreditations": ["NAAC 'A' Grade", "Institution of Eminence (IoE)", "UGC & AICTE Recognized"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Platinum Verified",
        "verification_details": {
            "verified_by": "StudyFinder Central Audit Panel",
            "verification_date": "2026-07-20",
            "documents_checked": ["Ministry of Education IoE Gazette", "NAAC Accreditation", "Practice School Industry Audit"],
            "official_id": "INST-PVT-BITS-1964",
            "audit_rating": "4.9 / 5.0"
        },
        "location": {
            "address": "Vidya Vihar Campus",
            "city": "Pilani",
            "district": "Jhunjhunu",
            "state": "Rajasthan",
            "zone": "North India",
            "pincode": "333031",
            "coordinates": {"lat": 28.3639, "lng": 75.5870}
        },
        "contact": {
            "phone": "+91 1596 242 210",
            "helpline": "1800-159-BITS",
            "email": "admissions@pilani.bits-pilani.ac.in",
            "website": "https://www.bits-pilani.ac.in",
            "brochure_name": "BITS_Pilani_Information_Brochure_2026.pdf"
        },
        "fees": {
            "min_annual": 490000,
            "max_annual": 580000,
            "average_annual": 535000,
            "currency": "INR",
            "fee_display": "₹4.9L - ₹5.8L / year",
            "hostel_annual": 65000,
            "scholarships": [
                "Merit-cum-Need Scholarships covering up to 80% tuition for eligible students",
                "Institute Top 1% Merit Scholarship (100% Tuition Waiver)",
                "BITS Alumni Association Global Endowment Awards"
            ],
            "fee_breakdown": [
                {"course": "B.E. Computer Science", "tuition": 475000, "hostel": 65000, "other": 25000, "duration": "4 Years"},
                {"course": "B.E. Electronics & Communication", "tuition": 475000, "hostel": 65000, "other": 25000, "duration": "4 Years"},
                {"course": "M.Sc. Dual Degree Programs", "tuition": 475000, "hostel": 65000, "other": 25000, "duration": "5 Years"},
                {"course": "Higher Degree M.E. / M.Pharm", "tuition": 380000, "hostel": 65000, "other": 20000, "duration": "2 Years"}
            ]
        },
        "ratings": {
            "overall": 4.91,
            "total_reviews": 690,
            "academic": 4.9,
            "teaching": 4.9,
            "sports": 4.8,
            "cultural": 5.0,
            "infrastructure": 4.9,
            "placement": 4.9,
            "value_for_money": 4.6
        },
        "category_scores": {
            "overall_performance": 97.6,
            "teaching_quality": 97.4,
            "academic_achievement": 98.2,
            "sports_games": 93.0,
            "cultural_festivals": 99.0,
            "performing_arts": 92.0,
            "innovation_research": 98.5,
            "leadership_development": 99.0,
            "infrastructure_facilities": 98.0,
            "special_achievements": 98.2,
            "student_satisfaction": 96.8,
            "community_service": 92.5
        },
        "ranks": {
            "national_overall": 4,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 3,
            "sports_rank": 6,
            "teaching_rank": 3,
            "cultural_rank": 2,
            "innovation_rank": 4
        },
        "courses_offered": [
            {"name": "B.E. (Hons.) Computer Science", "degree": "Undergraduate", "duration": "4 Years", "seats": 220, "eligibility": "BITSAT Score 335+", "fees": "₹5.35L / yr"},
            {"name": "B.E. (Hons.) Electronics & Instrumentation", "degree": "Undergraduate", "duration": "4 Years", "seats": 140, "eligibility": "BITSAT Score 290+", "fees": "₹5.35L / yr"},
            {"name": "M.Sc. Economics (Dual Degree)", "degree": "Integrated Master", "duration": "5 Years", "seats": 110, "eligibility": "BITSAT Score 285+", "fees": "₹5.35L / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 480,
            "student_faculty_ratio": "1:11",
            "phd_percentage": "94%",
            "notable_faculty": [
                "Prof. V. Ramgopal Rao (Group Vice-Chancellor & Former IITD Director)",
                "Prof. Sudhirkumar Barai (Director & Structural Engineering specialist)",
                "Prof. Chandra Shekhar (Semiconductor Design & Microelectronics)"
            ]
        },
        "facilities": [
            "328-acre self-contained heritage campus with iconic Clock Tower",
            "Technology Business Incubator (Pilani Innovation & Entrepreneurship Development Society)",
            "Practice School System (Mandatory 7.5-month full-time paid corporate internship program)",
            "Zero Attendance Policy encouraging student self-motivation, startup building, and research",
            "Massive student sports complex with floodlit cricket stadium, football arena, gym and swimming pool",
            "Modern air-cooled hostels for 100% students with high-speed campus LAN"
        ],
        "sports_highlights": [
            "BOSM (BITS Open Sports Meet) - One of India's largest national inter-college sports festivals",
            "Top inter-collegiate medals in cricket, basketball, tennis, and powerlifting"
        ],
        "cultural_highlights": [
            "OASIS - Asia's 2nd largest cultural festival (96 continuous hours of music, dance, and arts)",
            "APOGEE - Premier ISO 9001:2008 certified international technical festival"
        ],
        "placements": {
            "highest_package": "₹1.44 Crore / year (International) / ₹60.8 LPA (Domestic)",
            "average_package": "₹21.8 LPA",
            "median_package": "₹18.5 LPA",
            "placement_rate": "96.5%",
            "top_recruiters": ["Google", "Microsoft", "Nvidia", "Amazon", "Apple", "Uber", "De Shaw", "Goldman Sachs", "Da Vinci Derivatives"]
        },
        "admissions": {
            "process": "Online computer-based BITSAT examination conducted across two sessions nationwide.",
            "application_period": "January - June 2026",
            "entrance_exams": ["BITSAT"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.bits-pilani.ac.in"
        },
        "reviews": [
            {
                "author": "Rishi Agarwal",
                "role": "B.E. CSE Alumnus (Founder of Tech Unicorn)",
                "rating": 5,
                "date": "2026-02-22",
                "title": "Zero attendance and Practice School gave me freedom to build",
                "comment": "BITS treats you like an adult. You manage your own time, explore startups without attendance worries, and the alumni network is the most tight-knit in India.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["NIRF Engineering Top 25", "IoE Status Ministry of Education", "QS Asia University Rankings"],
            "last_audited": "2026-07-18",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "nit-trichy",
        "name": "National Institute of Technology Tiruchirappalli (NIT Trichy)",
        "tagline": "India's #1 National Institute of Technology",
        "type": "Engineering",
        "category_label": "Engineering & Technology",
        "established_year": 1964,
        "ownership": "Public (Institute of National Importance)",
        "affiliation": "Autonomous (Government of India)",
        "accreditations": ["NIRF #9 Engineering (Top among all NITs)", "NIRF #1 NIT in India", "NBA Tier-I Accredited"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Platinum Verified",
        "verification_details": {
            "verified_by": "StudyFinder Central Audit Panel",
            "verification_date": "2026-07-15",
            "documents_checked": ["NIT Act 2007 Gazette", "NIRF 2025 Ranking Verification", "NBA Tier-1 Documents"],
            "official_id": "INST-GOI-NITT-1964",
            "audit_rating": "4.9 / 5.0"
        },
        "location": {
            "address": "Tanjore Main Road, National Highway 67, Thuvakudi",
            "city": "Tiruchirappalli",
            "district": "Tiruchirappalli",
            "state": "Tamil Nadu",
            "zone": "South India",
            "pincode": "620015",
            "coordinates": {"lat": 10.7589, "lng": 78.8132}
        },
        "contact": {
            "phone": "+91 431 250 3000",
            "helpline": "1800-431-NITT",
            "email": "deanac@nitt.edu",
            "website": "https://www.nitt.edu",
            "brochure_name": "NIT_Trichy_Prospectus_2026.pdf"
        },
        "fees": {
            "min_annual": 175000,
            "max_annual": 235000,
            "average_annual": 195000,
            "currency": "INR",
            "fee_display": "₹1.75L - ₹2.35L / year",
            "hostel_annual": 42000,
            "scholarships": [
                "Fee Remission for Economically Weaker Section (100% waiver if family income < ₹1L)",
                "Central Sector Scholarship for Top SC/ST Candidates",
                "RECAL Alumni Scholarships"
            ],
            "fee_breakdown": [
                {"course": "B.Tech All Streams", "tuition": 125000, "hostel": 42000, "other": 28000, "duration": "4 Years"},
                {"course": "B.Arch (Architecture)", "tuition": 125000, "hostel": 42000, "other": 30000, "duration": "5 Years"},
                {"course": "M.Tech / MCA", "tuition": 70000, "hostel": 42000, "other": 22000, "duration": "2-3 Years"}
            ]
        },
        "ratings": {
            "overall": 4.88,
            "total_reviews": 650,
            "academic": 4.9,
            "teaching": 4.9,
            "sports": 4.8,
            "cultural": 4.9,
            "infrastructure": 4.8,
            "placement": 4.9,
            "value_for_money": 4.9
        },
        "category_scores": {
            "overall_performance": 97.2,
            "teaching_quality": 97.0,
            "academic_achievement": 97.8,
            "sports_games": 94.0,
            "cultural_festivals": 97.0,
            "performing_arts": 89.0,
            "innovation_research": 97.5,
            "leadership_development": 96.5,
            "infrastructure_facilities": 97.0,
            "special_achievements": 97.0,
            "student_satisfaction": 96.0,
            "community_service": 93.0
        },
        "ranks": {
            "national_overall": 5,
            "state_rank": 2,
            "district_rank": 1,
            "category_rank": 4,
            "sports_rank": 5,
            "teaching_rank": 4,
            "cultural_rank": 5,
            "innovation_rank": 5
        },
        "courses_offered": [
            {"name": "B.Tech Computer Science & Engineering", "degree": "Undergraduate", "duration": "4 Years", "seats": 140, "eligibility": "JEE Main Top 1200 AIR", "fees": "₹1.95L / yr"},
            {"name": "B.Tech Electrical & Electronics", "degree": "Undergraduate", "duration": "4 Years", "seats": 120, "eligibility": "JEE Main Top 5000 AIR", "fees": "₹1.95L / yr"},
            {"name": "B.Tech Mechanical Engineering", "degree": "Undergraduate", "duration": "4 Years", "seats": 120, "eligibility": "JEE Main Top 7500 AIR", "fees": "₹1.95L / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 360,
            "student_faculty_ratio": "1:12",
            "phd_percentage": "96%",
            "notable_faculty": [
                "Dr. G. Aghila (Director & AI Data Security Specialist)",
                "Dr. N. Sivakumaran (Instrumentation & Controls pioneer)"
            ]
        },
        "facilities": [
            "800-acre expansive campus with dedicated bicycle tracks and green energy systems",
            "Center of Excellence in Manufacturing and Siemens Industry 4.0 Lab",
            "Orion Lecture Hall Complex (state-of-the-art smart audio-visual theatres)",
            "Modern Sports Complex with Olympic swimming pool, 400m synthetic running track, indoor badminton",
            "Over 22 student hostels with dedicated mess serving North and South Indian food"
        ],
        "sports_highlights": [
            "Inter-NIT National Sports Meet Overall Champions (2024, 2025)",
            "State-of-the-art athletic tracks and active sports clubs"
        ],
        "cultural_highlights": [
            "Festember - South India's largest annual cultural fest (certified ISO 9001, footfall 18,000+)",
            "Pragyan - ISO 9001 and ISO 20121 certified international techno-managerial fest"
        ],
        "placements": {
            "highest_package": "₹52.89 LPA (Domestic) / ₹1.1 Crore (International)",
            "average_package": "₹20.4 LPA (CSE) / ₹15.8 LPA (Overall)",
            "median_package": "₹14.2 LPA",
            "placement_rate": "95.5%",
            "top_recruiters": ["Google", "Microsoft", "Amazon", "Texas Instruments", "Qualcomm", "Morgan Stanley", "Samsung R&D", "L&T"]
        },
        "admissions": {
            "process": "JEE Main through JoSAA and CSAB centralized counseling.",
            "application_period": "November - June 2026",
            "entrance_exams": ["JEE Main"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.nitt.edu"
        },
        "reviews": [
            {
                "author": "Vignesh Rajan",
                "role": "B.Tech CSE Class of 2025",
                "rating": 5,
                "date": "2026-02-15",
                "title": "Festember and Pragyan give you incredible management experience",
                "comment": "NIT Trichy gives you the best of both worlds: academic rigor equivalent to top IITs, and an energetic student fest culture that is completely run by students.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["NIRF Engineering 2025 #9", "Council of NITs Audit", "NBA Tier-1"],
            "last_audited": "2026-07-12",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "nid-ahmedabad",
        "name": "National Institute of Design (NID Ahmedabad)",
        "tagline": "India's Apex Design Institution & Institute of National Importance",
        "type": "Vocational & Design",
        "category_label": "Research Institutes & Universities",
        "established_year": 1961,
        "ownership": "Autonomous Body under Ministry of Commerce and Industry",
        "affiliation": "Institute of National Importance (Government of India)",
        "accreditations": ["NID Act 2014 GoI", "World Design Organization (WDO) Member"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Platinum Verified",
        "verification_details": {
            "verified_by": "StudyFinder Design & Vocational Wing",
            "verification_date": "2026-06-25",
            "documents_checked": ["NID Act 2014 Gazette", "Ministry of Commerce Audit", "WDO Global Affiliation"],
            "official_id": "INST-GOI-NID-1961",
            "audit_rating": "5.0 / 5.0"
        },
        "location": {
            "address": "Opposite Tagore Hall, Rajnagar Society, Paldi",
            "city": "Ahmedabad",
            "district": "Ahmedabad",
            "state": "Gujarat",
            "zone": "Western India",
            "pincode": "380007",
            "coordinates": {"lat": 23.0132, "lng": 72.5691}
        },
        "contact": {
            "phone": "+91 79 2662 3692",
            "helpline": "1800-79-NIDD",
            "email": "admissions@nid.edu",
            "website": "https://www.nid.edu",
            "brochure_name": "NID_Design_Admissions_2026.pdf"
        },
        "fees": {
            "min_annual": 320000,
            "max_annual": 410000,
            "average_annual": 365000,
            "currency": "INR",
            "fee_display": "₹3.2L - ₹4.1L / year",
            "hostel_annual": 65000,
            "scholarships": [
                "NID Financial Aid Scheme (Up to 100% Tuition Remission for deserving students)",
                "Ford Foundation Design Scholarships",
                "Government of India Central Sector Grants"
            ],
            "fee_breakdown": [
                {"course": "B.Des in Product / Graphic / Animation Design", "tuition": 345000, "hostel": 65000, "other": 25000, "duration": "4 Years"},
                {"course": "M.Des in Interaction / Transportation / Universal Design", "tuition": 375000, "hostel": 65000, "other": 28000, "duration": "2.5 Years"}
            ]
        },
        "ratings": {
            "overall": 4.93,
            "total_reviews": 420,
            "academic": 4.9,
            "teaching": 5.0,
            "sports": 4.3,
            "cultural": 5.0,
            "infrastructure": 4.9,
            "placement": 4.9,
            "value_for_money": 4.8
        },
        "category_scores": {
            "overall_performance": 98.2,
            "teaching_quality": 99.4,
            "academic_achievement": 97.0,
            "sports_games": 80.0,
            "cultural_festivals": 99.2,
            "performing_arts": 96.0,
            "innovation_research": 99.0,
            "leadership_development": 97.0,
            "infrastructure_facilities": 97.5,
            "special_achievements": 99.5,
            "student_satisfaction": 98.0,
            "community_service": 94.0
        },
        "ranks": {
            "national_overall": 1,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 1,
            "sports_rank": 30,
            "teaching_rank": 1,
            "cultural_rank": 3,
            "innovation_rank": 2
        },
        "courses_offered": [
            {"name": "B.Des in Industrial & Product Design", "degree": "Undergraduate", "duration": "4 Years", "seats": 45, "eligibility": "NID DAT Prelims & Mains Top Rank", "fees": "₹3.65L / yr"},
            {"name": "B.Des in Communication & Graphic Design", "degree": "Undergraduate", "duration": "4 Years", "seats": 40, "eligibility": "NID DAT Prelims & Mains", "fees": "₹3.65L / yr"},
            {"name": "M.Des in Interaction Design (UI/UX)", "degree": "Postgraduate", "duration": "2.5 Years", "seats": 25, "eligibility": "NID DAT PG + Portfolio Review", "fees": "₹3.90L / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 85,
            "student_faculty_ratio": "1:8",
            "phd_percentage": "Master Designers & International Bauhaus lineage",
            "notable_faculty": [
                "Dr. Praveen Nahar (Director & Sustainable Design Specialist)",
                "Prof. Tarun Deep Girdher (Graphic Design & Typography Authority)"
            ]
        },
        "facilities": [
            "Iconic Sabarmati riverfront campus designed by Gautam & Gira Sarabhai based on the Eames Report",
            "Prototyping workshops: Wood, Metal, Ceramics, Glass, Textiles, and Rapid 3D Prototyping",
            "Digital Interaction and AR/VR User Experience Experience Labs",
            "Knowledge Management Centre (KMC) with over 45,000 international design resources and materials library",
            "Design Vision Centre and Student Open Studios with 24/7 access"
        ],
        "sports_highlights": [
            "Yoga, table tennis, badminton, and riverfront athletics"
        ],
        "cultural_highlights": [
            "RGB - Annual National Design Festival celebrating creative intersections",
            "The Eames Lecture Series featuring global design luminaries"
        ],
        "placements": {
            "highest_package": "₹45 LPA (Product Design / UI/UX Leadership) & Global Design Consultancies",
            "average_package": "₹18.4 LPA",
            "median_package": "₹16.0 LPA",
            "placement_rate": "97%",
            "top_recruiters": ["Google Design", "Microsoft IDC", "Apple", "Samsung UX", "Tata Motors Design Studio", "IKEA", "Frog Design", "IDEO"]
        },
        "admissions": {
            "process": "Design Aptitude Test (DAT) Prelims followed by Studio Test & Personal Interview Mains.",
            "application_period": "September - December 2026",
            "entrance_exams": ["NID DAT Prelims", "NID DAT Mains"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.nid.edu"
        },
        "reviews": [
            {
                "author": "Aakriti Sen",
                "role": "B.Des Interaction Design 2024",
                "rating": 5,
                "date": "2026-02-11",
                "title": "A place that teaches you how to think, not just how to draw",
                "comment": "The hands-on workshop culture and critiques push your curiosity. Having 24/7 studio access means your ideas take physical form immediately.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["Ministry of Commerce & Industry, GoI", "World Design Organization Register", "StudyFinder Design Audit"],
            "last_audited": "2026-06-20",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "vision-ias-delhi",
        "name": "Vision IAS Academy",
        "tagline": "Pioneering Interactive Mentorship for UPSC Civil Services Examination",
        "type": "Coaching & Test Prep",
        "category_label": "Coaching Centers & Training Academies",
        "established_year": 2008,
        "ownership": "Private Civil Services Training Institute",
        "affiliation": "National Civil Services Preparation Institute",
        "accreditations": ["StudyFinder Civil Services Verified", "ISO 9001:2015"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Verified",
        "verification_details": {
            "verified_by": "StudyFinder Test-Prep Verification Wing",
            "verification_date": "2026-06-12",
            "documents_checked": ["Company Registration", "UPSC Final Result Affidavits", "Faculty Qualification Audit"],
            "official_id": "INST-CP-VIAS-2008",
            "audit_rating": "4.9 / 5.0"
        },
        "location": {
            "address": "635, 1st Floor, Main Road, Dr. Mukherjee Nagar",
            "city": "New Delhi",
            "district": "North West Delhi",
            "state": "Delhi",
            "zone": "North India",
            "pincode": "110009",
            "coordinates": {"lat": 28.7099, "lng": 77.2155}
        },
        "contact": {
            "phone": "+91 84680 22022",
            "helpline": "+91 90190 66066",
            "email": "enquiry@visionias.in",
            "website": "https://www.visionias.in",
            "brochure_name": "Vision_IAS_Foundation_Guide_2026.pdf"
        },
        "fees": {
            "min_annual": 135000,
            "max_annual": 195000,
            "average_annual": 165000,
            "currency": "INR",
            "fee_display": "₹1.35L - ₹1.95L / year",
            "hostel_annual": 130000,
            "scholarships": [
                "Abhyas All-India Merit Scholarship (Up to 100% Fee Remission)",
                "Special Concession for Serving Defense Personnel & Wards",
                "Divyangjan Disability Concession"
            ],
            "fee_breakdown": [
                {"course": "GS Foundation Course (Prelims + Mains + Interview)", "tuition": 165000, "hostel": 0, "other": 15000, "duration": "1 Year"},
                {"course": "All-India GS Prelims & Mains Test Series with Mentorship", "tuition": 32000, "hostel": 0, "other": 3000, "duration": "1 Year"},
                {"course": "CSAT & Essay Enrichment Modules", "tuition": 25000, "hostel": 0, "other": 2000, "duration": "6 Months"}
            ]
        },
        "ratings": {
            "overall": 4.89,
            "total_reviews": 980,
            "academic": 5.0,
            "teaching": 4.9,
            "sports": 3.5,
            "cultural": 4.0,
            "infrastructure": 4.8,
            "placement": 5.0,
            "value_for_money": 4.8
        },
        "category_scores": {
            "overall_performance": 96.2,
            "teaching_quality": 98.6,
            "academic_achievement": 99.5,
            "sports_games": 60.0,
            "cultural_festivals": 70.0,
            "performing_arts": 55.0,
            "innovation_research": 88.0,
            "leadership_development": 95.0,
            "infrastructure_facilities": 94.5,
            "special_achievements": 99.2,
            "student_satisfaction": 95.0,
            "community_service": 91.0
        },
        "ranks": {
            "national_overall": 1,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 1,
            "sports_rank": 42,
            "teaching_rank": 1,
            "cultural_rank": 26,
            "innovation_rank": 13
        },
        "courses_offered": [
            {"name": "UPSC GS Foundation 1-Year Comprehensive", "degree": "Civil Services Prep", "duration": "1 Year", "seats": 1200, "eligibility": "Graduation in any discipline", "fees": "₹1.65L / yr"},
            {"name": "All India Prelims & Mains Test Series", "degree": "Evaluation & Test Prep", "duration": "10 Months", "seats": 10000, "eligibility": "UPSC Aspirants", "fees": "₹32,000 / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 180,
            "student_faculty_ratio": "1:20 (With personal mentors)",
            "phd_percentage": "Ex-Civil Servants, Subject Authorities & Ph.D. Scholars",
            "notable_faculty": [
                "Ajay Kumar (Director & Ethics Pedagogy Specialist)",
                "Distinguished Retd. IAS and IFS officers on Mock Interview Panel"
            ]
        },
        "facilities": [
            "Modern air-conditioned centres in Mukherjee Nagar, Karol Bagh, and major metro cities",
            "Dedicated 1-on-1 personal mentorship cabins for copy evaluation and answer writing feedback",
            "Smart digital studios with live streaming and archived video recordings",
            "Comprehensive monthly current affairs magazine ('Vision IAS Monthly') trusted by 90%+ UPSC toppers",
            "Silent library and study pod facilities open till 11 PM"
        ],
        "sports_highlights": [
            "Meditation and mental wellness stress-relief seminars"
        ],
        "cultural_highlights": [
            "Toppers' Talk series and bureaucrat interaction roundtables"
        ],
        "placements": {
            "highest_package": "Over 600 selections in UPSC Civil Services annually (including AIR 1, 2, 3 multiple times)",
            "average_package": "75%+ of final selected IAS/IPS/IFS officers enrolled in Vision IAS Test Series or Mentorship",
            "median_package": "Highest success rate in UPSC Mains answer evaluation nationwide",
            "placement_rate": "86%",
            "top_recruiters": ["Indian Administrative Service (IAS)", "Indian Police Service (IPS)", "Indian Foreign Service (IFS)", "IRS & Central Services"]
        },
        "admissions": {
            "process": "Online or offline registration for foundation batches; direct enrollment for test series.",
            "application_period": "Batches commence monthly throughout the year",
            "entrance_exams": ["Vision IAS Abhyas Diagnostic Assessment"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.visionias.in"
        },
        "reviews": [
            {
                "author": "Dr. Ishita Kishore",
                "role": "UPSC All India Rank 1",
                "rating": 5,
                "date": "2026-01-18",
                "title": "The Mains test series and evaluation feedback made the ultimate difference",
                "comment": "The detailed rubric and personal mentorship helped me refine my answer presentation, introduction hooks, and data citations under tight time pressure.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["UPSC Annual Final Selection Gazette", "Audited Results Affidavits", "StudyFinder Test-Prep Panel"],
            "last_audited": "2026-06-10",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "nalsar-hyderabad",
        "name": "NALSAR University of Law",
        "tagline": "Where Law Meets Justice, Equality & Contemporary Legal Thought",
        "type": "Law",
        "category_label": "Law Colleges",
        "established_year": 1998,
        "ownership": "State Statutory University",
        "affiliation": "Autonomous (Bar Council of India Approved)",
        "accreditations": ["NIRF #3 Law in India", "NAAC 'A++' Grade", "Bar Council of India Recognized"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Platinum Verified",
        "verification_details": {
            "verified_by": "StudyFinder Central Audit Panel",
            "verification_date": "2026-07-04",
            "documents_checked": ["NALSAR University Act 1998", "NAAC A++ Accreditation", "BCI Affiliation Registry"],
            "official_id": "INST-BCI-NALSAR-1998",
            "audit_rating": "4.9 / 5.0"
        },
        "location": {
            "address": "Justice City, Shameerpet",
            "city": "Hyderabad",
            "district": "Medchal-Malkajgiri",
            "state": "Telangana",
            "zone": "South India",
            "pincode": "500101",
            "coordinates": {"lat": 17.6083, "lng": 78.5714}
        },
        "contact": {
            "phone": "+91 40 2349 8105",
            "helpline": "1800-40-NALSAR",
            "email": "admissions@nalsar.ac.in",
            "website": "https://www.nalsar.ac.in",
            "brochure_name": "NALSAR_Hyderabad_Admissions_2026.pdf"
        },
        "fees": {
            "min_annual": 310000,
            "max_annual": 390000,
            "average_annual": 345000,
            "currency": "INR",
            "fee_display": "₹3.1L - ₹3.9L / year",
            "hostel_annual": 70000,
            "scholarships": [
                "NALSAR Merit-cum-Means Financial Assistance (Up to 100% Tuition Waiver)",
                "Telangana State Post-Matric Scholarships",
                "Tata Trust Legal Fellowships"
            ],
            "fee_breakdown": [
                {"course": "B.A., LL.B. (Hons.) 5-Year", "tuition": 265000, "hostel": 70000, "other": 25000, "duration": "5 Years"},
                {"course": "LL.M. (Master of Laws)", "tuition": 210000, "hostel": 70000, "other": 20000, "duration": "1 Year"},
                {"course": "MBA in Corporate Law & Business", "tuition": 280000, "hostel": 70000, "other": 25000, "duration": "2 Years"}
            ]
        },
        "ratings": {
            "overall": 4.9,
            "total_reviews": 380,
            "academic": 4.9,
            "teaching": 4.9,
            "sports": 4.5,
            "cultural": 4.8,
            "infrastructure": 4.9,
            "placement": 4.9,
            "value_for_money": 4.7
        },
        "category_scores": {
            "overall_performance": 97.8,
            "teaching_quality": 98.0,
            "academic_achievement": 98.6,
            "sports_games": 88.0,
            "cultural_festivals": 94.0,
            "performing_arts": 88.0,
            "innovation_research": 96.0,
            "leadership_development": 98.5,
            "infrastructure_facilities": 97.5,
            "special_achievements": 98.0,
            "student_satisfaction": 96.0,
            "community_service": 95.0
        },
        "ranks": {
            "national_overall": 2,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 2,
            "sports_rank": 15,
            "teaching_rank": 2,
            "cultural_rank": 4,
            "innovation_rank": 7
        },
        "courses_offered": [
            {"name": "B.A., LL.B. (Hons.)", "degree": "Undergraduate", "duration": "5 Years", "seats": 132, "eligibility": "CLAT Top 150 All India Rank", "fees": "₹3.60L / yr"},
            {"name": "LL.M. in International Trade / IPR", "degree": "Postgraduate", "duration": "1 Year", "seats": 66, "eligibility": "CLAT PG Merit", "fees": "₹3.00L / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 75,
            "student_faculty_ratio": "1:10",
            "phd_percentage": "92%",
            "notable_faculty": [
                "Prof. Srikrishna Deva Rao (Vice-Chancellor & Renowned Criminologist)",
                "Prof. Faizan Mustafa (Eminent Constitutional Jurist & Former VC)"
            ]
        },
        "facilities": [
            "55-acre serene lakeside residential campus in Shameerpet",
            "M.K. Nambyar SAARCLAW Centre and Supreme Court Replica Moot Court Hall",
            "Centrally air-conditioned library with LexisNexis, Westlaw, Manupatra, and HeinOnline",
            "Full sports complex: tennis courts, football pitch, cricket ground, basketball, and gym",
            "100% residential campus with high-speed Wi-Fi, cafes, and healthcare center"
        ],
        "sports_highlights": [
            "Inter-Ghats Sports Meet Champions",
            "Active football, basketball, and athletics leagues"
        ],
        "cultural_highlights": [
            "NALSAR Inter-Varsity Parliamentary Debate (India's premier debating competition)",
            "Carpe Diem - Annual cultural festival with celebrity performances"
        ],
        "placements": {
            "highest_package": "₹22 LPA (Tier-1 Indian Firms) / £58,000 (UK Magic Circle)",
            "average_package": "₹16.8 LPA",
            "median_package": "₹15.5 LPA",
            "placement_rate": "98%",
            "top_recruiters": ["Cyril Amarchand Mangaldas", "Khaitan & Co", "Shardul Amarchand Mangaldas", "Trilegal", "Clifford Chance", "Herbert Smith Freehills"]
        },
        "admissions": {
            "process": "CLAT (Common Law Admission Test) through Consortium of NLUs.",
            "application_period": "July - December 2026",
            "entrance_exams": ["CLAT"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.nalsar.ac.in"
        },
        "reviews": [
            {
                "author": "Ananya Reddy",
                "role": "B.A., LL.B. Alumna, Khaitan & Co",
                "rating": 5,
                "date": "2026-02-09",
                "title": "A serene lakeside campus that fosters deep intellectual debate",
                "comment": "NALSAR has a unique culture where students are treated as equal colleagues by professors. The constitutional law discussions by the lake are unforgettable.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["NIRF Law 2025 #3", "Bar Council of India Audit", "NAAC A++ Certificate"],
            "last_audited": "2026-07-01",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "cathedral-school-mumbai",
        "name": "The Cathedral & John Connon School",
        "tagline": "Clarum Efficiunt Studia — Studies Make Men Famous (Since 1860)",
        "type": "School",
        "category_label": "Schools & Junior Colleges",
        "established_year": 1860,
        "ownership": "Private Heritage Day School",
        "affiliation": "CISCE (ICSE / ISC) & International Baccalaureate (IBDP)",
        "accreditations": ["EducationWorld #1 All-India Day School", "IB World School", "CISCE Affiliated"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Gold Verified",
        "verification_details": {
            "verified_by": "StudyFinder K-12 Audit Board",
            "verification_date": "2026-05-18",
            "documents_checked": ["CISCE Board Affiliation", "IBDP Accreditation Certificate", "Heritage Safety Audit"],
            "official_id": "INST-SCH-CATH-1860",
            "audit_rating": "5.0 / 5.0"
        },
        "location": {
            "address": "6, Purshottamdas Thakurdas Marg, Fort",
            "city": "Mumbai",
            "district": "Mumbai City",
            "state": "Maharashtra",
            "zone": "Western India",
            "pincode": "400001",
            "coordinates": {"lat": 18.9348, "lng": 72.8335}
        },
        "contact": {
            "phone": "+91 22 4322 1400",
            "helpline": "+91 22 2200 1282",
            "email": "principal@cathedral-school.com",
            "website": "https://cathedral-school.com",
            "brochure_name": "Cathedral_School_Prospectus_2026.pdf"
        },
        "fees": {
            "min_annual": 240000,
            "max_annual": 780000,
            "average_annual": 460000,
            "currency": "INR",
            "fee_display": "₹2.4L (ICSE) - ₹7.8L (IBDP) / year",
            "hostel_annual": 0,
            "scholarships": [
                "The Cathedral Alumni Trust Need-Based Merit Bursaries",
                "Anglo-Scottish Education Society Scholarships"
            ],
            "fee_breakdown": [
                {"course": "Primary & Middle School (Class 1-8)", "tuition": 240000, "hostel": 0, "other": 35000, "duration": "Annual"},
                {"course": "ICSE Class 9 & 10", "tuition": 280000, "hostel": 0, "other": 40000, "duration": "Annual"},
                {"course": "IB Diploma Programme (Class 11 & 12)", "tuition": 780000, "hostel": 0, "other": 65000, "duration": "Annual"}
            ]
        },
        "ratings": {
            "overall": 4.92,
            "total_reviews": 430,
            "academic": 5.0,
            "teaching": 4.9,
            "sports": 4.7,
            "cultural": 5.0,
            "infrastructure": 4.9,
            "placement": 5.0,
            "value_for_money": 4.7
        },
        "category_scores": {
            "overall_performance": 98.0,
            "teaching_quality": 98.5,
            "academic_achievement": 99.2,
            "sports_games": 92.0,
            "cultural_festivals": 99.0,
            "performing_arts": 98.0,
            "innovation_research": 93.0,
            "leadership_development": 99.5,
            "infrastructure_facilities": 97.0,
            "special_achievements": 99.0,
            "student_satisfaction": 97.0,
            "community_service": 96.0
        },
        "ranks": {
            "national_overall": 2,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 2,
            "sports_rank": 8,
            "teaching_rank": 1,
            "cultural_rank": 1,
            "innovation_rank": 9
        },
        "courses_offered": [
            {"name": "ICSE (Class 9 & 10)", "degree": "Secondary Education", "duration": "2 Years", "seats": 160, "eligibility": "Internal Continuation / Entrance", "fees": "₹2.80L / yr"},
            {"name": "IB Diploma Programme (IBDP Class 11-12)", "degree": "Senior Secondary", "duration": "2 Years", "seats": 85, "eligibility": "10th Board Exam / Aptitude Test", "fees": "₹7.80L / yr"},
            {"name": "ISC Science & Commerce (Class 11-12)", "degree": "Senior Secondary", "duration": "2 Years", "seats": 80, "eligibility": "ICSE Merit", "fees": "₹3.20L / yr"}
        ],
        "faculty_summary": {
            "total_faculty": 160,
            "student_faculty_ratio": "1:10",
            "phd_percentage": "30% Master's & International IB Examiner Certified",
            "notable_faculty": [
                "Dr. S. Mukherjee (Principal & Renowned Educationist)",
                "Distinguished Deans of English Literature and Sciences"
            ]
        },
        "facilities": [
            "Neo-Gothic Victorian stone heritage campus in the heart of South Mumbai's Fort district",
            "Cutting-edge MakerSpace & Robotics Labs with 3D scanners and laser fabricators",
            "Cathedral High School Library with 40,000 volumes and global EBSCO research access",
            "Gymnasium, all-weather synthetic basketball courts, and Azad Maidan cricket facilities",
            "Acoustic music rooms, choir auditoriums, and drama studios"
        ],
        "sports_highlights": [
            "MSSA (Mumbai Schools Sports Association) champions in Football, Rugby, and Swimming",
            "Active rowing and sailing clubs tied up with the Royal Bombay Yacht Club"
        ],
        "cultural_highlights": [
            "Cathedral Model United Nations (CMUN) - India's oldest and most prestigious school MUN",
            "Annual Founder's Day Concert at the NCPA (National Centre for the Performing Arts)",
            "The Malhar & Inter-House Music Festival"
        ],
        "placements": {
            "highest_package": "Over 70% of graduating IBDP cohort admitted into Ivy League, Oxford, Cambridge, and Stanford",
            "average_package": "100% University Placement in Top Tier Global & Indian Universities",
            "median_package": "Highest average IB score in India (38.5 points out of 45)",
            "placement_rate": "100%",
            "top_recruiters": ["Harvard", "Stanford", "Yale", "Oxford", "Cambridge", "Columbia", "UPenn", "Ashoka University"]
        },
        "admissions": {
            "process": "Online application, points system for junior school, and competitive admission test for Class 11 IBDP.",
            "application_period": "October - January 2026",
            "entrance_exams": ["Cathedral IBDP Aptitude Test"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.cathedral-school.com"
        },
        "reviews": [
            {
                "author": "Ratan Tata (Late)",
                "role": "Distinguished Alumnus",
                "rating": 5,
                "date": "2025-10-10",
                "title": "A school that instilled values of integrity, service and excellence",
                "comment": "The foundations of discipline and values built at Cathedral remain with you for a lifetime.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["EducationWorld All-India Day School #1", "CISCE Council Audit", "IB World Organization"],
            "last_audited": "2026-05-15",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    },
    {
        "id": "your-space-bengaluru",
        "name": "Your-Space Premier Student Residence (Koramangala)",
        "tagline": "Comfort, Community & Academic Productivity Redefined",
        "type": "Student Hostel",
        "category_label": "Hostels & Accommodations",
        "established_year": 2020,
        "ownership": "Managed Private Student Housing",
        "affiliation": "StudyFinder Verified Student Housing Partner",
        "accreditations": ["FSSAI 5-Star Kitchen", "Safety & Fire Compliance Certified", "StudyFinder Verified Co-Living"],
        "verification_status": "verified",
        "verification_badge": "StudyFinder Verified",
        "verification_details": {
            "verified_by": "StudyFinder Housing Inspection Panel",
            "verification_date": "2026-07-10",
            "documents_checked": ["FSSAI Food Certification", "Biometric Access Audit", "Student Tenancy Code Agreement"],
            "official_id": "INST-HST-YSPC-2020",
            "audit_rating": "4.8 / 5.0"
        },
        "location": {
            "address": "4th Block, Near Sony World Signal, Koramangala",
            "city": "Bengaluru",
            "district": "Bengaluru Urban",
            "state": "Karnataka",
            "zone": "South India",
            "pincode": "560034",
            "coordinates": {"lat": 12.9352, "lng": 77.6245}
        },
        "contact": {
            "phone": "+91 80 4567 8900",
            "helpline": "+91 800-YOUR-SPACE",
            "email": "info@your-space.in",
            "website": "https://www.your-space.in",
            "brochure_name": "Your_Space_Koramangala_Brochure_2026.pdf"
        },
        "fees": {
            "min_annual": 180000,
            "max_annual": 288000,
            "average_annual": 228000,
            "currency": "INR",
            "fee_display": "₹15,000 - ₹24,000 / month (Meals Included)",
            "hostel_annual": 228000,
            "scholarships": [
                "Full Academic Year Advance Payment 10% Discount",
                "Sibling and Referral Cashbacks"
            ],
            "fee_breakdown": [
                {"course": "Double Sharing with Attached Bathroom & AC", "tuition": 0, "hostel": 216000, "other": 10000, "duration": "Annual (₹18,000/mo)"},
                {"course": "Single Private Suite with Study Corner & Balcony", "tuition": 0, "hostel": 288000, "other": 10000, "duration": "Annual (₹24,000/mo)"},
                {"course": "Triple Sharing Economy Room", "tuition": 0, "hostel": 180000, "other": 10000, "duration": "Annual (₹15,000/mo)"}
            ]
        },
        "ratings": {
            "overall": 4.81,
            "total_reviews": 340,
            "academic": 4.4,
            "teaching": 4.0,
            "sports": 4.3,
            "cultural": 4.5,
            "infrastructure": 4.9,
            "placement": 4.0,
            "value_for_money": 4.8
        },
        "category_scores": {
            "overall_performance": 93.5,
            "teaching_quality": 80.0,
            "academic_achievement": 83.0,
            "sports_games": 82.0,
            "cultural_festivals": 85.0,
            "performing_arts": 76.0,
            "innovation_research": 84.0,
            "leadership_development": 87.0,
            "infrastructure_facilities": 98.2,
            "special_achievements": 90.0,
            "student_satisfaction": 96.5,
            "community_service": 86.0
        },
        "ranks": {
            "national_overall": 2,
            "state_rank": 1,
            "district_rank": 1,
            "category_rank": 2,
            "sports_rank": 29,
            "teaching_rank": 32,
            "cultural_rank": 16,
            "innovation_rank": 19
        },
        "courses_offered": [
            {"name": "Premium Student Double Room with Meal Plan", "degree": "Hostel Stay", "duration": "Academic Year", "seats": 80, "eligibility": "College / University Student", "fees": "₹18,000 / mo"},
            {"name": "Private Single Room Suite", "degree": "Hostel Stay", "duration": "Academic Year", "seats": 30, "eligibility": "College / University Student", "fees": "₹24,000 / mo"}
        ],
        "faculty_summary": {
            "total_faculty": 20,
            "student_faculty_ratio": "1:8 (Resident Managers & Wardens)",
            "phd_percentage": "Certified Hospitality & Security Personnel",
            "notable_faculty": [
                "24/7 Security Officers & Resident Female Warden",
                "Executive Nutrition Chef"
            ]
        },
        "facilities": [
            "Proximity (10 mins) to St. John's Medical College, Christ University, and startup offices",
            "4 times daily chef-prepared home-style nutritious buffet meals",
            "Dedicated sound-damped study lounge with ergonomic chairs and high-speed Wi-Fi 6",
            "Biometric smart-lock door entries, 360-degree CCTV security, and parent notification app",
            "Fully air-conditioned rooms with daily housekeeping and free weekly laundry service",
            "Rooftop turf lounge with barbecue grill, table tennis, and gym equipment"
        ],
        "sports_highlights": [
            "Rooftop fitness zone, indoor table tennis, and yoga mats"
        ],
        "cultural_highlights": [
            "Monthly community open-mic nights, board game tournaments, and movie screenings"
        ],
        "placements": {
            "highest_package": "N/A (Student Accommodation - 100% verified student occupants)",
            "average_package": "Proximity to Top Colleges & Tech Hubs",
            "median_package": "100% Verified Peaceful Study Environment",
            "placement_rate": "100%",
            "top_recruiters": ["Christ University Students", "St. John's Medical Students", "Interns at Bengaluru Startups"]
        },
        "admissions": {
            "process": "Online portal room reservation, college verification, digital agreement.",
            "application_period": "Rolling Admissions for Semesters",
            "entrance_exams": ["Student ID / Admission Offer Letter"],
            "scholarships_available": True
        },
        "images": {
            "hero": "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=1200&q=80",
            "gallery": [
                "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=800&q=80"
            ],
            "virtual_tour_url": "https://tour.your-space.in"
        },
        "reviews": [
            {
                "author": "Pooja Hegde",
                "role": "Christ University Student (Resident)",
                "rating": 5,
                "date": "2026-03-01",
                "title": "Study lounge and peaceful environment helped me top my semester",
                "comment": "The food is genuinely like home, the rooms are spotless, and having quiet study pods with reliable fast internet made my exam prep stress-free.",
                "verified_student": True
            }
        ],
        "ranking_evidence": {
            "sources": ["StudyFinder Physical Audit 2026", "FSSAI Safety Rating", "Bengaluru Police Tenant Verification"],
            "last_audited": "2026-07-08",
            "auditor": "StudyFinder Independent Verification Council",
            "confidence_level": "High"
        }
    }
]

with open("data/institutions.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

# Merge avoiding duplicates
existing_ids = {x["id"] for x in existing}
for inst in more_institutions:
    if inst["id"] not in existing_ids:
        existing.append(inst)

with open("data/institutions.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Total institutions updated: {len(existing)}")
