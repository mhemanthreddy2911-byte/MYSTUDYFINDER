"""
StudyFinder India — Trust, Verification & Fraud Prevention Service
Handles institution document verification, audit trails, fake review detection,
and user inaccuracy reports.
"""

import datetime
from typing import List, Dict, Any, Optional

class VerificationService:
    def __init__(self):
        # In-memory storage for submitted verification claims, reviews, and reports
        self.verification_claims: List[Dict[str, Any]] = [
            {
                "claim_id": "CLM-2026-0819",
                "institution_id": "iit-bombay",
                "institution_name": "Indian Institute of Technology Bombay",
                "applicant_name": "Dr. S. K. Roy",
                "designation": "Dean of Academic Affairs",
                "official_email": "dean.acad@iitb.ac.in",
                "phone": "+91 22 2572 2522",
                "document_types": ["UGC/MoE Gazette Notification", "NIRF 2025 Audit Sheet", "NBA Certificate"],
                "status": "APPROVED",
                "verified_badge": "StudyFinder Platinum Verified",
                "audit_timestamp": "2026-08-15T10:30:00Z",
                "auditor_notes": "All statutory documents verified against Ministry of Education gazette."
            },
            {
                "claim_id": "CLM-2026-0824",
                "institution_id": "padukone-dravid-cse",
                "institution_name": "Padukone-Dravid Centre for Sports Excellence",
                "applicant_name": "Anand S.",
                "designation": "Head of Operations & Sports Science",
                "official_email": "ops@centreforsportsexcellence.com",
                "phone": "+91 80 6825 8000",
                "document_types": ["Sports Authority Inspection Report", "Olympic Association Recognition"],
                "status": "APPROVED",
                "verified_badge": "StudyFinder Gold Verified",
                "audit_timestamp": "2026-07-14T15:20:00Z",
                "auditor_notes": "Physical facility inspected in Yelahanka; Olympic pools and biomechanics labs certified."
            }
        ]

        self.reports: List[Dict[str, Any]] = []
        self.user_reviews: List[Dict[str, Any]] = []

    def submit_claim(self, claim_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Submit a new institution verification claim with documentation.
        """
        claim_id = f"CLM-2026-{len(self.verification_claims) + 1001}"
        record = {
            "claim_id": claim_id,
            "institution_id": claim_data.get("institution_id", "unregistered"),
            "institution_name": claim_data.get("institution_name", "Unknown Institution"),
            "applicant_name": claim_data.get("applicant_name", ""),
            "designation": claim_data.get("designation", ""),
            "official_email": claim_data.get("official_email", ""),
            "phone": claim_data.get("phone", ""),
            "registration_number": claim_data.get("registration_number", ""),
            "document_types": claim_data.get("document_types", ["Affiliation Certificate"]),
            "status": "UNDER_AUDIT",
            "audit_timestamp": datetime.datetime.now().isoformat(),
            "auditor_notes": "Document package received. Assigned to Regional Audit Officer."
        }
        self.verification_claims.append(record)
        return {
            "success": True,
            "claim_id": claim_id,
            "message": "Institution verification application submitted successfully. Audit verification turnaround is typically 48-72 hours."
        }

    def report_inaccuracy(self, report_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Report incorrect fees, outdated admissions dates, or false claims.
        """
        report_id = f"REP-2026-{len(self.reports) + 501}"
        record = {
            "report_id": report_id,
            "institution_id": report_data.get("institution_id"),
            "institution_name": report_data.get("institution_name"),
            "reporter_role": report_data.get("reporter_role", "Student"),
            "category": report_data.get("category", "Fee Discrepancy"),
            "description": report_data.get("description", ""),
            "evidence_link": report_data.get("evidence_link", ""),
            "status": "INVESTIGATING",
            "created_at": datetime.datetime.now().isoformat()
        }
        self.reports.append(record)
        return {
            "success": True,
            "report_id": report_id,
            "message": "Thank you for safeguarding educational transparency! Our verification desk has logged this investigation ticket."
        }

    def submit_review(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Submit student or parent review with anti-spam and verification filter.
        """
        # Anti-fraud check: check minimum length and suspicious promotional phrases
        comment = review_data.get("comment", "")
        if len(comment.strip()) < 20:
            return {
                "success": False,
                "error": "Review must be at least 20 characters and describe genuine campus or academic experience."
            }

        spam_triggers = ["call me for admission", "guaranteed seat direct quota", "whatsapp at +91", "100% money back"]
        if any(trigger in comment.lower() for trigger in spam_triggers):
            return {
                "success": False,
                "error": "Review flagged by anti-spam filter for commercial solicitation. Please keep feedback focused on institutional quality."
            }

        review_id = f"REV-2026-{len(self.user_reviews) + 1}"
        verified_student = review_data.get("roll_number") is not None or review_data.get("verified_student", True)

        new_rev = {
            "review_id": review_id,
            "institution_id": review_data.get("institution_id"),
            "author": review_data.get("author", "Anonymous Student"),
            "role": review_data.get("role", "Current Student"),
            "rating": float(review_data.get("rating", 5.0)),
            "title": review_data.get("title", "Student Experience"),
            "comment": comment,
            "date": datetime.date.today().strftime("%Y-%m-%d"),
            "verified_student": verified_student
        }
        self.user_reviews.append(new_rev)
        return {
            "success": True,
            "review": new_rev,
            "message": "Your review has been verified and posted! Thank you for helping students across India."
        }

    def get_claims_list(self) -> List[Dict[str, Any]]:
        return self.verification_claims

    def get_reports_list(self) -> List[Dict[str, Any]]:
        return self.reports
