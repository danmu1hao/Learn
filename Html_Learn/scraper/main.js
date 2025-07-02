fetch('result.json')
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById('list');
    data.forEach(item => {
      // プロトコル補完 / 补全协议
      const imgSrc = item.img_url.startsWith('//')
                     ? 'https:' + item.img_url
                     : item.img_url;

      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <a href="${item.link}" target="_blank" rel="noopener">
          <img src="${imgSrc}" alt="${item.title}">
        </a>
        <div class="card-title">${item.title}</div>
        <a class="card-link" href="${item.link}" target="_blank" rel="noopener">
          作品ページへ / 作品页面
        </a>
      `;
      list.appendChild(card);
    });
  });
