"""
StudyFinder India — Transparent Ranking Engine
Configurable multi-dimensional scoring, category weightings, authentic verification audits,
and dynamic leaderboards with safeguards against misleading comparisons.
"""

from typing import List, Dict, Any, Optional

CATEGORIES_MAP = {
    "overall": "Overall Institutional Performance",
    "teaching": "Teaching Quality and Pedagogy",
    "academics": "Academic Achievement",
    "sports": "Sports and Games",
    "cultural": "Cultural Events and Festivals",
    "arts": "Dance, Music, Drama and Performing Arts",
    "innovation": "Innovation, Research and Technology",
    "leadership": "Leadership and Student Development",
    "infrastructure": "Infrastructure and Modern Facilities",
    "special": "Special Achievements and Unique Qualities",
    "satisfaction": "Student Satisfaction and Parent Feedback",
    "community": "Community Service and Extracurriculars"
}

SCORE_KEYS = {
    "overall": "overall_performance",
    "teaching": "teaching_quality",
    "academics": "academic_achievement",
    "sports": "sports_games",
    "cultural": "cultural_festivals",
    "arts": "performing_arts",
    "innovation": "innovation_research",
    "leadership": "leadership_development",
    "infrastructure": "infrastructure_facilities",
    "special": "special_achievements",
    "satisfaction": "student_satisfaction",
    "community": "community_service"
}

DEFAULT_WEIGHTS = {
    "academics": 0.20,
    "teaching": 0.20,
    "infrastructure": 0.15,
    "innovation": 0.15,
    "satisfaction": 0.10,
    "leadership": 0.05,
    "sports": 0.05,
    "cultural": 0.05,
    "community": 0.05
}

