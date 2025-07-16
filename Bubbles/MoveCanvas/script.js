// 获取canvas和上下文
const canvas = document.getElementById('moveCanvas');
const ctx = canvas.getContext('2d');

// 全局偏移量，用于画布平移
let offsetX = 0, offsetY = 0;
// 是否正在拖动画布
let draggingCanvas = false;
// 记录上一次鼠标位置
let lastMouseX, lastMouseY;

// 参照物方块参数
const boxSize = 80;
const boxCenter = { x: 400, y: 300 };

// 绘制画布内容（参照物方块和十字线）
function draw() {
  // 清空画布
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // 画参照物方块
  ctx.save();
  ctx.fillStyle = '#FF7043';
  ctx.strokeStyle = '#BF360C';
  ctx.lineWidth = 3;
  ctx.fillRect(boxCenter.x - boxSize/2 + offsetX, boxCenter.y - boxSize/2 + offsetY, boxSize, boxSize);
  ctx.strokeRect(boxCenter.x - boxSize/2 + offsetX, boxCenter.y - boxSize/2 + offsetY, boxSize, boxSize);
  ctx.restore();
  // 画十字线，帮助观察平移效果
  ctx.save();
  ctx.strokeStyle = '#1976D2';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(boxCenter.x + offsetX, 0);
  ctx.lineTo(boxCenter.x + offsetX, canvas.height);
  ctx.moveTo(0, boxCenter.y + offsetY);
  ctx.lineTo(canvas.width, boxCenter.y + offsetY);
  ctx.stroke();
  ctx.restore();
}

// 初始绘制
draw();

// 鼠标按下事件，开始拖动画布
canvas.onmousedown = function(e) {
  draggingCanvas = true;
  lastMouseX = e.clientX;
  lastMouseY = e.clientY;
};

// 鼠标移动事件，实时更新偏移量并重绘
canvas.onmousemove = function(e) {
  if (draggingCanvas) {
    offsetX += e.clientX - lastMouseX;
    offsetY += e.clientY - lastMouseY;
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    draw();
  }
};

// 鼠标松开事件，结束拖动
canvas.onmouseup = function(e) {
  draggingCanvas = false;
};

// 鼠标移出画布事件，防止拖动状态丢失
canvas.onmouseleave = function(e) {
  draggingCanvas = false;
}; 