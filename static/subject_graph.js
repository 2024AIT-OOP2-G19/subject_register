const register_summary_chart = document.getElementById('register_summary_chart');


fetch('/api/register_summary_bar')

    .then(res => res.json())
    .then(data => {
        console.log(data)

        new Chart(register_summary_chart, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    axis: 'y',
                    label: '履修登録数',
                    data: data.data,
                    fill: false,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
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
      
const subject_ranking_chart = document.getElementById('subject_ranking_chart');

fetch('/api/register_summary_ranking')
      .then(res => res.json())
      .then(data => {
        console.log(data)

        new Chart(subject_ranking_chart, {
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