/**
 * StudyFinder India — Institution Profile Controller
 * Renders rich institution profiles with 12-category score breakdown,
 * interactive action buttons (Call, Chat, Email, Brochure, Enquire, Book Visit),
 * and transparent trust verification cards.
 */

window.ProfileController = {
  activeInstitution: null,

  async openProfile(institutionId) {
    AppState.activeInstitutionId = institutionId;
    const modal = document.getElementById('institution-profile-modal');
    if (!modal) return;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    const contentContainer = document.getElementById('profile-modal-content');
    contentContainer.innerHTML = `
      <div class="py-24 text-center">
        <div class="inline-block animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600 mb-4"></div>
        <p class="text-sm font-semibold text-slate-600">Loading verified institutional dossier...</p>
      </div>
    `;

    try {
      const res = await fetch(`/api/institutions/${institutionId}`);
      if (!res.ok) throw new Error('Failed to load institution');
      const inst = await res.json();
      this.activeInstitution = inst;
      this.renderProfile(inst);
    } catch (err) {
      console.error(err);
      contentContainer.innerHTML = `<div class="p-8 text-center text-red-500">Failed to load institution profile.</div>`;
    }
  },

  renderProfile(inst) {
    const contentContainer = document.getElementById('profile-modal-content');
    if (!contentContainer) return;

    const isSaved = AppState.bookmarks.includes(inst.id);
    const isCompared = AppState.compareList.includes(inst.id);

    contentContainer.innerHTML = `
      <!-- Hero Banner -->
      <div class="relative h-64 md:h-80 w-full overflow-hidden bg-slate-900">
        <img src="${inst.images.hero}" alt="${inst.name}" class="w-full h-full object-cover opacity-75">
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-transparent"></div>

        <!-- Close button -->
        <button onclick="closeModal('institution-profile-modal')" class="absolute top-4 right-4 z-20 w-10 h-10 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center font-bold text-lg transition">
          ✕
        </button>

        <!-- Top Badges -->
        <div class="absolute top-4 left-4 z-10 flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-500 text-white shadow-lg">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
            ${inst.verification_badge}
          </span>
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-blue-600 text-white shadow-lg">
            All-India Rank #${inst.ranks ? inst.ranks.national_overall : '1'}
          </span>
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-white/90 text-slate-900 backdrop-blur-md shadow-lg">
            ${inst.type}
          </span>
        </div>

        <!-- Banner Content -->
        <div class="absolute bottom-6 left-6 right-6 text-white z-10">
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="text-xs font-medium text-slate-300">Est. ${inst.established_year}</span>
            <span class="text-slate-400">•</span>
            <span class="text-xs font-medium text-slate-300">📍 ${inst.location.address}, ${inst.location.city}, ${inst.location.state} (${inst.location.pincode})</span>
          </div>

          <h2 class="text-2xl md:text-3xl font-black leading-tight text-white mb-2">
            ${inst.name}
          </h2>
          <p class="text-sm md:text-base text-slate-300 max-w-3xl font-medium">
            ${inst.tagline}
          </p>
        </div>
      </div>

      <!-- Action Toolbar (Call, Chat, Email, Brochure, Enquire, Book Visit, Compare, Save) -->
      <div class="bg-white border-b border-slate-200 px-6 py-4 flex flex-wrap items-center justify-between gap-3 sticky top-0 z-20 shadow-sm">
        <div class="flex flex-wrap items-center gap-2">
          <button onclick="ProfileController.openEnquiryModal('${inst.id}')" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold transition shadow-sm flex items-center gap-1.5">
            <span>🎯</span> Enquire Now
          </button>
          <button onclick="ProfileController.openVisitModal('${inst.id}')" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold transition shadow-sm flex items-center gap-1.5">
            <span>🗓️</span> Book Campus Visit
          </button>
          <button onclick="ProfileController.openChatModal('${inst.id}')" class="px-3.5 py-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
            <span>💬</span> Live Counselor Chat
          </button>
          <button onclick="ProfileController.openCallModal('${inst.id}')" class="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
            <span>📞</span> Call Office
          </button>
          <button onclick="ProfileController.openBrochure('${inst.id}')" class="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
            <span>📄</span> Official Brochure
          </button>
          <a href="${inst.contact.website}" target="_blank" rel="noopener noreferrer" class="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold transition flex items-center gap-1.5">
            <span>🌐</span> Website
          </a>
        </div>

        <div class="flex items-center gap-2">
          <button onclick="toggleCompare('${inst.id}', event)" class="px-3.5 py-2 rounded-xl text-xs font-bold transition border ${isCompared ? 'bg-amber-500 text-white border-amber-500' : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'}">
            <span>⚖️</span> ${isCompared ? 'In Compare Drawer' : 'Compare'}
          </button>
          <button onclick="toggleBookmark('${inst.id}', event)" class="p-2 rounded-xl text-sm border border-slate-200 hover:bg-slate-50 transition ${isSaved ? 'text-rose-500' : 'text-slate-400'}">
            ${isSaved ? '❤️' : '🤍'}
          </button>
        </div>
      </div>

      <!-- Profile Tabs Navigation -->
      <div class="bg-slate-50 border-b border-slate-200 px-6 overflow-x-auto">
        <div class="flex space-x-6 min-w-max">
          <button onclick="ProfileController.switchProfileTab('tab-overview')" class="profile-tab-btn py-3.5 text-xs font-bold border-b-2 border-blue-600 text-blue-600" data-tab="tab-overview">Overview & Highlights</button>
          <button onclick="ProfileController.switchProfileTab('tab-courses')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-courses">Courses & Fees</button>
          <button onclick="ProfileController.switchProfileTab('tab-rankings')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-rankings">12-Category Scores</button>
          <button onclick="ProfileController.switchProfileTab('tab-facilities')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-facilities">Campus & Facilities</button>
          <button onclick="ProfileController.switchProfileTab('tab-sports-culture')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-sports-culture">Sports & Culture</button>
          <button onclick="ProfileController.switchProfileTab('tab-placements')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-placements">Placements</button>
          <button onclick="ProfileController.switchProfileTab('tab-reviews')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-reviews">Verified Reviews (${inst.reviews ? inst.reviews.length : 0})</button>
          <button onclick="ProfileController.switchProfileTab('tab-verification')" class="profile-tab-btn py-3.5 text-xs font-bold text-slate-500 hover:text-slate-800" data-tab="tab-verification">Trust & Audit Dossier</button>
        </div>
      </div>

      <!-- Profile Tab Contents -->
      <div class="p-6 md:p-8 max-h-[60vh] overflow-y-auto">
        <!-- 1. Tab Overview -->
        <div id="tab-overview" class="profile-tab-panel space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-blue-50/60 p-4 rounded-xl border border-blue-100">
              <span class="text-xs font-semibold text-blue-700 block mb-1">Annual Fee Structure</span>
              <span class="text-lg font-black text-slate-900">${inst.fees.fee_display}</span>
              <span class="text-xs text-slate-500 block mt-1">Hostel: ${inst.fees.hostel_annual > 0 ? '₹' + inst.fees.hostel_annual + '/yr' : 'Subsidized or Day Scholar'}</span>
            </div>

            <div class="bg-emerald-50/60 p-4 rounded-xl border border-emerald-100">
              <span class="text-xs font-semibold text-emerald-700 block mb-1">Student Satisfaction Rating</span>
              <div class="flex items-center gap-2">
                <span class="text-lg font-black text-slate-900">⭐ ${inst.ratings.overall} / 5.0</span>
                <span class="text-xs text-slate-500">(${inst.ratings.total_reviews} verified)</span>
              </div>
              <span class="text-xs text-slate-500 block mt-1">Academics: ${inst.ratings.academic} • Teaching: ${inst.ratings.teaching}</span>
            </div>

            <div class="bg-purple-50/60 p-4 rounded-xl border border-purple-100">
              <span class="text-xs font-semibold text-purple-700 block mb-1">Mentorship & Faculty</span>
              <span class="text-lg font-black text-slate-900">${inst.faculty_summary.student_faculty_ratio}</span>
              <span class="text-xs text-slate-500 block mt-1">${inst.faculty_summary.phd_percentage} Doctoral / Specialist Faculty</span>
            </div>
          </div>

          <div>
            <h4 class="text-sm font-bold text-slate-800 uppercase tracking-wider mb-3">Accreditations & Official Affiliations</h4>
            <div class="flex flex-wrap gap-2">
              ${inst.accreditations.map(acc => `
                <span class="px-3 py-1.5 bg-slate-100 border border-slate-200 text-slate-800 text-xs font-semibold rounded-lg">
                  🛡️ ${acc}
                </span>
              `).join('')}
            </div>
          </div>

          <div>
            <h4 class="text-sm font-bold text-slate-800 uppercase tracking-wider mb-3">Distinguished Highlights</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              ${inst.facilities.slice(0, 6).map(fac => `
                <div class="flex items-center gap-2 p-3 bg-slate-50 rounded-xl border border-slate-100 text-xs font-medium text-slate-700">
                  <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-xs">✓</span>
                  ${fac}
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- 2. Tab Courses & Fees -->
        <div id="tab-courses" class="profile-tab-panel hidden space-y-6">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-slate-700 border border-slate-200 rounded-xl overflow-hidden">
              <thead class="bg-slate-100 text-slate-800 font-bold uppercase text-[11px]">
                <tr>
                  <th class="p-3">Program Name</th>
                  <th class="p-3">Level / Degree</th>
                  <th class="p-3">Duration</th>
                  <th class="p-3">Seats</th>
                  <th class="p-3">Eligibility / Exam</th>
                  <th class="p-3">Estimated Fee</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                ${inst.courses_offered.map(c => `
                  <tr class="hover:bg-slate-50">
                    <td class="p-3 font-bold text-slate-900">${c.name}</td>
                    <td class="p-3">${c.degree}</td>
                    <td class="p-3">${c.duration}</td>
                    <td class="p-3 font-semibold text-slate-800">${c.seats}</td>
                    <td class="p-3 text-slate-600">${c.eligibility}</td>
                    <td class="p-3 font-bold text-blue-600">${c.fees}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>

          <div class="bg-amber-50 p-4 rounded-xl border border-amber-200">
            <h5 class="text-xs font-bold text-amber-800 uppercase mb-2">Available Scholarships & Financial Aid</h5>
            <ul class="text-xs text-amber-900 space-y-1 list-disc list-inside">
              ${inst.fees.scholarships.map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>
        </div>

        <!-- 3. Tab 12-Category Scores -->
        <div id="tab-rankings" class="profile-tab-panel hidden space-y-6">
          <div class="flex items-center justify-between">
            <h4 class="text-sm font-bold text-slate-800 uppercase">12-Dimensional Evaluated Scorecard</h4>
            <span class="text-xs text-slate-500">Evaluation Period: 2025-2026 Academic Year</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            ${Object.entries(inst.category_scores).map(([k, val]) => {
              const labelMap = {
                'overall_performance': 'Overall Institutional Performance',
                'teaching_quality': 'Teaching Quality & Pedagogy',
                'academic_achievement': 'Academic Achievement & Board/Exam Scores',
                'sports_games': 'Sports, Athletics & Games',
                'cultural_festivals': 'Cultural Events & College Festivals',
                'performing_arts': 'Dance, Music, Drama & Performing Arts',
                'innovation_research': 'Innovation, Research & Patents',
                'leadership_development': 'Leadership & Student Development',
                'infrastructure_facilities': 'Infrastructure & Campus Facilities',
                'special_achievements': 'Special Achievements & Unique Qualities',
                'student_satisfaction': 'Student Satisfaction & Parent Feedback',
                'community_service': 'Community Service & Social Impact'
              };
              const title = labelMap[k] || k;
              const barColor = val >= 95 ? 'bg-emerald-500' : (val >= 90 ? 'bg-blue-500' : (val >= 80 ? 'bg-amber-500' : 'bg-slate-400'));

              return `
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                  <div class="flex justify-between items-center text-xs mb-1.5">
                    <span class="font-bold text-slate-800">${title}</span>
                    <span class="font-black text-slate-900">${val} <span class="text-[10px] text-slate-400 font-normal">/ 100</span></span>
                  </div>
                  <div class="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
                    <div class="${barColor} h-full rounded-full transition-all duration-500" style="width: ${val}%"></div>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        </div>

        <!-- 4. Tab Campus & Facilities -->
        <div id="tab-facilities" class="profile-tab-panel hidden space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            ${inst.facilities.map(fac => `
              <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-sm flex items-center gap-2 text-xs font-semibold text-slate-800">
                <span class="text-base">🏛️</span>
                <span>${fac}</span>
              </div>
            `).join('')}
          </div>

          <div>
            <h5 class="text-xs font-bold text-slate-800 uppercase mb-3">Campus Gallery Preview</h5>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
              ${inst.images.gallery.map(img => `
                <div class="h-32 rounded-xl overflow-hidden bg-slate-100 border border-slate-200">
                  <img src="${img}" class="w-full h-full object-cover hover:scale-105 transition-transform" loading="lazy">
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- 5. Tab Sports & Culture -->
        <div id="tab-sports-culture" class="profile-tab-panel hidden space-y-6">
          <div>
            <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2 mb-3">
              <span>🏆</span> Sports & Athletics Excellence (Rank #${inst.ranks ? inst.ranks.sports_rank : 'N/A'} in India)
            </h5>
            <div class="space-y-2">
              ${inst.sports_highlights.map(sh => `
                <div class="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs font-medium text-amber-900 flex items-start gap-2">
                  <span class="font-bold text-amber-600">★</span>
                  <span>${sh}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <div>
            <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2 mb-3">
              <span>🎭</span> Cultural Legacy & Performing Arts
            </h5>
            <div class="space-y-2">
              ${inst.cultural_highlights.map(ch => `
                <div class="p-3 bg-purple-50 rounded-xl border border-purple-200 text-xs font-medium text-purple-900 flex items-start gap-2">
                  <span class="font-bold text-purple-600">★</span>
                  <span>${ch}</span>
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- 6. Tab Placements -->
        <div id="tab-placements" class="profile-tab-panel hidden space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 bg-emerald-50 rounded-xl border border-emerald-200">
              <span class="text-xs font-semibold text-emerald-800 block">Highest Package</span>
              <span class="text-lg font-black text-emerald-950 mt-1 block">${inst.placements.highest_package}</span>
            </div>
            <div class="p-4 bg-blue-50 rounded-xl border border-blue-200">
              <span class="text-xs font-semibold text-blue-800 block">Average Package</span>
              <span class="text-lg font-black text-blue-950 mt-1 block">${inst.placements.average_package}</span>
            </div>
            <div class="p-4 bg-purple-50 rounded-xl border border-purple-200">
              <span class="text-xs font-semibold text-purple-800 block">Placement Rate</span>
              <span class="text-lg font-black text-purple-950 mt-1 block">${inst.placements.placement_rate || '100% Outcome'}</span>
            </div>
          </div>

          <div>
            <h5 class="text-xs font-bold text-slate-800 uppercase mb-3">Prominent Recruiters / Destinations</h5>
            <div class="flex flex-wrap gap-2">
              ${(inst.placements.top_recruiters || []).map(rec => `
                <span class="px-3 py-1.5 bg-slate-100 border border-slate-200 text-slate-800 rounded-lg text-xs font-semibold">
                  💼 ${rec}
                </span>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- 7. Tab Verified Reviews -->
        <div id="tab-reviews" class="profile-tab-panel hidden space-y-6">
          <div class="flex items-center justify-between">
            <div>
              <h5 class="text-sm font-bold text-slate-900">Student & Parent Verified Reviews</h5>
              <p class="text-xs text-slate-500">Every review is checked against verified institutional enrollment.</p>
            </div>
            <button onclick="ProfileController.openWriteReviewModal('${inst.id}')" class="px-3.5 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold transition">
              ✍️ Write a Review
            </button>
          </div>

          <div class="space-y-4">
            ${(inst.reviews || []).map(rev => `
              <div class="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <span class="font-bold text-slate-900 text-xs">${rev.author}</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-100 text-blue-800">${rev.role}</span>
                    ${rev.verified_student ? `
                      <span class="inline-flex items-center gap-1 text-[10px] font-bold text-emerald-700">
                        <svg class="w-3 h-3 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                        Verified
                      </span>
                    ` : ''}
                  </div>
                  <div class="flex items-center gap-1 text-xs">
                    <span class="font-bold text-slate-800">⭐ ${rev.rating}</span>
                    <span class="text-slate-400 text-[11px]">• ${rev.date}</span>
                  </div>
                </div>

                <h6 class="font-bold text-slate-800 text-xs">${rev.title}</h6>
                <p class="text-xs text-slate-600 leading-relaxed">${rev.comment}</p>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- 8. Tab Trust & Verification Dossier -->
        <div id="tab-verification" class="profile-tab-panel hidden space-y-6">
          <div class="p-4 bg-emerald-50 rounded-xl border border-emerald-200">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-emerald-900 uppercase">StudyFinder Transparency Audit</span>
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-600 text-white">Status: Verified</span>
            </div>
            <p class="text-xs text-emerald-800">
              Verified by: <strong>${inst.verification_details.verified_by}</strong> on ${inst.verification_details.verification_date}.
            </p>
            <p class="text-xs text-emerald-800 mt-1">
              Statutory License Code: <strong>${inst.verification_details.official_id}</strong>
            </p>
          </div>

          <div>
            <h5 class="text-xs font-bold text-slate-800 uppercase mb-2">Documents Cross-Examined</h5>
            <div class="space-y-1.5">
              ${inst.verification_details.documents_checked.map(doc => `
                <div class="flex items-center gap-2 text-xs text-slate-700 bg-slate-50 p-2.5 rounded-lg border border-slate-100">
                  <span class="text-emerald-600 font-bold">✓</span>
                  <span>${doc}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="pt-4 border-t border-slate-200 flex justify-between items-center">
            <span class="text-xs text-slate-500">Notice any inaccurate fee, rank, or contact info?</span>
            <button onclick="ProfileController.openReportModal('${inst.id}')" class="text-xs font-bold text-rose-600 hover:text-rose-800 flex items-center gap-1">
              🚩 Report Inaccurate Information
            </button>
          </div>
        </div>
      </div>
    `;
  },

  switchProfileTab(tabId) {
    document.querySelectorAll('.profile-tab-btn').forEach(btn => {
      if (btn.dataset.tab === tabId) {
        btn.classList.add('border-b-2', 'border-blue-600', 'text-blue-600');
        btn.classList.remove('text-slate-500');
      } else {
        btn.classList.remove('border-b-2', 'border-blue-600', 'text-blue-600');
        btn.classList.add('text-slate-500');
      }
    });

    document.querySelectorAll('.profile-tab-panel').forEach(p => {
      if (p.id === tabId) {
        p.classList.remove('hidden');
      } else {
        p.classList.add('hidden');
      }
    });
  },

  // Modals for actions
  openEnquiryModal(institutionId) {
    const inst = AppState.institutions.find(x => x.id === institutionId) || this.activeInstitution;
    const nameEl = document.getElementById('enquiry-modal-inst-name');
    const hiddenIdEl = document.getElementById('enquiry-modal-inst-id');
    if (nameEl && inst) nameEl.textContent = inst.name;
    if (hiddenIdEl) hiddenIdEl.value = institutionId;
    openModal('enquiry-action-modal');
  },

  openVisitModal(institutionId) {
    const inst = AppState.institutions.find(x => x.id === institutionId) || this.activeInstitution;
    const nameEl = document.getElementById('visit-modal-inst-name');
    const hiddenIdEl = document.getElementById('visit-modal-inst-id');
    if (nameEl && inst) nameEl.textContent = inst.name;
    if (hiddenIdEl) hiddenIdEl.value = institutionId;
    openModal('visit-action-modal');
  },

  openCallModal(institutionId) {
    const inst = AppState.institutions.find(x => x.id === institutionId) || this.activeInstitution;
    if (!inst) return;
    alert(`Official Admissions Helpline for ${inst.name}:\n\nPhone: ${inst.contact.phone}\nHelpline: ${inst.contact.helpline}\nEmail: ${inst.contact.email}\n\nOffice Hours: Monday - Saturday (9:00 AM to 5:00 PM IST)`);
  },

  openBrochure(institutionId) {
    const inst = AppState.institutions.find(x => x.id === institutionId) || this.activeInstitution;
    if (!inst) return;
    alert(`📄 Official Prospectus: ${inst.contact.brochure_name}\n\nGenerating high-resolution digital syllabus, fee breakdown, and admission guidelines for ${inst.name}...`);
    showToast(`Downloaded ${inst.contact.brochure_name}`, 'success');
  },

  openChatModal(institutionId) {
    AppState.chatInstitutionId = institutionId;
    const chatModal = document.getElementById('live-chat-modal');
    if (chatModal) {
      chatModal.classList.remove('hidden');
      const inst = AppState.institutions.find(x => x.id === institutionId) || this.activeInstitution;
      const titleEl = document.getElementById('chat-modal-title');
      if (titleEl && inst) titleEl.textContent = `Counselor Chat: ${inst.name}`;
    }
  },

  openWriteReviewModal(institutionId) {
    const hiddenId = document.getElementById('review-modal-inst-id');
    if (hiddenId) hiddenId.value = institutionId;
    openModal('write-review-modal');
  },

  openReportModal(institutionId) {
    const hiddenId = document.getElementById('report-modal-inst-id');
    if (hiddenId) hiddenId.value = institutionId;
    openModal('report-modal');
  }
};
