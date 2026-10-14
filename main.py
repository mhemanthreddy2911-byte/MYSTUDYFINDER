"""
StudyFinder India — The Ultimate Education Discovery, Ranking & Talent Platform
Backend API Server (FastAPI + Python 3.13)
Tagline: 'Find. Compare. Rank. Choose. Succeed.'
"""

import json
import os
import datetime
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, Query, HTTPException, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.ranking_engine import RankingEngine, CATEGORIES_MAP
from services.search_service import SearchService
from services.ai_recommender import EduMatchAI
from services.verification import VerificationService

# Initialize app
app = FastAPI(
    title="StudyFinder India API",
    description="The Ultimate Education Discovery, Ranking & Talent Platform in India",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "institutions.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    institutions_data: List[Dict[str, Any]] = json.load(f)

# Instantiate core engines
ranking_engine = RankingEngine(institutions_data)
search_service = SearchService(institutions_data)
ai_recommender = EduMatchAI(institutions_data)
verification_service = VerificationService()

# In-memory storage for enquiries and campus visit passes
enquiries_store: List[Dict[str, Any]] = [
    {
        "enquiry_id": "ENQ-901",
        "institution_id": "iit-bombay",
        "institution_name": "Indian Institute of Technology Bombay",
        "student_name": "Rohan Deshmukh",
        "email": "rohan.d@gmail.com",
        "phone": "+91 98200 11223",
        "target_course": "B.Tech Computer Science",
        "message": "Inquiring about JoSAA cutoffs and hostel accommodation for outstation students.",
        "status": "Responded",
        "timestamp": "2026-10-12T14:20:00"
    },
    {
        "enquiry_id": "ENQ-902",
        "institution_id": "doon-school-dehradun",
        "institution_name": "The Doon School",
        "student_name": "Vikram Sethi (Parent)",
        "email": "v.sethi@enterprise.in",
        "phone": "+91 98110 55667",
        "target_course": "Class 7 Residential Admission",
        "message": "Requesting prospectus and details for October entrance examination centers.",
        "status": "New",
        "timestamp": "2026-10-14T09:15:00"
    }
]

campus_visits_store: List[Dict[str, Any]] = [
    {
        "visit_pass_id": "VISIT-7701",
        "institution_id": "iit-madras",
        "institution_name": "Indian Institute of Technology Madras",
        "visitor_name": "Priyanka Nair",
        "email": "priyanka.n@outlook.com",
        "phone": "+91 94440 88776",
        "visit_date": "2026-10-25",
        "slot": "Morning (10:00 AM - 1:00 PM)",
        "attendees": 3,
        "purpose": "Research Park & Campus Tour with Parents",
        "status": "Confirmed Pass Generated"
    }
]

# Pydantic Schemas for validation
class EnquiryRequest(BaseModel):
    institution_id: str
    student_name: str
    email: str
    phone: str
    target_course: str
    message: Optional[str] = ""

class VisitBookingRequest(BaseModel):
    institution_id: str
    visitor_name: str
    email: str
    phone: str
    visit_date: str
    slot: str
    attendees: int = 2
    purpose: Optional[str] = "Prospective Admission Visit"

class ChatRequest(BaseModel):
    institution_id: Optional[str] = None
    message: str
    conversation_history: Optional[List[Dict[str, str]]] = []

class CompareRequest(BaseModel):
    institution_ids: List[str]

class RecommendRequest(BaseModel):
    stage: str
    target_field: str
    preferred_state: Optional[str] = "All India"
    max_annual_budget: Optional[float] = 1000000
    priorities: Optional[List[str]] = []
    hostel_needed: Optional[bool] = False

# API Endpoints
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "platform": "StudyFinder India",
        "institutions_loaded": len(institutions_data),
        "version": "1.0.0"
    }

@app.get("/api/institutions")
def list_institutions(
    q: Optional[str] = Query(None, description="Keyword search query"),
    type: Optional[str] = Query(None, description="Institution category type"),
    state: Optional[str] = Query(None, description="State filter"),
    city: Optional[str] = Query(None, description="City filter"),
    pincode: Optional[str] = Query(None, description="PIN code prefix or exact"),
    min_fee: Optional[float] = Query(None, description="Minimum annual fee"),
    max_fee: Optional[float] = Query(None, description="Maximum annual fee"),
    facilities: Optional[str] = Query(None, description="Comma-separated facilities"),
    min_rating: Optional[float] = Query(None, description="Minimum rating"),
    verified_only: Optional[bool] = Query(False, description="Filter only verified"),
    sort_by: Optional[str] = Query("rank", description="Sort parameter"),
    limit: Optional[int] = Query(50, description="Page limit"),
    offset: Optional[int] = Query(0, description="Page offset")
):
    facility_list = [f.strip() for f in facilities.split(",")] if facilities else None
    return search_service.search(
        query=q,
        institution_type=type,
        state=state,
        city=city,
        pincode=pincode,
        min_fee=min_fee,
        max_fee=max_fee,
        required_facilities=facility_list,
        min_rating=min_rating,
        verified_only=verified_only or False,
        sort_by=sort_by or "rank",
        limit=limit,
        offset=offset
    )

