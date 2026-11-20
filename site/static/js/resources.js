/* These utilities never read or transmit checklist contents. */
(() => {
  document.querySelector('[data-print]')?.addEventListener('click', () => window.print());
  document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
    const status = document.querySelector('[data-copy-status]');
    const content = button.closest('section')?.querySelector('pre')?.textContent;
    if (!content || !status) return;
    try { await navigator.clipboard.writeText(content); status.textContent = '例文をコピーしました。差し替え箇所を編集してからお使いください。'; }
    catch { status.textContent = 'コピーできませんでした。例文を選択してコピーしてください。'; }
  }));
})();
