/**
 * StudyFinder India — Trust, Verification & Admin Dashboard Controller
 * Handles institution claim submissions, inaccuracy reports, verified reviews,
 * live admissions counselor chat, and the institution registrar dashboard.
 */

window.AdminController = {
  init() {
    this.bindEvents();
    this.initChat();
  },

  bindEvents() {
    // 1. Institution Claim Application Form
    const claimForm = document.getElementById('claim-institution-form');
    if (claimForm) {
      claimForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
          institution_name: document.getElementById('claim-inst-name').value,
          applicant_name: document.getElementById('claim-applicant-name').value,
          designation: document.getElementById('claim-designation').value,
          official_email: document.getElementById('claim-email').value,
          phone: document.getElementById('claim-phone').value,
          registration_number: document.getElementById('claim-license-id').value,
          document_types: ['Affiliation Letter', 'Fee Transparency Declaration', 'Infrastructure Geotagged Audit']
        };

        try {
          const res = await fetch('/api/verify/claim', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            alert(`✅ Verification Application Submitted!\n\nTracking ID: ${data.claim_id}\n\nOur Central Audit Board has received your documents. A regional verification officer will inspect credentials within 48-72 hours.`);
            claimForm.reset();
            showToast(`Claim application logged (${data.claim_id})`, 'success');
          }
        } catch (err) {
          showToast('Failed to submit claim application.', 'error');
        }
      });
    }

    // 2. Inaccuracy Report Form
    const reportForm = document.getElementById('report-discrepancy-form');
    if (reportForm) {
      reportForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
          institution_id: document.getElementById('report-modal-inst-id').value,
          category: document.getElementById('report-category-select').value,
          description: document.getElementById('report-description').value,
          evidence_link: document.getElementById('report-evidence-link').value,
          reporter_role: document.getElementById('report-role-select').value
        };

        try {
          const res = await fetch('/api/verify/report', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            alert(`🛡️ Inaccuracy Report Logged (${data.report_id})\n\nThank you for protecting educational truth! Our audit team will review official gazettes and correct any discrepancy immediately.`);
            closeModal('report-modal');
            reportForm.reset();
            showToast('Discrepancy report recorded.', 'success');
          }
        } catch (err) {
          showToast('Failed to log report.', 'error');
        }
      });
    }

    // 3. Enquiry Form
    const enquiryForm = document.getElementById('admissions-enquiry-form');
    if (enquiryForm) {
      enquiryForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
          institution_id: document.getElementById('enquiry-modal-inst-id').value,
          student_name: document.getElementById('enquiry-name').value,
          email: document.getElementById('enquiry-email').value,
          phone: document.getElementById('enquiry-phone').value,
          target_course: document.getElementById('enquiry-course').value,
          message: document.getElementById('enquiry-message').value
        };

        try {
          const res = await fetch('/api/enquire', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            alert(`🎯 Enquiry Sent Successfully!\n\nReference: ${data.enquiry_id}\n\nYour message was forwarded to ${data.institution_name}'s official admissions desk. An academic counselor will reach out shortly.`);
            closeModal('enquiry-action-modal');
            enquiryForm.reset();
            showToast('Admissions enquiry delivered!', 'success');
          }
        } catch (err) {
          showToast('Could not deliver enquiry.', 'error');
        }
      });
    }

    // 4. Visit Booking Form
    const visitForm = document.getElementById('book-visit-form');
    if (visitForm) {
      visitForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
          institution_id: document.getElementById('visit-modal-inst-id').value,
          visitor_name: document.getElementById('visit-visitor-name').value,
          email: document.getElementById('visit-email').value,
          phone: document.getElementById('visit-phone').value,
          visit_date: document.getElementById('visit-date').value,
          slot: document.getElementById('visit-slot').value,
          attendees: parseInt(document.getElementById('visit-attendees').value || '2'),
          purpose: document.getElementById('visit-purpose').value
        };

        try {
          const res = await fetch('/api/book-visit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            alert(`🎉 Campus Visit Pass Confirmed!\n\nPass ID: ${data.visit_pass.visit_pass_id}\nDate: ${data.visit_pass.visit_date} (${data.visit_pass.slot})\nAttendees: ${data.visit_pass.attendees}\nGate Pass Token: ${data.visit_pass.qr_code_token}\n\nPlease present this pass ID at the main campus security gate.`);
            closeModal('visit-action-modal');
            visitForm.reset();
            showToast('Campus Visit Pass generated!', 'success');
          }
        } catch (err) {
          showToast('Could not book visit pass.', 'error');
        }
      });
    }

    // 5. Write Review Form
    const reviewForm = document.getElementById('write-review-form');
    if (reviewForm) {
      reviewForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
          institution_id: document.getElementById('review-modal-inst-id').value,
          author: document.getElementById('review-author').value,
          role: document.getElementById('review-role').value,
          rating: parseFloat(document.getElementById('review-rating').value),
          title: document.getElementById('review-title').value,
          comment: document.getElementById('review-comment').value,
          roll_number: document.getElementById('review-roll').value
        };

        try {
          const res = await fetch('/api/reviews', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const data = await res.json();
          if (data.success) {
            alert(`⭐ Verified Review Posted!\n\n${data.message}`);
            closeModal('write-review-modal');
            reviewForm.reset();
            showToast('Review verified and published!', 'success');
            // Refresh active institution profile
            if (AppState.activeInstitutionId) {
              ProfileController.openProfile(AppState.activeInstitutionId);
            }
          } else {
            alert(`⚠️ Review Error:\n\n${data.error}`);
          }
        } catch (err) {
          showToast('Error submitting review.', 'error');
        }
      });
    }
  },

  // Interactive Live Chat Assistant
  initChat() {
    const chatInput = document.getElementById('chat-input-field');
    const sendBtn = document.getElementById('chat-send-btn');
    const messagesContainer = document.getElementById('chat-messages-container');

    if (!sendBtn || !chatInput) return;

    const sendMessage = async (text) => {
      const msg = text || chatInput.value.trim();
      if (!msg) return;

      // Render user message
      this.appendChatMessage('user', msg);
      chatInput.value = '';

      // Typing indicator
      const typingId = this.appendTypingIndicator();

      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            institution_id: AppState.chatInstitutionId,
            message: msg
          })
        });
        const data = await res.json();
        this.removeTypingIndicator(typingId);
        this.appendChatMessage('assistant', data.reply);
      } catch (err) {
        this.removeTypingIndicator(typingId);
        this.appendChatMessage('assistant', "I'm having trouble connecting to the admissions server. Please try again.");
      }
    };

    sendBtn.addEventListener('click', () => sendMessage());
    chatInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendMessage();
    });

    // Suggested query chips
    document.querySelectorAll('.chat-suggestion-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        sendMessage(chip.textContent.trim());
      });
    });
  },

  appendChatMessage(sender, text) {
    const container = document.getElementById('chat-messages-container');
    if (!container) return;

    const div = document.createElement('div');
    const isUser = sender === 'user';
    div.className = `flex ${isUser ? 'justify-end' : 'justify-start'} mb-3`;

    // Format markdown bold & linebreaks
    const formatted = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br/>');

    div.innerHTML = `
      <div class="max-w-[85%] rounded-2xl px-4 py-2.5 text-xs ${isUser ? 'bg-blue-600 text-white rounded-br-none shadow-sm' : 'bg-slate-100 text-slate-800 rounded-bl-none border border-slate-200'}">
        ${formatted}
      </div>
    `;

    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
  },

  appendTypingIndicator() {
    const container = document.getElementById('chat-messages-container');
    if (!container) return null;
    const id = 'typing-' + Date.now();
    const div = document.createElement('div');
    div.id = id;
    div.className = 'flex justify-start mb-3';
    div.innerHTML = `
      <div class="bg-slate-100 text-slate-400 rounded-2xl px-4 py-2.5 text-xs rounded-bl-none flex items-center gap-1">
        <span class="animate-bounce">●</span>
        <span class="animate-bounce delay-100">●</span>
        <span class="animate-bounce delay-200">●</span>
      </div>
    `;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
    return id;
  },

  removeTypingIndicator(id) {
    if (!id) return;
    const el = document.getElementById(id);
    if (el) el.remove();
  },

  // Institution Admin Dashboard Loader
  async loadAdminData() {
    const enquiriesContainer = document.getElementById('admin-enquiries-list');
    const visitsContainer = document.getElementById('admin-visits-list');
    const claimsContainer = document.getElementById('admin-claims-list');

    try {
      const [leadsRes, claimsRes] = await Promise.all([
        fetch('/api/admin/leads'),
        fetch('/api/admin/claims')
      ]);

      const leadsData = await leadsRes.json();
      const claimsData = await claimsRes.json();

      // Render enquiries
      if (enquiriesContainer) {
        enquiriesContainer.innerHTML = leadsData.enquiries.map(enq => `
          <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="font-bold text-slate-900 text-xs">${enq.student_name}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-100 text-blue-800">${enq.target_course}</span>
                <span class="text-xs text-slate-400">•</span>
                <span class="text-xs text-slate-500 font-semibold">${enq.institution_name}</span>
              </div>
              <p class="text-xs text-slate-600 mb-1">"${enq.message}"</p>
              <div class="text-[11px] text-slate-400">📞 ${enq.phone} • ✉️ ${enq.email}</div>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <span class="px-2.5 py-1 rounded-full text-[10px] font-bold ${enq.status === 'Responded' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
                ${enq.status}
              </span>
              <button onclick="alert('Replying to ${enq.student_name} at ${enq.email}...')" class="px-3 py-1.5 bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white rounded-lg text-xs font-bold transition">
                Contact
              </button>
            </div>
          </div>
        `).join('');
      }

      // Render visits
      if (visitsContainer) {
        visitsContainer.innerHTML = leadsData.campus_visits.map(v => `
          <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="font-bold text-slate-900 text-xs">${v.visitor_name}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-100 text-emerald-800">Pass #${v.visit_pass_id}</span>
                <span class="text-xs text-slate-500">(${v.attendees} visitors)</span>
              </div>
              <div class="text-xs text-slate-600 font-medium">🗓️ ${v.visit_date} • ${v.slot}</div>
              <div class="text-[11px] text-slate-400 mt-1">Campus: ${v.institution_name}</div>
            </div>
            <span class="px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold rounded-lg">
              Authorized Pass
            </span>
          </div>
        `).join('');
      }

      // Render claims
      if (claimsContainer) {
        claimsContainer.innerHTML = claimsData.claims.map(c => `
          <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="font-bold text-slate-900 text-xs">${c.institution_name}</span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold ${c.status === 'APPROVED' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
                  ${c.status}
                </span>
              </div>
              <p class="text-xs text-slate-600">Applicant: ${c.applicant_name} (${c.designation})</p>
              <div class="text-[11px] text-slate-400 mt-1">Auditor Notes: ${c.auditor_notes}</div>
            </div>
            <span class="text-xs font-mono font-bold text-slate-600">${c.claim_id}</span>
          </div>
        `).join('');
      }

    } catch (err) {
      console.error(err);
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.AdminController.init();
});
