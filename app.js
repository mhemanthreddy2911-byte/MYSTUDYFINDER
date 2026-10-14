/**
 * StudyFinder India — Main Application State & Router
 * Tagline: "Find. Compare. Rank. Choose. Succeed."
 */

const AppState = {
  currentTab: 'discovery', // 'discovery', 'rankings', 'recommender', 'compare', 'verification', 'admin'
  institutions: [],
  compareList: [], // Array of up to 4 institution IDs
  bookmarks: [], // Array of saved institution IDs
  activeInstitutionId: null,
  chatInstitutionId: null
};

// Toast notification helper
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  const bgClass = type === 'success' ? 'bg-emerald-600 text-white' : (type === 'error' ? 'bg-rose-600 text-white' : 'bg-slate-900 text-white');
  const icon = type === 'success' ? '✓' : (type === 'error' ? '✕' : 'ℹ');

  toast.className = `flex items-center gap-3 px-4 py-3 rounded-xl shadow-xl transition-all transform duration-300 translate-y-4 opacity-0 ${bgClass}`;
  toast.innerHTML = `
    <span class="font-bold flex items-center justify-center w-6 h-6 rounded-full bg-white/20 text-sm">${icon}</span>
    <span class="text-sm font-medium">${message}</span>
  `;

  container.appendChild(toast);
  setTimeout(() => {
    toast.classList.remove('translate-y-4', 'opacity-0');
  }, 10);

  setTimeout(() => {
    toast.classList.add('opacity-0', 'translate-y-2');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Router: switch primary active views
function switchTab(tabName) {
  AppState.currentTab = tabName;

  // Update navbar active state
  document.querySelectorAll('.nav-link').forEach(btn => {
    if (btn.dataset.tab === tabName) {
      btn.classList.add('text-blue-600', 'font-semibold', 'border-b-2', 'border-blue-600');
      btn.classList.remove('text-slate-600');
    } else {
      btn.classList.remove('text-blue-600', 'font-semibold', 'border-b-2', 'border-blue-600');
      btn.classList.add('text-slate-600');
    }
  });

  // Mobile nav buttons
  document.querySelectorAll('.mobile-nav-btn').forEach(btn => {
    if (btn.dataset.tab === tabName) {
      btn.classList.add('text-blue-600');
      btn.classList.remove('text-slate-500');
    } else {
      btn.classList.remove('text-blue-600');
      btn.classList.add('text-slate-500');
    }
  });

  // Toggle view sections
  const sections = ['discovery-view', 'rankings-view', 'recommender-view', 'compare-view', 'verification-view', 'admin-view'];
  sections.forEach(secId => {
    const el = document.getElementById(secId);
    if (!el) return;
    if (secId === `${tabName}-view`) {
      el.classList.remove('hidden');
    } else {
      el.classList.add('hidden');
    }
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Tab-specific trigger actions
  if (tabName === 'rankings') {
    if (window.RankingsController) window.RankingsController.loadLeaderboard();
  } else if (tabName === 'compare') {
    if (window.CompareController) window.CompareController.renderComparison();
  } else if (tabName === 'admin') {
    if (window.AdminController) window.AdminController.loadAdminData();
  }
}

// Bookmark / Shortlist Management
function toggleBookmark(institutionId, event) {
  if (event) event.stopPropagation();
  const idx = AppState.bookmarks.indexOf(institutionId);
  if (idx > -1) {
    AppState.bookmarks.splice(idx, 1);
    showToast('Removed from your Shortlist.', 'info');
  } else {
    AppState.bookmarks.push(institutionId);
    showToast('Saved to your Shortlist! ❤️', 'success');
  }
  localStorage.setItem('sf_bookmarks', JSON.stringify(AppState.bookmarks));
  updateBookmarkBadges();
  if (window.SearchController) window.SearchController.updateCardBadges();
}

function updateBookmarkBadges() {
  const countEls = document.querySelectorAll('.bookmark-count');
  countEls.forEach(el => {
    el.textContent = AppState.bookmarks.length;
    el.classList.toggle('hidden', AppState.bookmarks.length === 0);
  });
}

// Compare Drawer Management
function toggleCompare(institutionId, event) {
  if (event) event.stopPropagation();
  const idx = AppState.compareList.indexOf(institutionId);
  if (idx > -1) {
    AppState.compareList.splice(idx, 1);
    showToast('Removed from comparison.', 'info');
  } else {
    if (AppState.compareList.length >= 4) {
      showToast('You can compare a maximum of 4 institutions at once.', 'error');
      return;
    }
    AppState.compareList.push(institutionId);
    showToast(`Added to compare drawer (${AppState.compareList.length}/4) ⚖️`, 'success');
  }
  updateCompareDrawer();
  if (window.SearchController) window.SearchController.updateCardBadges();
}

function updateCompareDrawer() {
  const drawer = document.getElementById('compare-drawer');
  const countEl = document.getElementById('compare-drawer-count');
  const chipsContainer = document.getElementById('compare-drawer-chips');

  if (!drawer) return;

  const count = AppState.compareList.length;
  if (count > 0) {
    drawer.classList.remove('translate-y-full');
    drawer.classList.add('translate-y-0');
  } else {
    drawer.classList.add('translate-y-full');
    drawer.classList.remove('translate-y-0');
  }

  if (countEl) countEl.textContent = count;

  if (chipsContainer) {
    chipsContainer.innerHTML = AppState.compareList.map(id => {
      const inst = AppState.institutions.find(x => x.id === id);
      const name = inst ? inst.name : id;
      const shortName = name.length > 20 ? name.substring(0, 18) + '...' : name;
      return `
        <div class="inline-flex items-center gap-1.5 px-3 py-1 bg-white/10 text-white rounded-lg text-xs font-medium border border-white/20">
          <span>${shortName}</span>
          <button onclick="toggleCompare('${id}', event)" class="hover:text-red-300 font-bold ml-1">✕</button>
        </div>
      `;
    }).join('');
  }
}

function clearCompareList() {
  AppState.compareList = [];
  updateCompareDrawer();
  if (window.SearchController) window.SearchController.updateCardBadges();
  showToast('Comparison cleared.', 'info');
}

function triggerCompareView() {
  if (AppState.compareList.length < 2) {
    showToast('Please select at least 2 institutions to compare.', 'error');
    return;
  }
  switchTab('compare');
}

// Modal open/close helpers
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.add('hidden');
  document.body.style.overflow = 'auto';
}

// Global initialization
document.addEventListener('DOMContentLoaded', () => {
  // Load saved bookmarks
  try {
    const saved = localStorage.getItem('sf_bookmarks');
    if (saved) AppState.bookmarks = JSON.parse(saved);
  } catch (e) {}

  updateBookmarkBadges();

  // Navigation click handlers
  document.querySelectorAll('.nav-link, .mobile-nav-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const tab = btn.dataset.tab;
      if (tab) switchTab(tab);
    });
  });

  // Global escape key to close modals
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-wrapper:not(.hidden)').forEach(modal => {
        modal.classList.add('hidden');
      });
      document.body.style.overflow = 'auto';
    }
  });
});
