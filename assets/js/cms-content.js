(() => {
  const pageId = document.body && document.body.dataset.cmsPage;
  if (!pageId) return;

  const readJson = path => fetch(path, { cache: 'no-store' }).then(response => {
    if (!response.ok) throw new Error('Could not load ' + path);
    return response.json();
  });
  const imageUrl = value => {
    if (/^(https?:|data:|blob:)/i.test(value)) return value;
    if (/^(\.\.\/)?\/?assets\/images\//i.test(value)) return '../' + value.replace(/^(\.\.\/)?\/?/, '');
    return value;
  };
  const setText = (selector, attr, source) => {
    document.querySelectorAll(selector).forEach(el => {
      const key = el.getAttribute(attr);
      if (key && typeof source[key] === 'string') el.textContent = source[key];
    });
  };
  const setLinks = (selector, attr, source) => {
    document.querySelectorAll(selector).forEach(el => {
      const key = el.getAttribute(attr);
      if (key && typeof source[key] === 'string') el.setAttribute('href', source[key]);
    });
  };
  const setImages = (selector, attr, altAttr, source) => {
    document.querySelectorAll(selector).forEach(el => {
      const key = el.getAttribute(attr);
      if (key && typeof source[key] === 'string' && source[key]) {
        el.setAttribute('src', imageUrl(source[key]));
        el.removeAttribute('srcset');
      }
      const altKey = el.getAttribute(altAttr);
      if (altKey && typeof source[altKey] === 'string') el.setAttribute('alt', source[altKey]);
    });
  };
  const setBackgrounds = (selector, attr, source) => {
    document.querySelectorAll(selector).forEach(el => {
      const key = el.getAttribute(attr), value = key && source[key];
      if (typeof value !== 'string' || !value) return;
      const url = 'url("' + imageUrl(value).replace(/"/g, '%22') + '")';
      const current = el.style.backgroundImage;
      el.style.backgroundImage = /url\(/i.test(current) ? current.replace(/url\((?:'[^']*'|"[^"]*"|[^)]*)\)/i, url) : url;
    });
  };
  const apply = (content, shared) => {
    setText('[data-cms-text]', 'data-cms-text', content);
    document.querySelectorAll('[data-cms-html]').forEach(el => {
      const key = el.getAttribute('data-cms-html');
      if (key && typeof content[key] === 'string') el.innerHTML = content[key];
    });
    setLinks('[data-cms-href]', 'data-cms-href', content);
    setImages('[data-cms-image]', 'data-cms-image', 'data-cms-alt', content);
    setBackgrounds('[data-cms-background]', 'data-cms-background', content);
    setText('[data-cms-placeholder]', 'data-cms-placeholder', content);
    if (typeof content.page_title === 'string' && content.page_title) document.title = content.page_title;
    if (typeof content.meta_description === 'string' && content.meta_description.trim()) {
      let meta = document.querySelector('meta[name="description"]');
      if (!meta) { meta = document.createElement('meta'); meta.name = 'description'; document.head.appendChild(meta); }
      meta.content = content.meta_description;
      document.querySelectorAll('meta[property="og:description"]').forEach(el => el.setAttribute('content', content.meta_description));
    }
    if (shared) {
      setText('[data-cms-shared-text]', 'data-cms-shared-text', content);
      setLinks('[data-cms-shared-href]', 'data-cms-shared-href', content);
      setImages('[data-cms-shared-image]', 'data-cms-shared-image', 'data-cms-shared-alt', content);
      setBackgrounds('[data-cms-shared-background]', 'data-cms-shared-background', content);
    }
  };
  readJson('../content/pages/' + pageId + '.json').then(page => apply(page, false)).catch(error => console.warn('Website page content was not loaded:', error));
  readJson('../content/shared.json').then(shared => apply(shared, true)).catch(error => console.warn('Shared website content was not loaded:', error));
})();
