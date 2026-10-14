/**
 * StudyFinder India — Side-by-Side Comparison Controller
 * Renders side-by-side matrices for 2 to 4 institutions across fees, rankings,
 * faculty metrics, sports, culture, and hostel facilities.
 */

window.CompareController = {
  async renderComparison() {
    const container = document.getElementById('compare-matrix-container');
    const emptyState = document.getElementById('compare-empty-state');
    if (!container) return;

    if (AppState.compareList.length < 2) {
      if (emptyState) emptyState.classList.remove('hidden');
      container.classList.add('hidden');
      return;
    }

    if (emptyState) emptyState.classList.add('hidden');
    container.classList.remove('hidden');

    container.innerHTML = `
      <div class="py-16 text-center text-slate-400">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mb-3"></div>
        <p class="text-sm font-semibold text-slate-600">Generating side-by-side comparison matrix...</p>
      </div>
    `;

    try {
      const res = await fetch('/api/compare', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ institution_ids: AppState.compareList })
      });
      const data = await res.json();
      this.displayMatrix(data);
    } catch (err) {
      console.error(err);
      container.innerHTML = `<div class="p-8 text-center text-red-500">Failed to generate comparison.</div>`;
    }
  },

  displayMatrix(data) {
    const container = document.getElementById('compare-matrix-container');
    if (!container) return;

    const institutions = data.institutions;
    const metrics = data.metrics;

    container.innerHTML = `
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse border border-slate-200 rounded-2xl overflow-hidden bg-white shadow-sm">
          <!-- Table Header: Institution Cards -->
          <thead>
            <tr class="bg-slate-50 border-b border-slate-200">
              <th class="p-4 w-1/4 text-xs font-bold text-slate-500 uppercase tracking-wider">Metric Comparison</th>
              ${institutions.map(inst => `
                <th class="p-4 w-1/${institutions.length + 1} align-top">
                  <div class="relative rounded-xl overflow-hidden h-28 mb-3 border border-slate-200">
                    <img src="${inst.images.hero}" class="w-full h-full object-cover">
                    <button onclick="toggleCompare('${inst.id}')" class="absolute top-2 right-2 w-6 h-6 rounded-full bg-black/60 text-white flex items-center justify-center text-xs font-bold hover:bg-red-600 transition">
                      ✕
                    </button>
                    <span class="absolute bottom-2 left-2 px-2 py-0.5 rounded text-[10px] font-bold bg-white/90 text-slate-800 shadow">
                      Rank #${inst.ranks ? inst.ranks.national_overall : '1'}
                    </span>
                  </div>
                  <h4 class="font-bold text-slate-900 text-sm leading-tight mb-1">${inst.name}</h4>
                  <span class="text-xs text-slate-500 block mb-2">📍 ${inst.location.city}, ${inst.location.state}</span>
                  <button onclick="ProfileController.openProfile('${inst.id}')" class="w-full py-1.5 bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white rounded-lg text-xs font-bold transition">
                    View Details
                  </button>
                </th>
              `).join('')}
            </tr>
          </thead>

          <!-- Metric Rows -->
          <tbody class="divide-y divide-slate-100 text-xs text-slate-700">
            ${metrics.map(m => `
              <tr class="hover:bg-slate-50/60 transition">
                <td class="p-4 font-bold text-slate-900 bg-slate-50/40">${m.label}</td>
                ${institutions.map(inst => `
                  <td class="p-4 font-semibold text-slate-800">
                    ${m.values[inst.id] || 'N/A'}
                  </td>
                `).join('')}
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  }
};