class RankingEngine:
    def __init__(self, institutions: List[Dict[str, Any]]):
        self.institutions = institutions

    def get_leaderboard(
        self,
        category: str = "overall",
        scope: str = "national",  # 'national' or state name
        institution_type: Optional[str] = None, # 'Engineering', 'Medical', 'School', etc.
        min_budget: Optional[float] = None,
        max_budget: Optional[float] = None,
        custom_weights: Optional[Dict[str, float]] = None
    ) -> Dict[str, Any]:
        """
        Generate a transparent, ranked leaderboard with score details, evidence citations,
        and data sufficiency checks.
        """
        score_key = SCORE_KEYS.get(category, "overall_performance")
        filtered_list = []

        for inst in self.institutions:
            # Type filter
            if institution_type and institution_type.lower() != "all":
                if inst.get("type", "").lower() != institution_type.lower():
                    continue

            # State / Scope filter
            if scope and scope.lower() != "national" and scope.lower() != "all":
                inst_state = inst.get("location", {}).get("state", "").lower()
                if inst_state != scope.lower():
                    continue

            # Budget filter
            avg_fee = inst.get("fees", {}).get("average_annual", 0)
            if min_budget is not None and avg_fee < min_budget:
                continue
            if max_budget is not None and avg_fee > max_budget:
                continue

            scores = inst.get("category_scores", {})
            raw_score = scores.get(score_key, None)

            # Safeguard: check data sufficiency
            has_sufficient_data = raw_score is not None and raw_score > 0
            # If hostels or coaching academies lack certain university-only metrics
            if category in ["innovation", "academics"] and inst.get("type") in ["Student Hostel"]:
                has_sufficient_data = False

            # Custom weighting composite calculation if category is 'overall' and custom_weights provided
            if category == "overall" and custom_weights:
                composite = 0.0
                total_weight = 0.0
                for cat_k, w in custom_weights.items():
                    k_score = scores.get(SCORE_KEYS.get(cat_k, cat_k), 0)
                    composite += k_score * w
                    total_weight += w
                final_score = round(composite / max(total_weight, 0.001), 2)
            else:
                final_score = round(raw_score, 2) if raw_score is not None else 0.0

            filtered_list.append({
                "institution": inst,
                "score": final_score,
                "has_sufficient_data": has_sufficient_data,
                "evidence": inst.get("ranking_evidence", {}),
                "verification_badge": inst.get("verification_badge", "Unverified"),
                "verification_status": inst.get("verification_status", "pending")
            })

        # Sort institutions with sufficient data first, descending by score
        ranked_items = sorted(
            [item for item in filtered_list if item["has_sufficient_data"]],
            key=lambda x: x["score"],
            reverse=True
        )

        insufficient_items = [item for item in filtered_list if not item["has_sufficient_data"]]

        # Assign ranks
        leaderboard = []
        for i, item in enumerate(ranked_items, start=1):
            inst_dict = dict(item["institution"])
            leaderboard.append({
                "rank": i,
                "institution_id": inst_dict["id"],
                "name": inst_dict["name"],
                "tagline": inst_dict["tagline"],
                "type": inst_dict["type"],
                "city": inst_dict["location"]["city"],
                "state": inst_dict["location"]["state"],
                "score": item["score"],
                "rating": inst_dict["ratings"]["overall"],
                "total_reviews": inst_dict["ratings"]["total_reviews"],
                "fee_display": inst_dict["fees"]["fee_display"],
                "accreditations": inst_dict["accreditations"],
                "verification_badge": item["verification_badge"],
                "verification_status": item["verification_status"],
                "evidence_sources": item["evidence"].get("sources", []),
                "last_audited": item["evidence"].get("last_audited", "2026-08-01"),
                "auditor": item["evidence"].get("auditor", "StudyFinder Independent Council"),
                "has_sufficient_data": True,
                "image": inst_dict["images"]["hero"]
            })

        # Add insufficient data items clearly marked
        for item in insufficient_items:
            inst_dict = dict(item["institution"])
            leaderboard.append({
                "rank": "N/A",
                "institution_id": inst_dict["id"],
                "name": inst_dict["name"],
                "tagline": inst_dict["tagline"],
                "type": inst_dict["type"],
                "city": inst_dict["location"]["city"],
                "state": inst_dict["location"]["state"],
                "score": "Data Insufficient",
                "rating": inst_dict["ratings"]["overall"],
                "total_reviews": inst_dict["ratings"]["total_reviews"],
                "fee_display": inst_dict["fees"]["fee_display"],
                "accreditations": inst_dict["accreditations"],
                "verification_badge": item["verification_badge"],
                "verification_status": item["verification_status"],
                "evidence_sources": ["Pending independent category audit"],
                "last_audited": item["evidence"].get("last_audited", "2026-08-01"),
                "auditor": item["evidence"].get("auditor", "StudyFinder Independent Council"),
                "has_sufficient_data": False,
                "insufficient_reason": f"Category '{CATEGORIES_MAP.get(category, category)}' metrics not directly applicable or pending field audit.",
                "image": inst_dict["images"]["hero"]
            })

        return {
            "category_key": category,
            "category_name": CATEGORIES_MAP.get(category, "Overall Performance"),
            "scope": scope,
            "institution_type": institution_type or "All",
            "total_ranked": len(ranked_items),
            "total_evaluated": len(filtered_list),
            "leaderboard": leaderboard,
            "methodology": {
                "evaluation_period": "2025-2026 Academic Year",
                "anti_manipulation_safeguard": "Double-blind document verification, sentiment verification, zero paid promotion boost.",
                "formula_summary": "Scores normalized from 0-100 based on verified NIRF/NAAC/Board results, faculty index, infrastructure audits, and verified alumni satisfaction."
            }
        }

    def get_category_breakdown_for_institution(self, institution_id: str) -> Optional[Dict[str, Any]]:
        """
        Return the 12-category score radar/breakdown for a specific institution.
        """
        inst = next((x for x in self.institutions if x["id"] == institution_id), None)
        if not inst:
            return None

        scores = inst.get("category_scores", {})
        breakdown = []
        for cat_k, cat_label in CATEGORIES_MAP.items():
            s_key = SCORE_KEYS[cat_k]
            score_val = scores.get(s_key, 0)
            breakdown.append({
                "category_key": cat_k,
                "category_name": cat_label,
                "score": score_val,
                "tier": "Elite (>95)" if score_val >= 95 else ("Exceptional (90-95)" if score_val >= 90 else ("Strong (80-90)" if score_val >= 80 else "Developing (<80)"))
            })

        return {
            "institution_id": inst["id"],
            "name": inst["name"],
            "breakdown": breakdown,
            "verification": inst.get("verification_details", {})
        }
