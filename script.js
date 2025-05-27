// const choices = ['グー', 'チョキ', 'パー'];
// const buttons = document.querySelectorAll('#choices button');
// const resultDiv = document.getElementById('result');

// buttons.forEach(button => {
//     button.addEventListener('click', () => {
//         const userChoice = button.getAttribute('data-choice');
//         const cpuChoice = choices[Math.floor(Math.random() * choices.length)];

//         // 勝敗判定
//         let resultText = `あなたは${userChoice}。向こうは${cpuChoice}。<br>`;
//         if (userChoice === cpuChoice) {
//             resultText += '引き分け！';
//         } else if (
//             (userChoice === 'グー' && cpuChoice === 'チョキ') ||
//             (userChoice === 'チョキ' && cpuChoice === 'パー') ||
//             (userChoice === 'パー' && cpuChoice === 'グー')
//         ) {
//             resultText += 'あなたの勝ち！';
//         } else {
//             resultText += 'あなたの負け！';
//         }

//         // 結果を表示
//         resultDiv.innerHTML = resultText;
//     });
// });
// 補足