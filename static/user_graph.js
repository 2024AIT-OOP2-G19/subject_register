const credit_summary_chart = document.getElementById('credit_summary_chart');

    fetch('/api/credit_summary_bar')
      .then(res => res.json())
      .then(data => {
        console.log(data)

        new Chart(credit_summary_chart, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              axis: 'y',
              label: '獲得単位',
              data: data.data,
              fill: false,
              backgroundColor: [
                'rgba(255, 99, 132, 0.5)',  // 半透明の赤
                'rgba(54, 162, 235, 0.5)',  // 半透明の青
                'rgba(255, 206, 86, 0.5)',  // 半透明の黄色
                'rgba(75, 192, 192, 0.5)',  // 半透明の緑
                'rgba(153, 102, 255, 0.5)', // 半透明の紫
                'rgba(255, 159, 64, 0.5)'   // 半透明のオレンジ
              ],
              borderColor: [
                'rgb(0, 128, 255)',  // 青
                'rgb(0, 255, 128)',  // 緑
                'rgb(255, 128, 0)',  // オレンジ
                'rgb(128, 0, 255)',  // 紫
                'rgb(255, 0, 128)',  // ピンク
                'rgb(128, 255, 0)',  // 黄緑
                'rgb(0, 255, 255)'   // シアン
              ],
              borderWidth: 1

            }]
          },
          options: {
            responsive: true,
            indexAxis: 'y',
            scales: {
              x: {
                beginAtZero: true
              }
            }
          }
        })
      })


    const credit_ranking_chart = document.getElementById('credit_ranking_chart');

    fetch('/api/credit_summary_ranking')
      .then(res => res.json())
      .then(data => {
        console.log(data)

        new Chart(credit_ranking_chart, {
          type: 'doughnut',
          data: {
            labels: data.labels,
            datasets: [{
              data: data.data,
              borderWidth: 1

            }]
          },
          options: {
            responsive: true,
             plugins: {
                legend: {
                  position: 'right'
                }
             }
          }
        })
      })