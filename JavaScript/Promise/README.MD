JavaScript の Promise は非同期処理を扱うためのオブジェクトで、「将来的に成功または失敗する値」を表します。3つの状態（pending, fulfilled, rejected）を持ち、then と catch を使って結果の処理やエラー処理が可能です。複数の非同期処理をまとめる Promise.all や Promise.race なども便利です。
fetch=>
1.成功
.then(
    (results) => 
    {
        処理
    }
);
　
2.失敗
.catch