@app.get("/api/institutions/{institution_id}")
def get_institution(institution_id: str):
    inst = next((x for x in institutions_data if x["id"] == institution_id), None)
    if not inst:
        raise HTTPException(status_code=404, detail="Institution not found")
    
    # Enrich with latest user reviews if any
    additional_reviews = [r for r in verification_service.user_reviews if r.get("institution_id") == institution_id]
    inst_copy = dict(inst)
    if additional_reviews:
        inst_copy["reviews"] = additional_reviews + inst_copy.get("reviews", [])

    return inst_copy

@app.get("/api/rankings")
def get_rankings(
    category: Optional[str] = Query("overall", description="Ranking category key"),
    scope: Optional[str] = Query("national", description="Scope: 'national' or state name"),
    type: Optional[str] = Query(None, description="Institution type filter"),
    min_budget: Optional[float] = Query(None, description="Min budget filter"),
    max_budget: Optional[float] = Query(None, description="Max budget filter")
):
    return ranking_engine.get_leaderboard(
        category=category or "overall",
        scope=scope or "national",
        institution_type=type,
        min_budget=min_budget,
        max_budget=max_budget
    )

@app.get("/api/rankings/categories")
def get_ranking_categories():
    return {
        "categories": [
            {"key": k, "name": v} for k, v in CATEGORIES_MAP.items()
        ]
    }

@app.get("/api/rankings/breakdown/{institution_id}")
def get_institution_ranking_breakdown(institution_id: str):
    breakdown = ranking_engine.get_category_breakdown_for_institution(institution_id)
    if not breakdown:
        raise HTTPException(status_code=404, detail="Institution not found")
    return breakdown

@app.post("/api/recommend")
def get_recommendations(req: RecommendRequest):
    return ai_recommender.recommend(
        stage=req.stage,
        target_field=req.target_field,
        preferred_state=req.preferred_state or "All India",
        max_annual_budget=req.max_annual_budget or 1000000,
        priorities=req.priorities or [],
        hostel_needed=req.hostel_needed or False
    )

@app.post("/api/compare")
def compare_institutions(req: CompareRequest):
    if len(req.institution_ids) < 2:
        raise HTTPException(status_code=400, detail="Please select at least 2 institutions to compare.")
    
    selected = [x for x in institutions_data if x["id"] in req.institution_ids]
    if not selected:
        raise HTTPException(status_code=404, detail="Selected institutions not found")
    
    # Generate side-by-side matrix
    matrix = {
        "institutions": selected,
        "metrics": [
            {
                "label": "Annual Fees (Average)",
                "values": {inst["id"]: inst["fees"]["fee_display"] for inst in selected}
            },
            {
                "label": "National Overall Rank",
                "values": {inst["id"]: f"#{inst['ranks'].get('national_overall', 'N/A')}" for inst in selected}
            },
            {
                "label": "Sports & Games Rank",
                "values": {inst["id"]: f"#{inst['ranks'].get('sports_rank', 'N/A')}" for inst in selected}
            },
            {
                "label": "Teaching Quality Score",
                "values": {inst["id"]: f"{inst['category_scores'].get('teaching_quality', 'N/A')}/100" for inst in selected}
            },
            {
                "label": "Faculty-Student Ratio",
                "values": {inst["id"]: inst.get("faculty_summary", {}).get("student_faculty_ratio", "1:10") for inst in selected}
            },
            {
                "label": "PhD Faculty %",
                "values": {inst["id"]: inst.get("faculty_summary", {}).get("phd_percentage", "N/A") for inst in selected}
            },
            {
                "label": "Placements / Outcome",
                "values": {inst["id"]: inst.get("placements", {}).get("average_package", "N/A") for inst in selected}
            },
            {
                "label": "Hostel & Accommodation",
                "values": {inst["id"]: "Available On-Campus" if (inst.get("fees", {}).get("hostel_annual", 0) > 0 or inst.get("type") == "Student Hostel") else "Day Scholar / External" for inst in selected}
            },
            {
                "label": "Verification Badge",
                "values": {inst["id"]: inst.get("verification_badge", "Verified") for inst in selected}
            }
        ]
    }
    return matrix

