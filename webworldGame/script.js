// 游戏状态
const gameState = {
    fireBurning: true,
    selectedWood: null,
    usedWoods: [],
    fireTimer: null,
    fireDuration: 10000, // 10秒后火堆熄灭
    woodCount: 4
};

// 按钮框架 - 每个按钮由emoji+文字组成
const buttonFramework = {
    // 火堆按钮
    fire: {
        emoji: '🔥',
        text: '火堆',
        method: handleFireClick,
        states: {
            burning: { emoji: '🔥', text: '火堆' },
            extinguished: { emoji: '💀', text: '熄灭' }
        }
    },
    
    // 木头按钮
    woods: {
        emoji: '🪵',
        text: '木头',
        method: handleWoodClick,
        states: {
            normal: { emoji: '🪵', text: '木头' },
            selected: { emoji: '🪵', text: '已选' },
            used: { emoji: '🌫️', text: '用完' }
        }
    }
};

// 更新按钮显示
function updateButtonDisplay(elementId, state) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const emojiSpan = element.querySelector('.emoji');
    const textSpan = element.querySelector('.text');
    
    if (elementId === 'fire') {
        const fireState = buttonFramework.fire.states[state];
        if (fireState) {
            emojiSpan.textContent = fireState.emoji;
            textSpan.textContent = fireState.text;
        }
    } else if (elementId.startsWith('wood')) {
        const woodState = buttonFramework.woods.states[state];
        if (woodState) {
            emojiSpan.textContent = woodState.emoji;
            textSpan.textContent = woodState.text;
        }
    }
}

// 火堆点击处理
function handleFireClick() {
    console.log('火堆被点击了！');
    
    // 如果有选中的木头，添加到火堆
    if (gameState.selectedWood) {
        addWoodToFire(gameState.selectedWood);
    } else {
        // 如果没有选中木头，显示提示
        showMessage('请先选择一块木头！');
    }
}

// 木头点击处理
function handleWoodClick(woodId) {
    console.log(`木头 ${woodId} 被点击了！`);
    
    // 如果木头已经被使用，不能选择
    if (gameState.usedWoods.includes(woodId)) {
        showMessage('这块木头已经用过了！');
        return;
    }
    
    // 取消之前选中的木头
    if (gameState.selectedWood) {
        const prevWood = document.getElementById(gameState.selectedWood);
        prevWood.classList.remove('selected');
        updateButtonDisplay(gameState.selectedWood, 'normal');
    }
    
    // 选中新的木头
    gameState.selectedWood = woodId;
    const wood = document.getElementById(woodId);
    wood.classList.add('selected');
    updateButtonDisplay(woodId, 'selected');
    
    showMessage(`选中了 ${woodId}！`);
}

// 添加木头到火堆
function addWoodToFire(woodId) {
    console.log(`将木头 ${woodId} 添加到火堆`);
    
    // 标记木头为已使用
    gameState.usedWoods.push(woodId);
    const wood = document.getElementById(woodId);
    wood.classList.remove('selected');
    wood.classList.add('used');
    updateButtonDisplay(woodId, 'used');
    
    // 重新点燃火堆
    relightFire();
    
    // 清除选中状态
    gameState.selectedWood = null;
    
    showMessage('火堆重新燃烧了！');
}

// 重新点燃火堆
function relightFire() {
    const fire = document.getElementById('fire');
    fire.classList.remove('extinguished');
    fire.classList.add('burning');
    updateButtonDisplay('fire', 'burning');
    gameState.fireBurning = true;
    
    // 清除之前的定时器
    if (gameState.fireTimer) {
        clearTimeout(gameState.fireTimer);
    }
    
    // 设置新的熄灭定时器
    gameState.fireTimer = setTimeout(() => {
        extinguishFire();
    }, gameState.fireDuration);
}

// 火堆熄灭
function extinguishFire() {
    console.log('火堆熄灭了！');
    
    const fire = document.getElementById('fire');
    fire.classList.remove('burning');
    fire.classList.add('extinguished');
    updateButtonDisplay('fire', 'extinguished');
    gameState.fireBurning = false;
    
    showMessage('火堆熄灭了！需要添加木头重新点燃。');
}

// 显示消息
function showMessage(message) {
    console.log(message);
    
    // 创建临时消息显示
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        z-index: 1000;
        animation: fadeInOut 3s ease-in-out;
    `;
    
    document.body.appendChild(messageDiv);
    
    // 3秒后移除消息
    setTimeout(() => {
        if (messageDiv.parentElement) {
            messageDiv.parentElement.removeChild(messageDiv);
        }
    }, 3000);
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('火堆游戏初始化完成！');
    
    // 添加消息动画样式
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInOut {
            0%, 100% { opacity: 0; transform: translateX(-50%) translateY(-20px); }
            20%, 80% { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
    `;
    document.head.appendChild(style);
    
    // 初始化按钮显示
    updateButtonDisplay('fire', 'burning');
    updateButtonDisplay('wood1', 'normal');
    updateButtonDisplay('wood2', 'normal');
    updateButtonDisplay('wood3', 'normal');
    updateButtonDisplay('wood4', 'normal');
    
    // 开始火堆熄灭倒计时
    gameState.fireTimer = setTimeout(() => {
        extinguishFire();
    }, gameState.fireDuration);
    
    showMessage('游戏开始！点击木头选择，然后点击火堆添加燃料。');
});

// 导出函数供HTML调用
window.handleFireClick = handleFireClick;
window.handleWoodClick = handleWoodClick;
