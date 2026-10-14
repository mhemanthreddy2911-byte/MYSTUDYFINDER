"""
StudyFinder India — Nationwide Search & Multi-Facet Filtering Engine
Supports full-text query, PIN code resolution, geographic filters, fee brackets,
facilities matching, and instant aggregate counts.
"""

from typing import List, Dict, Any, Optional

class SearchService:
    def __init__(self, institutions: List[Dict[str, Any]]):
        self.institutions = institutions

    def search(
        self,
        query: Optional[str] = None,
        institution_type: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        pincode: Optional[str] = None,
        min_fee: Optional[float] = None,
        max_fee: Optional[float] = None,
        required_facilities: Optional[List[str]] = None,
        min_rating: Optional[float] = None,
        verified_only: bool = False,
        sort_by: str = "rank",  # 'rank', 'rating', 'fee_low', 'fee_high', 'name'
        limit: int = 50,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        Execute multi-parameter search across all institutions.
        """
        results = []
        q = (query or "").strip().lower()

        for inst in self.institutions:
            # 1. Verification filter
            if verified_only and inst.get("verification_status") != "verified":
                continue

            # 2. Type filter
            if institution_type and institution_type.lower() != "all":
                if inst.get("type", "").lower() != institution_type.lower():
                    continue

            # 3. Location: State
            inst_loc = inst.get("location", {})
            if state and state.lower() != "all":
                if inst_loc.get("state", "").lower() != state.lower():
                    continue

            # 4. Location: City
            if city and city.lower() != "all":
                if inst_loc.get("city", "").lower() != city.lower():
                    continue

            # 5. PIN code match (exact or prefix)
            if pincode:
                clean_pin = pincode.strip()
                if not inst_loc.get("pincode", "").startswith(clean_pin):
                    continue

            # 6. Fee Range filter
            avg_fee = inst.get("fees", {}).get("average_annual", 0)
            if min_fee is not None and avg_fee < min_fee:
                continue
            if max_fee is not None and avg_fee > max_fee:
                continue

            # 7. Rating filter
            overall_rating = inst.get("ratings", {}).get("overall", 0.0)
            if min_rating is not None and overall_rating < min_rating:
                continue

            # 8. Facilities filter
            if required_facilities:
                inst_facs = [f.lower() for f in inst.get("facilities", [])]
                matched_all_facs = True
                for rf in required_facilities:
                    rf_clean = rf.strip().lower()
                    if not any(rf_clean in f for f in inst_facs):
                        matched_all_facs = False
                        break
                if not matched_all_facs:
                    continue

            # 9. Query text search (matches name, tagline, city, state, courses, affiliation)
            if q:
                # Searchable text pool
                name = inst.get("name", "").lower()
                tagline = inst.get("tagline", "").lower()
                city_name = inst_loc.get("city", "").lower()
                district_name = inst_loc.get("district", "").lower()
                state_name = inst_loc.get("state", "").lower()
                inst_pin = inst_loc.get("pincode", "").lower()
                courses_text = " ".join([c.get("name", "") + " " + c.get("eligibility", "") for c in inst.get("courses_offered", [])]).lower()
                facilities_text = " ".join(inst.get("facilities", [])).lower()
                accreditations_text = " ".join(inst.get("accreditations", [])).lower()
                type_text = inst.get("type", "").lower()

                full_text = f"{name} {tagline} {city_name} {district_name} {state_name} {inst_pin} {courses_text} {facilities_text} {accreditations_text} {type_text}"
                
                # Check all tokens in query match
                query_tokens = q.split()
                if not all(token in full_text for token in query_tokens):
                    continue

            results.append(inst)

        # Sorting logic
        if sort_by == "rank":
            results.sort(key=lambda x: x.get("ranks", {}).get("national_overall", 999))
        elif sort_by == "rating":
            results.sort(key=lambda x: x.get("ratings", {}).get("overall", 0), reverse=True)
        elif sort_by == "fee_low":
            results.sort(key=lambda x: x.get("fees", {}).get("average_annual", 0))
        elif sort_by == "fee_high":
            results.sort(key=lambda x: x.get("fees", {}).get("average_annual", 0), reverse=True)
        elif sort_by == "name":
            results.sort(key=lambda x: x.get("name", "").lower())

        total = len(results)
        paginated_results = results[offset : offset + limit]

        # Calculate facets for user filtering UI
        facets = self._calculate_facets(results)

        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "results": paginated_results,
            "facets": facets
        }

    def _calculate_facets(self, subset: List[Dict[str, Any]]) -> Dict[str, Any]:
        types_count: Dict[str, int] = {}
        states_count: Dict[str, int] = {}
        cities_count: Dict[str, int] = {}
        verified_count = 0

        for item in subset:
            t = item.get("type", "Other")
            types_count[t] = types_count.get(t, 0) + 1

            s = item.get("location", {}).get("state", "Unknown")
            states_count[s] = states_count.get(s, 0) + 1

            c = item.get("location", {}).get("city", "Unknown")
            cities_count[c] = cities_count.get(c, 0) + 1

            if item.get("verification_status") == "verified":
                verified_count += 1

        return {
            "types": [{"name": k, "count": v} for k, v in sorted(types_count.items(), key=lambda x: x[1], reverse=True)],
            "states": [{"name": k, "count": v} for k, v in sorted(states_count.items(), key=lambda x: x[1], reverse=True)],
            "cities": [{"name": k, "count": v} for k, v in sorted(cities_count.items(), key=lambda x: x[1], reverse=True)],
            "verified_count": verified_count
        }