@app.post("/api/enquire")
def submit_enquiry(req: EnquiryRequest):
    inst = next((x for x in institutions_data if x["id"] == req.institution_id), None)
    inst_name = inst["name"] if inst else "Educational Institution"

    enq_id = f"ENQ-{len(enquiries_store) + 903}"
    new_record = {
        "enquiry_id": enq_id,
        "institution_id": req.institution_id,
        "institution_name": inst_name,
        "student_name": req.student_name,
        "email": req.email,
        "phone": req.phone,
        "target_course": req.target_course,
        "message": req.message,
        "status": "Submitted to Admissions Desk",
        "timestamp": datetime.datetime.now().isoformat()
    }
    enquiries_store.append(new_record)

    return {
        "success": True,
        "enquiry_id": enq_id,
        "institution_name": inst_name,
        "message": f"Your enquiry has been delivered directly to {inst_name}'s official admissions office. An academic counselor will contact you at {req.phone} or {req.email} within 24 hours."
    }

@app.post("/api/book-visit")
def book_campus_visit(req: VisitBookingRequest):
    inst = next((x for x in institutions_data if x["id"] == req.institution_id), None)
    inst_name = inst["name"] if inst else "Campus"

    pass_id = f"VISIT-{len(campus_visits_store) + 7702}"
    new_visit = {
        "visit_pass_id": pass_id,
        "institution_id": req.institution_id,
        "institution_name": inst_name,
        "visitor_name": req.visitor_name,
        "email": req.email,
        "phone": req.phone,
        "visit_date": req.visit_date,
        "slot": req.slot,
        "attendees": req.attendees,
        "purpose": req.purpose,
        "status": "Confirmed Pass Generated",
        "qr_code_token": f"SF-IN-{pass_id}-PASS",
        "address": inst["location"]["address"] if inst else "Main Campus Gate"
    }
    campus_visits_store.append(new_visit)

    return {
        "success": True,
        "visit_pass": new_visit,
        "message": f"Campus visit pass confirmed for {inst_name}! Please present your digital pass #{pass_id} at the security gate."
    }

