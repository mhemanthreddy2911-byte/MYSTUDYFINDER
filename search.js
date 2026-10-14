/**
 * StudyFinder India — Search & Discovery Controller
 * Manages full-text search, PIN code matching, multi-facet filtering, and result card rendering.
 */

window.SearchController = {
  currentFilters: {
    q: '',
    type: '',
    state: '',
    city: '',
    pincode: '',
    max_fee: null,
    min_rating: null,
    verified_only: false,
    facilities: [],
    sort_by: 'rank'
  },

  init() {
    this.bindEvents();
    this.fetchInstitutions();
  },

  bindEvents() {
    // Hero & Navbar search inputs
    const heroSearchInput = document.getElementById('hero-search-input');
    const heroStateSelect = document.getElementById('hero-state-select');
    const heroTypeSelect = document.getElementById('hero-type-select');
    const heroPinInput = document.getElementById('hero-pin-input');
    const heroSearchBtn = document.getElementById('hero-search-btn');

    if (heroSearchBtn) {
      heroSearchBtn.addEventListener('click', () => {
        this.currentFilters.q = heroSearchInput ? heroSearchInput.value.trim() : '';
        this.currentFilters.state = heroStateSelect ? heroStateSelect.value : '';
        this.currentFilters.type = heroTypeSelect ? heroTypeSelect.value : '';
        this.currentFilters.pincode = heroPinInput ? heroPinInput.value.trim() : '';
        this.fetchInstitutions();
        switchTab('discovery');
      });
    }

    if (heroSearchInput) {
      heroSearchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
          if (heroSearchBtn) heroSearchBtn.click();
        }
      });
    }

    // Filter Sidebar inputs
    const sidebarSearch = document.getElementById('sidebar-search-input');
    if (sidebarSearch) {
      sidebarSearch.addEventListener('input', (e) => {
        this.currentFilters.q = e.target.value.trim();
        this.debounceFetch();
      });
    }

    const sortSelect = document.getElementById('sort-by-select');
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        this.currentFilters.sort_by = e.target.value;
        this.fetchInstitutions();
      });
    }

    const verifiedToggle = document.getElementById('filter-verified-toggle');
    if (verifiedToggle) {
      verifiedToggle.addEventListener('change', (e) => {
        this.currentFilters.verified_only = e.target.checked;
        this.fetchInstitutions();
      });
    }

    const feeSlider = document.getElementById('filter-fee-slider');
    const feeLabel = document.getElementById('filter-fee-label');
    if (feeSlider) {
      feeSlider.addEventListener('input', (e) => {
        const val = parseInt(e.target.value);
        if (val >= 1500000) {
          feeLabel.textContent = 'Any Budget (No Limit)';
          this.currentFilters.max_fee = null;
        } else {
          feeLabel.textContent = `Up to ₹${(val / 100000).toFixed(1)} Lakh / yr`;
          this.currentFilters.max_fee = val;
        }
        this.debounceFetch();
      });
    }

    // Facility checkboxes
    document.querySelectorAll('.facility-checkbox').forEach(cb => {
      cb.addEventListener('change', () => {
        const checkedFacs = Array.from(document.querySelectorAll('.facility-checkbox:checked')).map(c => c.value);
        this.currentFilters.facilities = checkedFacs;
        this.fetchInstitutions();
      });
    });

    // Rating filter buttons
    document.querySelectorAll('.rating-filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.rating-filter-btn').forEach(b => b.classList.remove('bg-blue-600', 'text-white'));
        btn.classList.add('bg-blue-600', 'text-white');
        const minR = parseFloat(btn.dataset.rating);
        this.currentFilters.min_rating = minR > 0 ? minR : null;
        this.fetchInstitutions();
      });
    });

    // Quick filter chips
    document.querySelectorAll('.quick-filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const type = chip.dataset.type;
        const query = chip.dataset.query;
        if (type) this.currentFilters.type = type;
        if (query) this.currentFilters.q = query;
        if (heroTypeSelect) heroTypeSelect.value = type || '';
        this.fetchInstitutions();
        switchTab('discovery');
      });
    });
  },

  debounceTimer: null,
  debounceFetch() {
    clearTimeout(this.debounceTimer);
    this.debounceTimer = setTimeout(() => this.fetchInstitutions(), 300);
  },

  async fetchInstitutions() {
    const resultsContainer = document.getElementById('institutions-results-grid');
    const countBadge = document.getElementById('results-count-badge');
    const loadingSpinner = document.getElementById('search-loading-spinner');

    if (loadingSpinner) loadingSpinner.classList.remove('hidden');

    try {
      const params = new URLSearchParams();
      if (this.currentFilters.q) params.append('q', this.currentFilters.q);
      if (this.currentFilters.type && this.currentFilters.type !== 'all') params.append('type', this.currentFilters.type);
      if (this.currentFilters.state && this.currentFilters.state !== 'all') params.append('state', this.currentFilters.state);
      if (this.currentFilters.city && this.currentFilters.city !== 'all') params.append('city', this.currentFilters.city);
      if (this.currentFilters.pincode) params.append('pincode', this.currentFilters.pincode);
      if (this.currentFilters.max_fee) params.append('max_fee', this.currentFilters.max_fee);
      if (this.currentFilters.min_rating) params.append('min_rating', this.currentFilters.min_rating);
      if (this.currentFilters.verified_only) params.append('verified_only', 'true');
      if (this.currentFilters.facilities.length > 0) params.append('facilities', this.currentFilters.facilities.join(','));
      if (this.currentFilters.sort_by) params.append('sort_by', this.currentFilters.sort_by);

      const res = await fetch(`/api/institutions?${params.toString()}`);
      const data = await res.json();

      AppState.institutions = data.results || [];
      if (countBadge) countBadge.textContent = `${data.total} Institutions Found`;

      this.renderInstitutions(data.results || []);
      this.renderFacetPills(data.facets || {});
    } catch (err) {
      console.error('Error fetching institutions:', err);
      showToast('Could not fetch institutions. Please check your network.', 'error');
    } finally {
      if (loadingSpinner) loadingSpinner.classList.add('hidden');
    }
  },

  renderInstitutions(institutions) {
    const container = document.getElementById('institutions-results-grid');
    if (!container) return;

    if (institutions.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-16 text-center bg-white rounded-2xl border border-dashed border-slate-300 p-8">
          <div class="w-16 h-16 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">🔍</div>
          <h3 class="text-xl font-bold text-slate-800 mb-2">No institutions match your current filter</h3>
          <p class="text-slate-500 max-w-md mx-auto mb-6 text-sm">Try broadening your search term, adjusting the fee slider, or clearing city/state restrictions.</p>
          <button onclick="SearchController.resetFilters()" class="px-5 py-2.5 bg-blue-600 text-white rounded-xl text-sm font-semibold hover:bg-blue-700 transition">Reset All Filters</button>
        </div>
      `;
      return;
    }

    container.innerHTML = institutions.map(inst => {
      const isSaved = AppState.bookmarks.includes(inst.id);
      const isCompared = AppState.compareList.includes(inst.id);
      const natRank = inst.ranks ? inst.ranks.national_overall : 'N/A';
      const sportsRank = inst.ranks ? inst.ranks.sports_rank : null;

      // Color coding per type
      const typeColors = {
        'Engineering': 'bg-blue-50 text-blue-700 border-blue-200',
        'Medical': 'bg-emerald-50 text-emerald-700 border-emerald-200',
        'Management': 'bg-amber-50 text-amber-700 border-amber-200',
        'Law': 'bg-purple-50 text-purple-700 border-purple-200',
        'School': 'bg-orange-50 text-orange-700 border-orange-200',
        'Sports & Arts Academy': 'bg-rose-50 text-rose-700 border-rose-200',
        'Degree College': 'bg-cyan-50 text-cyan-700 border-cyan-200',
        'Research': 'bg-indigo-50 text-indigo-700 border-indigo-200',
        'Coaching & Test Prep': 'bg-lime-50 text-lime-700 border-lime-200',
        'Student Hostel': 'bg-pink-50 text-pink-700 border-pink-200'
      };
      const badgeClass = typeColors[inst.type] || 'bg-slate-50 text-slate-700 border-slate-200';

      return `
        <div class="card-hover-lift glass-card rounded-2xl overflow-hidden shadow-sm flex flex-col justify-between border border-slate-200/80 group">
          <!-- Image & Badges -->
          <div class="relative h-48 w-full overflow-hidden bg-slate-100">
            <img src="${inst.images.hero}" alt="${inst.name}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

            <!-- Verification Badge -->
            <div class="absolute top-3 left-3 flex flex-wrap gap-1.5">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-500/90 text-white backdrop-blur-md shadow-sm">
                <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                ${inst.verification_badge.replace('StudyFinder ', '')}
              </span>
              <span class="px-2 py-0.5 rounded-full text-[11px] font-bold bg-white/90 text-slate-800 backdrop-blur-md shadow-sm">
                Rank #${natRank}
              </span>
            </div>

            <!-- Bookmark / Compare top right toggles -->
            <div class="absolute top-3 right-3 flex items-center gap-1.5">
              <button onclick="toggleCompare('${inst.id}', event)" title="Add to Compare" class="w-8 h-8 rounded-full flex items-center justify-center transition ${isCompared ? 'bg-amber-500 text-white shadow-md' : 'bg-black/40 text-white hover:bg-black/60'}">
                <span class="text-xs font-bold">⚖️</span>
              </button>
              <button onclick="toggleBookmark('${inst.id}', event)" title="Save to Shortlist" class="w-8 h-8 rounded-full flex items-center justify-center transition ${isSaved ? 'bg-rose-500 text-white shadow-md' : 'bg-black/40 text-white hover:bg-black/60'}">
                <span class="text-xs">${isSaved ? '❤️' : '🤍'}</span>
              </button>
            </div>

            <!-- Bottom Image Overlay info -->
            <div class="absolute bottom-2.5 left-3 right-3 flex justify-between items-end text-white">
              <div class="flex items-center gap-1 text-xs">
                <svg class="w-3.5 h-3.5 text-amber-400 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                <span class="font-bold text-sm">${inst.ratings.overall}</span>
                <span class="text-slate-300 text-[11px]">(${inst.ratings.total_reviews} verified)</span>
              </div>
              <span class="text-xs font-medium text-slate-200 flex items-center gap-1">
                📍 ${inst.location.city}, ${inst.location.state}
              </span>
            </div>
          </div>

          <!-- Card Body -->
          <div class="p-5 flex-1 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="px-2.5 py-0.5 rounded-md text-[11px] font-semibold border ${badgeClass}">
                  ${inst.type}
                </span>
                <span class="text-[11px] text-slate-500 font-mono">PIN: ${inst.location.pincode}</span>
              </div>

              <h4 class="font-bold text-slate-900 text-base leading-snug group-hover:text-blue-600 transition-colors line-clamp-1 mb-1">
                ${inst.name}
              </h4>
              <p class="text-xs text-slate-500 line-clamp-1 mb-3">
                ${inst.tagline}
              </p>

              <!-- Key Badges & Facilities -->
              <div class="flex flex-wrap gap-1.5 mb-4">
                ${inst.accreditations.slice(0, 2).map(acc => `
                  <span class="px-2 py-0.5 bg-slate-100 text-slate-700 text-[10px] font-medium rounded-md">
                    ${acc}
                  </span>
                `).join('')}
                ${sportsRank && sportsRank <= 10 ? `
                  <span class="px-2 py-0.5 bg-amber-50 text-amber-800 text-[10px] font-semibold rounded-md border border-amber-200">
                    🏆 #${sportsRank} in Sports
                  </span>
                ` : ''}
              </div>
            </div>

            <!-- Fee & Actions -->
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between mt-auto">
              <div>
                <span class="text-[10px] uppercase tracking-wider text-slate-400 font-semibold block">Annual Fee</span>
                <span class="text-xs font-bold text-slate-900">${inst.fees.fee_display}</span>
              </div>

              <div class="flex items-center gap-2">
                <button onclick="ProfileController.openProfile('${inst.id}')" class="px-3 py-1.5 bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white rounded-lg text-xs font-semibold transition">
                  Details
                </button>
                <button onclick="ProfileController.openEnquiryModal('${inst.id}')" class="px-3 py-1.5 bg-blue-600 text-white hover:bg-blue-700 rounded-lg text-xs font-semibold transition shadow-sm">
                  Enquire
                </button>
              </div>
            </div>
          </div>
        </div>
      `;
    }).join('');
  },

  renderFacetPills(facets) {
    const container = document.getElementById('state-facet-chips');
    if (!container || !facets.states) return;

    container.innerHTML = facets.states.slice(0, 8).map(st => `
      <button onclick="SearchController.filterByState('${st.name}')" class="px-3 py-1 rounded-full text-xs font-medium border ${this.currentFilters.state === st.name ? 'bg-blue-600 text-white border-blue-600' : 'bg-white text-slate-700 border-slate-200 hover:border-blue-400'} transition">
        ${st.name} <span class="opacity-70 text-[10px]">(${st.count})</span>
      </button>
    `).join('');
  },

  filterByState(stateName) {
    if (this.currentFilters.state === stateName) {
      this.currentFilters.state = '';
    } else {
      this.currentFilters.state = stateName;
    }
    const heroStateSelect = document.getElementById('hero-state-select');
    if (heroStateSelect) heroStateSelect.value = this.currentFilters.state;
    this.fetchInstitutions();
  },

  resetFilters() {
    this.currentFilters = {
      q: '',
      type: '',
      state: '',
      city: '',
      pincode: '',
      max_fee: null,
      min_rating: null,
      verified_only: false,
      facilities: [],
      sort_by: 'rank'
    };

    const sidebarSearch = document.getElementById('sidebar-search-input');
    if (sidebarSearch) sidebarSearch.value = '';

    const heroSearchInput = document.getElementById('hero-search-input');
    if (heroSearchInput) heroSearchInput.value = '';

    const feeSlider = document.getElementById('filter-fee-slider');
    const feeLabel = document.getElementById('filter-fee-label');
    if (feeSlider) feeSlider.value = 1500000;
    if (feeLabel) feeLabel.textContent = 'Any Budget (No Limit)';

    document.querySelectorAll('.facility-checkbox').forEach(cb => cb.checked = false);
    document.querySelectorAll('.rating-filter-btn').forEach(b => b.classList.remove('bg-blue-600', 'text-white'));

    this.fetchInstitutions();
    showToast('Filters cleared to default nationwide view.', 'info');
  },

  updateCardBadges() {
    // Re-render to update compare / bookmark icons
    if (AppState.institutions.length > 0) {
      this.renderInstitutions(AppState.institutions);
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.SearchController.init();
});
