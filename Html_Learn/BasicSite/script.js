'use strict';           // 厳格モードを有効化

// 1 動的型 & 2 スコープ
let n = 1;
n = 'hi';               // 型を途中で変更しても OK

// 3 厳密比較 ===
console.log(1 === '1'); // false（型も値も一致しない）

// 4 false 判定
if ('') console.log('実行されない'); //false 0 '' null undefined NaNはfalseと認識

// 5 自動型変換
console.log(1 + '2');   // '12'（数値 + 文字列 → 連結）
console.log('5' * 2);   // 10 （文字列 * 数値 → 数値化）

// 6 NaN
console.log(Number.isNaN(NaN)); // true（NaN 判定専用）

// 7 テンプレートリテラル
const name = 'Wen';
console.log(`こんにちは、${name} さん！`);

// 8 短絡評価（値を返す）
let userInput=false
const title = userInput || 'Untitled'; // userInput が falsy なら 'Untitled'
console.log(title);

// 9 アロー関数（独自 this を持たない）
const obj = {
  val: 42,
  fn: () => console.log(this.val) // 外側の this を参照（ここでは undefined）
};

//10 分割代入
const { x, y } = { x: 3, y: 4 }; // オブジェクトから x, y を取り出す
