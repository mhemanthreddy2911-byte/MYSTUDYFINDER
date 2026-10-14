"""
StudyFinder India — AI-Powered 'EduMatch' Recommendation Engine
Analyzes student stage, career aspirations, budget constraints, geographic flexibility,
and priority values (Sports, Research, Placements, Culture) to synthesize personalized recommendations.
"""

from typing import List, Dict, Any, Optional

class EduMatchAI:
    def __init__(self, institutions: List[Dict[str, Any]]):
        self.institutions = institutions

    def recommend(
        self,
        stage: str,  # "School", "Undergraduate", "Postgraduate", "Sports/Arts", "Coaching", "Hostel"
        target_field: str,  # "Engineering", "Medical", "Management", "Law", "Arts & Commerce", "Pure Science", "Sports", "Civil Services", "Design"
        preferred_state: str = "All India",
        max_annual_budget: float = 1000000,
        priorities: Optional[List[str]] = None, # e.g. ["placements", "sports", "cultural", "research", "budget", "faculty"]
        hostel_needed: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Calculates multidimensional compatibility score and synthesizes personalized rationale.
        """
        priorities = [p.lower() for p in (priorities or [])]
        recommendations = []

        for inst in self.institutions:
            inst_type = inst.get("type", "")
            category_label = inst.get("category_label", "")
            location = inst.get("location", {})
            fees = inst.get("fees", {})
            ratings = inst.get("ratings", {})
            category_scores = inst.get("category_scores", {})
            avg_fee = fees.get("average_annual", 0)

            # 1. Type / Field Relevance Score (Weight: 35)
            field_score = 0
            tf = target_field.lower()

            if tf in ["engineering", "tech", "computer science"] and inst_type == "Engineering":
                field_score = 35
            elif tf in ["medical", "healthcare", "doctor", "mbbs"] and inst_type == "Medical":
                field_score = 35
            elif tf in ["management", "business", "mba"] and inst_type == "Management":
                field_score = 35
            elif tf in ["law", "legal"] and inst_type == "Law":
                field_score = 35
            elif tf in ["school", "k-12", "boarding"] and inst_type == "School":
                field_score = 35
            elif tf in ["arts & commerce", "humanities", "economics"] and inst_type == "Degree College":
                field_score = 35
            elif tf in ["sports", "athletics", "football", "badminton"] and "Sports" in inst_type:
                field_score = 35
            elif tf in ["design", "acting", "music", "theatre"] and ("Arts" in inst_type or "Design" in inst_type):
                field_score = 35
            elif tf in ["civil services", "upsc", "jee/neet", "entrance"] and "Coaching" in inst_type:
                field_score = 35
            elif tf in ["hostel", "accommodation", "coliving"] and "Hostel" in inst_type:
                field_score = 35
            elif any(tf in c.get("name", "").lower() for c in inst.get("courses_offered", [])):
                field_score = 28
            else:
                # Partial cross-disciplinary match
                field_score = 12

            # 2. Budget Compatibility (Weight: 20)
            budget_score = 0
            if avg_fee <= max_annual_budget:
                # Well within budget
                savings_ratio = (max_annual_budget - avg_fee) / max(max_annual_budget, 1)
                budget_score = 16 + (4 * min(savings_ratio, 1.0))
            else:
                # Exceeds budget: penalize proportionally
                overage_ratio = (avg_fee - max_annual_budget) / max_annual_budget
                budget_score = max(0, 15 - (overage_ratio * 20))

            # 3. Location / State Compatibility (Weight: 15)
            loc_score = 0
            if preferred_state.lower() in ["all india", "anywhere", "any"]:
                loc_score = 15
            elif preferred_state.lower() == location.get("state", "").lower():
                loc_score = 15
            else:
                # Cross-state penalty, higher tier institutions retain high mobility score
                if inst.get("ranks", {}).get("national_overall", 99) <= 5:
                    loc_score = 11  # Top national institutes justify relocation
                else:
                    loc_score = 6

            # 4. User Priority Alignment (Weight: 20)
            priority_score = 0
            priority_matches = []

            # If no explicit priority, use overall performance
            if not priorities:
                priority_score = (category_scores.get("overall_performance", 85) / 100.0) * 20
            else:
                total_p_weight = len(priorities)
                p_sum = 0
                for p in priorities:
                    if "sports" in p:
                        s_val = category_scores.get("sports_games", 70)
                        p_sum += s_val
                        if s_val >= 90:
                            priority_matches.append(f"Ranked #{inst.get('ranks', {}).get('sports_rank', 'Top')} for Sports & Athletics in India")
                    elif "placements" in p or "career" in p:
                        s_val = (ratings.get("placement", 4.5) / 5.0) * 100
                        p_sum += s_val
                        top_pkg = inst.get("placements", {}).get("highest_package", "")
                        avg_pkg = inst.get("placements", {}).get("average_package", "")
                        if top_pkg and "N/A" not in top_pkg:
                            priority_matches.append(f"Premier Placements: {avg_pkg} avg, up to {top_pkg}")
                    elif "cultural" in p or "arts" in p:
                        s_val = category_scores.get("cultural_festivals", 75)
                        p_sum += s_val
                        if s_val >= 90:
                            priority_matches.append("Celebrated Campus Culture & Asia-renowned Student Festivals")
                    elif "research" in p or "innovation" in p:
                        s_val = category_scores.get("innovation_research", 75)
                        p_sum += s_val
                        if s_val >= 95:
                            priority_matches.append("Tier-1 Innovation Ecosystem with Patented Research Labs")
                    elif "faculty" in p or "teaching" in p:
                        s_val = category_scores.get("teaching_quality", 80)
                        p_sum += s_val
                        ratio = inst.get("faculty_summary", {}).get("student_faculty_ratio", "1:10")
                        priority_matches.append(f"Exceptional {ratio} Faculty-Student Mentorship Ratio")
                    elif "budget" in p or "affordable" in p:
                        s_val = 100 if avg_fee <= 100000 else (80 if avg_fee <= 300000 else 60)
                        p_sum += s_val
                        priority_matches.append(f"Great Value for Money: {fees.get('fee_display', '')}")
                    else:
                        p_sum += category_scores.get("overall_performance", 85)

                priority_score = (p_sum / (total_p_weight * 100.0)) * 20

            # 5. Verification & Accreditation Trust Bonus (Weight: 10)
            trust_score = 10 if inst.get("verification_status") == "verified" else 5

            # 6. Hostel requirement check
            hostel_note = None
            if hostel_needed:
                has_hostel = any("hostel" in f.lower() for f in inst.get("facilities", [])) or inst.get("fees", {}).get("hostel_annual", 0) > 0 or inst_type == "Student Hostel"
                if has_hostel:
                    trust_score += 2
                    hostel_note = "Verified on-campus accommodation with security & meals"
                else:
                    trust_score -= 5
                    hostel_note = "Hostel may require off-campus private arrangement"

            # Compute Total Match Score (0 - 100%)
            total_match = round(min(100.0, max(10.0, field_score + budget_score + loc_score + priority_score + trust_score)), 1)

            # Generate bespoke match insights
            insights = []
            if avg_fee <= max_annual_budget:
                insights.append(f"Fits within your annual budget ({fees.get('fee_display', '')})")
            else:
                insights.append(f"Requires scholarship consideration ({fees.get('fee_display', '')})")

            if priority_matches:
                insights.extend(priority_matches[:2])
            else:
                insights.append(f"Overall Institutional Rating: {ratings.get('overall', 4.5)}/5.0 from verified students")

            if location.get("state"):
                insights.append(f"Location: {location.get('city')}, {location.get('state')} ({location.get('zone', 'India')})")

            recommendations.append({
                "institution": inst,
                "match_percentage": total_match,
                "field_fit": round(field_score / 35.0 * 100),
                "budget_fit": round(budget_score / 20.0 * 100),
                "priority_fit": round(priority_score / 20.0 * 100),
                "match_insights": insights,
                "hostel_note": hostel_note,
                "verification_badge": inst.get("verification_badge", "Verified")
            })

        # Sort descending by match percentage
        recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
        return recommendations[:8]
