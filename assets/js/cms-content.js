(() => {
  const pageId = document.body && document.body.dataset.cmsPage;
  if (!pageId) return;

  fetch('../content/pages.json', { cache: 'no-store' })
    .then(response => {
      if (!response.ok) throw new Error('CMS content could not be loaded');
      return response.json();
    })
    .then(allPages => {
      const content = allPages[pageId];
      if (!content) return;

      document.querySelectorAll('[data-cms-text]').forEach(element => {
        const key = element.dataset.cmsText;
        if (typeof content[key] === 'string') element.textContent = content[key];
      });

      document.querySelectorAll('[data-cms-href]').forEach(element => {
        const key = element.dataset.cmsHref;
        if (typeof content[key] === 'string') element.setAttribute('href', content[key]);
      });

      document.querySelectorAll('[data-cms-image]').forEach(element => {
        const key = element.dataset.cmsImage;
        if (typeof content[key] === 'string' && content[key]) {
          element.setAttribute('src', content[key]);
          element.removeAttribute('srcset');
        }
        const altKey = element.dataset.cmsAlt;
        if (altKey && typeof content[altKey] === 'string') element.setAttribute('alt', content[altKey]);
      });

      if (typeof content.page_title === 'string') document.title = content.page_title;
      if (typeof content.meta_description === 'string') {
        let meta = document.querySelector('meta[name="description"]');
        if (!meta) {
          meta = document.createElement('meta');
          meta.name = 'description';
          document.head.appendChild(meta);
        }
        meta.content = content.meta_description;
        document.querySelectorAll('meta[property="og:description"]').forEach(item => {
          item.setAttribute('content', content.meta_description);
        });
      }
    })
    .catch(error => console.warn('Website content remains unchanged:', error));
})();
