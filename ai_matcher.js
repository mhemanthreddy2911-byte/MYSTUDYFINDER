/**
 * StudyFinder India — AI 'EduMatch' Recommendation Controller
 * Multi-factor matching engine analyzing budget, career stream, geography,
 * and extracurricular priority preferences.
 */

window.EduMatchController = {
  selectedStage: 'Undergraduate',
  selectedField: 'Engineering',
  selectedState: 'All India',
  budget: 500000,
  priorities: [],
  hostelNeeded: true,

  init() {
    this.bindEvents();
  },

  bindEvents() {
    // Stage buttons
    document.querySelectorAll('.edumatch-stage-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.edumatch-stage-btn').forEach(b => {
          b.classList.remove('bg-blue-600', 'text-white', 'shadow-sm');
          b.classList.add('bg-slate-100', 'text-slate-700');
        });
        btn.classList.add('bg-blue-600', 'text-white', 'shadow-sm');
        btn.classList.remove('bg-slate-100', 'text-slate-700');
        this.selectedStage = btn.dataset.stage;
      });
    });

    // Target Field select
    const fieldSelect = document.getElementById('edumatch-field-select');
    if (fieldSelect) {
      fieldSelect.addEventListener('change', (e) => {
        this.selectedField = e.target.value;
      });
    }

    // State select
    const stateSelect = document.getElementById('edumatch-state-select');
    if (stateSelect) {
      stateSelect.addEventListener('change', (e) => {
        this.selectedState = e.target.value;
      });
    }

    // Budget slider
    const budgetSlider = document.getElementById('edumatch-budget-slider');
    const budgetDisplay = document.getElementById('edumatch-budget-display');
    if (budgetSlider && budgetDisplay) {
      budgetSlider.addEventListener('input', (e) => {
        const val = parseInt(e.target.value);
        this.budget = val;
        budgetDisplay.textContent = `₹${(val / 100000).toFixed(1)} Lakh / year`;
      });
    }

    // Priority pill toggles
    document.querySelectorAll('.edumatch-priority-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        const priority = pill.dataset.priority;
        const idx = this.priorities.indexOf(priority);
        if (idx > -1) {
          this.priorities.splice(idx, 1);
          pill.classList.remove('bg-blue-600', 'text-white', 'border-blue-600');
          pill.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
        } else {
          this.priorities.push(priority);
          pill.classList.add('bg-blue-600', 'text-white', 'border-blue-600');
          pill.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
        }
      });
    });

    // Hostel needed checkbox
    const hostelCb = document.getElementById('edumatch-hostel-cb');
    if (hostelCb) {
      hostelCb.addEventListener('change', (e) => {
        this.hostelNeeded = e.target.checked;
      });
    }

    // Submit button
    const submitBtn = document.getElementById('edumatch-submit-btn');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        this.runRecommendation();
      });
    }
  },

  async runRecommendation() {
    const resultsContainer = document.getElementById('edumatch-results-container');
    if (!resultsContainer) return;

    resultsContainer.innerHTML = `
      <div class="py-16 text-center text-slate-500">
        <div class="inline-block animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600 mb-4"></div>
        <h4 class="font-bold text-slate-800 text-base mb-1">Synthesizing All-India EduMatch Matrix...</h4>
        <p class="text-xs text-slate-500">Calculating compatibility vectors against fees, verified ranks, placements, and facilities...</p>
      </div>
    `;

    try {
      const payload = {
        stage: this.selectedStage,
        target_field: this.selectedField,
        preferred_state: this.selectedState,
        max_annual_budget: this.budget,
        priorities: this.priorities,
        hostel_needed: this.hostelNeeded
      };

      const res = await fetch('/api/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const matches = await res.json();
      this.renderMatches(matches);
    } catch (err) {
      console.error(err);
      resultsContainer.innerHTML = `<div class="p-8 text-center text-red-500">Could not calculate matches.</div>`;
    }
  },

  renderMatches(matches) {
    const resultsContainer = document.getElementById('edumatch-results-container');
    if (!resultsContainer) return;

    if (!matches || matches.length === 0) {
      resultsContainer.innerHTML = `<div class="p-8 text-center text-slate-500">No compatible institutions found. Try adjusting budget or stage.</div>`;
      return;
    }

    resultsContainer.innerHTML = `
      <div class="mb-6 flex items-center justify-between">
        <div>
          <h3 class="text-lg font-black text-slate-900">Your Personalized EduMatch Results</h3>
          <p class="text-xs text-slate-500">Ranked by algorithm compatibility with your career target, budget, and extracurricular priority weights.</p>
        </div>
        <span class="px-3 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full">
          ${matches.length} Top Fits Identified
        </span>
      </div>

      <div class="space-y-4">
        ${matches.map((item, idx) => {
          const inst = item.institution;
          const matchPercent = item.match_percentage;
          const badgeColor = matchPercent >= 90 ? 'bg-emerald-500 text-white' : (matchPercent >= 80 ? 'bg-blue-600 text-white' : 'bg-amber-500 text-white');

          return `
            <div class="glass-card rounded-2xl p-5 border border-slate-200 shadow-sm card-hover-lift flex flex-col md:flex-row items-start md:items-center justify-between gap-5">
              <div class="flex items-start gap-4 flex-1">
                <!-- Match Score Dial -->
                <div class="w-16 h-16 rounded-2xl flex flex-col items-center justify-center font-black ${badgeColor} shrink-0 shadow-sm">
                  <span class="text-lg leading-tight">${matchPercent}%</span>
                  <span class="text-[9px] uppercase tracking-wider font-semibold opacity-90">Match</span>
                </div>

                <div class="flex-1 min-w-0">
                  <div class="flex flex-wrap items-center gap-2 mb-1">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-100 text-blue-800">
                      ${inst.type}
                    </span>
                    <span class="text-xs text-slate-400">•</span>
                    <span class="text-xs text-slate-500">📍 ${inst.location.city}, ${inst.location.state}</span>
                    <span class="text-xs text-slate-400">•</span>
                    <span class="text-xs font-bold text-slate-700">Fee: ${inst.fees.fee_display}</span>
                  </div>

                  <h4 class="font-bold text-slate-900 text-base mb-2">
                    ${inst.name}
                  </h4>

                  <!-- Match Insights -->
                  <div class="space-y-1">
                    ${item.match_insights.map(insight => `
                      <div class="flex items-center gap-1.5 text-xs text-slate-600">
                        <span class="text-emerald-600 font-bold">✓</span>
                        <span>${insight}</span>
                      </div>
                    `).join('')}
                    ${item.hostel_note ? `
                      <div class="flex items-center gap-1.5 text-xs text-blue-600 font-medium">
                        <span>🏠</span>
                        <span>${item.hostel_note}</span>
                      </div>
                    ` : ''}
                  </div>
                </div>
              </div>

              <!-- Action buttons -->
              <div class="flex items-center gap-2 w-full md:w-auto justify-end border-t md:border-t-0 pt-3 md:pt-0 border-slate-100">
                <button onclick="ProfileController.openProfile('${inst.id}')" class="px-4 py-2 bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white rounded-xl text-xs font-bold transition">
                  Full Details
                </button>
                <button onclick="ProfileController.openEnquiryModal('${inst.id}')" class="px-4 py-2 bg-blue-600 text-white hover:bg-blue-700 rounded-xl text-xs font-bold transition shadow-sm">
                  Enquire Now
                </button>
                <button onclick="toggleCompare('${inst.id}', event)" class="p-2 border border-slate-200 hover:bg-slate-100 rounded-xl text-xs font-bold" title="Compare">
                  ⚖️
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.EduMatchController.init();
});
