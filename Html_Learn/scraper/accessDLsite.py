import requests
from bs4 import BeautifulSoup
import json

# DLsiteのジャンルページURL
url = "https://www.dlsite.com/maniax/fsr/=/genre/256/from/work.genre"
# User-Agentを指定してリクエスト
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# BeautifulSoupでHTMLをパース
soup = BeautifulSoup(response.content, 'html.parser')

# 作品カード（1つ1つの作品情報が入っているdivタグ）を全て取得
# DLsiteではclass_='work'や'work_XXX'のdivが多いので、'work'を含むdivを取得
product_items = soup.find_all(
    'li',
    class_=[
        'search_result_img_box_inner',
        'type_exclusive_01',
        'for_pc'
    ]
)

print(f"{len(product_items)}件の作品カードを取得")

# 作品リストを作成
result = []
for item in product_items:
    title_elem = item.find('dd', class_='work_name')
    title = title_elem.get_text(strip=True) if title_elem else "タイトル不明"
    img_elem = item.find('img')
    img_url = img_elem['src'] if img_elem else ""
    link_elem = item.find('a', href=True)
    link = link_elem['href'] if link_elem else "リンク不明"
    result.append({
        "title": title,
        "img_url": img_url,
        "link": link
    })

# JSONファイルとして保存
with open("HtmlLearn/scraper/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)