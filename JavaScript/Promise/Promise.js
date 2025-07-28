function orderFood() {
    return new Promise((resolve, reject) => {
      console.log("🍔 正在下单...");
      setTimeout(() => {
        const success = true; // 假设订单成功了
        if (success) {
          resolve("🍔 你的汉堡做好了！");
        } else {
          reject("❌ 汉堡店关门了！");
        }
      }, 2000); // 模拟2秒等待
    });
  }
  
  orderFood()
    .then(result => {
      console.log("✅ 收到通知：", result);
    })
    .catch(error => {
      console.log("⚠️ 出错了：", error);
    });
  