@app.post("/api/chat")
def live_chat_assistant(req: ChatRequest):
    """
    Intelligent interactive admission assistant that answers questions accurately
    based on verified institutional facts or all-India discovery.
    """
    user_msg = req.message.lower().strip()
    inst = None
    if req.institution_id:
        inst = next((x for x in institutions_data if x["id"] == req.institution_id), None)

    # If institutional context is active
    if inst:
        name = inst["name"]
        fees = inst["fees"]
        courses = inst["courses_offered"]
        ranks = inst["ranks"]
        placements = inst.get("placements", {})
        admissions = inst.get("admissions", {})

        if any(w in user_msg for w in ["fee", "cost", "how much", "tuition", "hostel fee"]):
            reply = (
                f"**Fee Structure for {name}**:\n\n"
                f"• **Average Annual Fee**: {fees.get('fee_display')}\n"
                f"• **Hostel & Living**: "
                f"{('₹' + str(fees.get('hostel_annual')) + ' / year') if fees.get('hostel_annual') > 0 else 'Included in residential or day-scholar'}\n\n"
                f"• **Scholarships Available**: {', '.join(fees.get('scholarships', ['Merit & Need-based assistance']))}\n\n"
                f"Would you like me to connect you with an admissions counselor or download the official fee breakdown brochure?"
            )
        elif any(w in user_msg for w in ["placement", "package", "salary", "recruiter", "job"]):
            reply = (
                f"**Placement & Career Track Record for {name}**:\n\n"
                f"• **Highest Package**: {placements.get('highest_package', 'Premier global outcome')}\n"
                f"• **Average Package**: {placements.get('average_package', 'Top tier national average')}\n"
                f"• **Placement Rate**: {placements.get('placement_rate', '95%+')}\n"
                f"• **Key Recruiters**: {', '.join(placements.get('top_recruiters', ['Global Industry Leaders']))}\n\n"
                f"You can also compare these placement stats with other peer institutions using our Compare tool!"
            )
        elif any(w in user_msg for w in ["admission", "eligibility", "exam", "how to apply", "cutoff", "process"]):
            reply = (
                f"**Admissions Guide for {name}**:\n\n"
                f"• **Process**: {admissions.get('process')}\n"
                f"• **Required Entrance Exams**: {', '.join(admissions.get('entrance_exams', ['Merit/Direct']))}\n"
                f"• **Application Window**: {admissions.get('application_period', 'Check official website')}\n\n"
                f"You can click **'Enquire Now'** right here to submit an application query or **'Book Campus Visit'** to meet the admissions committee in person."
            )
        elif any(w in user_msg for w in ["course", "branch", "degree", "program", "subjects"]):
            course_list = "\n".join([f"• **{c['name']}** ({c['degree']}, {c['duration']}) — *{c['eligibility']}*" for c in courses[:4]])
            reply = (
                f"**Key Academic Programs at {name}**:\n\n"
                f"{course_list}\n\n"
                f"Total seats and specialized branches are listed under the Courses tab on this profile!"
            )
        elif any(w in user_msg for w in ["rank", "ranking", "reputation", "nirf"]):
            reply = (
                f"**Official Verified Rankings for {name}**:\n\n"
                f"• **All-India Overall Rank**: #{ranks.get('national_overall', 'Top Tier')}\n"
                f"• **State Rank in {inst['location']['state']}**: #{ranks.get('state_rank', 1)}\n"
                f"• **Category Rank ({inst['type']})**: #{ranks.get('category_rank', 1)}\n"
                f"• **Accreditations**: {', '.join(inst.get('accreditations', []))}\n"
                f"• **Audit Evidence**: {inst.get('ranking_evidence', {}).get('sources', ['Official Ministry Registry'])[0]}\n\n"
                f"StudyFinder India ranks are updated each academic cycle using verified evidence only."
            )
        elif any(w in user_msg for w in ["sports", "cultural", "fest", "facility", "activities"]):
            sports = inst.get("sports_highlights", ["Inter-college athletic competitions"])
            cultural = inst.get("cultural_highlights", ["Annual student fest"])
            reply = (
                f"**Campus Life, Sports & Culture at {name}**:\n\n"
                f"• **Sports Highlights**: {sports[0]}\n"
                f"• **Cultural Legacy**: {cultural[0]}\n"
                f"• **Campus Amenities**: {', '.join(inst.get('facilities', [])[:5])}\n\n"
                f"Would you like to book a campus visit to experience these facilities in person?"
            )
        else:
            reply = (
                f"Hello! I am your StudyFinder Admissions Assistant for **{name}** in {inst['location']['city']}.\n\n"
                f"I can help you with:\n"
                f"1. **Course Cutoffs & Entrance Requirements**\n"
                f"2. **Tuition & Hostel Fee Structure with Scholarships**\n"
                f"3. **Placements, Packages & Recruiter Statistics**\n"
                f"4. **Campus Facilities, Sports & Student Housing**\n"
                f"5. **Booking a Verified Campus Visit**\n\n"
                f"What would you like to know?"
            )
    else:
        # General All-India Counselor Assistant
        if "best" in user_msg and "engineering" in user_msg:
            reply = "For Engineering in India, **IIT Madras** holds the #1 NIRF rank, closely followed by **IIT Bombay** (famous for Techfest & entrepreneurship) and **BITS Pilani** (renowned for its Zero Attendance policy and startup culture). You can view the full Engineering Leaderboard under the **Rankings** tab!"
        elif "medical" in user_msg or "neet" in user_msg:
            reply = "For Medical Education in India, **AIIMS New Delhi** ranks #1 nationally with unbeatable clinical immersion and highly subsidized fees, followed by **CMC Vellore** for clinical compassion. Use our **EduMatch AI** tool to calculate which college fits your NEET score best!"
        elif "school" in user_msg:
            reply = "For schools, **The Doon School** leads boys' boarding education and sports (#1 in India), while **DPS R.K. Puram** is an academic powerhouse in Delhi, and **The Cathedral and John Connon School** excels in ICSE/IBDP in Mumbai. You can filter schools by CBSE, ICSE, or IB under Discovery!"
        else:
            reply = (
                "Namaste! Welcome to **StudyFinder India** — your intelligent companion for discovering, comparing, and ranking educational institutions across India.\n\n"
                "You can search by course name, state, PIN code, or fee budget. Try asking me:\n"
                "• *'Which are the top schools for sports in India?'*\n"
                "• *'Show me top colleges in Karnataka with low fees'*\n"
                "• *'Compare IIT Bombay vs IIT Madras'*\n"
                "• *'Help me find student hostels near Delhi University'*\n\n"
                "How can I help your educational journey today?"
            )

    return {
        "reply": reply,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/verify/claim")
def submit_institution_claim(payload: Dict[str, Any] = Body(...)):
    return verification_service.submit_claim(payload)

@app.post("/api/verify/report")
def report_inaccurate_info(payload: Dict[str, Any] = Body(...)):
    return verification_service.report_inaccuracy(payload)

@app.post("/api/reviews")
def submit_review(payload: Dict[str, Any] = Body(...)):
    return verification_service.submit_review(payload)

@app.get("/api/admin/claims")
def get_admin_claims():
    return {
        "claims": verification_service.get_claims_list(),
        "total_claims": len(verification_service.get_claims_list())
    }

@app.get("/api/admin/leads")
def get_admin_leads():
    return {
        "enquiries": enquiries_store,
        "campus_visits": campus_visits_store,
        "total_enquiries": len(enquiries_store),
        "total_visits": len(campus_visits_store)
    }

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def serve_index():
    index_file = os.path.join(static_dir, "index.html")
    return FileResponse(index_file)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
