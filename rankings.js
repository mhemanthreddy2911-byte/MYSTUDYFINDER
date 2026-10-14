/**
 * StudyFinder India — Advanced All-India Ranking System Controller
 * Transparent leaderboards across 12 dimensions with anti-fraud methodology disclosure
 * and data sufficiency badges.
 */

window.RankingsController = {
  currentCategory: 'overall',
  currentScope: 'national',
  currentType: '',
  maxBudget: null,

  init() {
    this.bindEvents();
  },

  bindEvents() {
    // 12 Category pill tabs
    document.querySelectorAll('.ranking-cat-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.ranking-cat-btn').forEach(b => {
          b.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
          b.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
        });
        btn.classList.add('bg-blue-600', 'text-white', 'shadow-md');
        btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');

        this.currentCategory = btn.dataset.category;
        this.loadLeaderboard();
      });
    });

    // Scope select (National vs State-wise)
    const scopeSelect = document.getElementById('ranking-scope-select');
    if (scopeSelect) {
      scopeSelect.addEventListener('change', (e) => {
        this.currentScope = e.target.value;
        this.loadLeaderboard();
      });
    }

    // Type filter
    const typeSelect = document.getElementById('ranking-type-select');
    if (typeSelect) {
      typeSelect.addEventListener('change', (e) => {
        this.currentType = e.target.value;
        this.loadLeaderboard();
      });
    }
  },

  async loadLeaderboard() {
    const listContainer = document.getElementById('rankings-list-container');
    const headerTitle = document.getElementById('ranking-category-title');
    const headerSub = document.getElementById('ranking-category-subtitle');
    const totalRankedBadge = document.getElementById('ranking-total-badge');

    if (!listContainer) return;
    listContainer.innerHTML = `
      <div class="py-16 text-center text-slate-400">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-3"></div>
        <p class="text-sm font-medium">Calculating verified rankings and cross-referencing audit sources...</p>
      </div>
    `;

    try {
      const params = new URLSearchParams();
      params.append('category', this.currentCategory);
      if (this.currentScope) params.append('scope', this.currentScope);
      if (this.currentType) params.append('type', this.currentType);
      if (this.maxBudget) params.append('max_budget', this.maxBudget);

      const res = await fetch(`/api/rankings?${params.toString()}`);
      const data = await res.json();

      if (headerTitle) headerTitle.textContent = `${data.category_name} Leaderboard`;
      if (headerSub) {
        headerSub.textContent = `Scope: ${this.currentScope === 'national' ? 'All-India National' : this.currentScope} • ${data.total_ranked} Verified Institutions Evaluated`;
      }
      if (totalRankedBadge) totalRankedBadge.textContent = `${data.total_ranked} Institutions Ranked`;

      this.renderLeaderboard(data.leaderboard || [], data.methodology);
    } catch (err) {
      console.error('Error loading rankings:', err);
      listContainer.innerHTML = `<div class="p-8 text-center text-red-500">Could not calculate leaderboard. Please retry.</div>`;
    }
  },

  renderLeaderboard(items, methodology) {
    const container = document.getElementById('rankings-list-container');
    if (!container) return;

    if (items.length === 0) {
      container.innerHTML = `
        <div class="bg-white rounded-2xl p-12 text-center border border-slate-200">
          <p class="text-slate-600 font-medium">No institutions found matching this category and scope filter.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = items.map((item, idx) => {
      const isTop3 = item.rank === 1 || item.rank === 2 || item.rank === 3;
      const rankBg = item.rank === 1 ? 'bg-amber-500 text-white shadow-md' : (item.rank === 2 ? 'bg-slate-400 text-white' : (item.rank === 3 ? 'bg-amber-700 text-white' : 'bg-slate-100 text-slate-700 font-bold'));
      const rankIcon = item.rank === 1 ? '🥇' : (item.rank === 2 ? '🥈' : (item.rank === 3 ? '🥉' : `#${item.rank}`));

      // Check if data is sufficient
      if (!item.has_sufficient_data) {
        return `
          <div class="glass-card rounded-2xl p-5 border border-slate-200 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 bg-slate-50/50 opacity-80">
            <div class="flex items-center gap-4">
              <span class="w-12 h-12 rounded-xl flex items-center justify-center font-bold text-xs bg-slate-200 text-slate-600">
                N/A
              </span>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h4 class="font-bold text-slate-800 text-base">${item.name}</h4>
                  <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-slate-200 text-slate-700">${item.type}</span>
                </div>
                <p class="text-xs text-amber-700 flex items-center gap-1 font-medium">
                  ⚠️ ${item.insufficient_reason || 'Insufficient category specific audit data — Rank withheld to maintain integrity.'}
                </p>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <button onclick="ProfileController.openProfile('${item.institution_id}')" class="px-3 py-1.5 bg-white border border-slate-200 hover:bg-slate-100 text-slate-700 rounded-lg text-xs font-semibold">
                View Profile
              </button>
            </div>
          </div>
        `;
      }

      return `
        <div class="glass-card rounded-2xl p-5 border ${isTop3 ? 'border-blue-200 shadow-sm bg-gradient-to-r from-blue-50/40 via-white to-white' : 'border-slate-200/80'} card-hover-lift flex flex-col md:flex-row items-start md:items-center justify-between gap-4 group">
          <!-- Rank & Institution info -->
          <div class="flex items-start md:items-center gap-4 flex-1">
            <span class="w-12 h-12 rounded-xl flex items-center justify-center font-bold text-base shrink-0 ${rankBg}">
              ${rankIcon}
            </span>

            <img src="${item.image}" alt="${item.name}" class="w-14 h-14 rounded-xl object-cover shrink-0 hidden sm:block border border-slate-200">

            <div class="flex-1 min-w-0">
              <div class="flex flex-wrap items-center gap-2 mb-1">
                <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-100 text-blue-800">
                  ${item.type}
                </span>
                <span class="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-700">
                  <svg class="w-3 h-3 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                  ${item.verification_badge}
                </span>
                <span class="text-xs text-slate-400">•</span>
                <span class="text-xs text-slate-500">📍 ${item.city}, ${item.state}</span>
              </div>

              <h4 class="font-bold text-slate-900 text-base group-hover:text-blue-600 transition truncate">
                ${item.name}
              </h4>

              <div class="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-slate-500 mt-1">
                <span class="font-semibold text-slate-800">Fee: ${item.fee_display}</span>
                <span>•</span>
                <span>⭐ ${item.rating} (${item.total_reviews} reviews)</span>
                <span>•</span>
                <span class="text-slate-600">Audit Source: <strong class="text-slate-800">${item.evidence_sources[0] || 'Official Gazette'}</strong></span>
              </div>
            </div>
          </div>

          <!-- Score & Actions -->
          <div class="flex items-center gap-4 w-full md:w-auto justify-between md:justify-end border-t md:border-t-0 pt-3 md:pt-0 border-slate-100">
            <div class="text-left md:text-right">
              <span class="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">Audited Score</span>
              <div class="flex items-baseline gap-1">
                <span class="text-xl font-black text-blue-600">${item.score}</span>
                <span class="text-xs font-semibold text-slate-400">/ 100</span>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <button onclick="ProfileController.openProfile('${item.institution_id}')" class="px-3.5 py-2 bg-blue-600 text-white rounded-xl text-xs font-semibold hover:bg-blue-700 transition shadow-sm">
                View Profile
              </button>
              <button onclick="toggleCompare('${item.institution_id}', event)" class="p-2 border border-slate-200 hover:bg-slate-100 rounded-xl text-xs font-bold text-slate-700 transition" title="Add to Compare">
                ⚖️
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.RankingsController.init();
});
